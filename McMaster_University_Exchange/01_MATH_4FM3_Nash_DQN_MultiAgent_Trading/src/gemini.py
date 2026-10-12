import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from collections import deque, namedtuple

# ==============================================================================
# I. THE MARKET ENVIRONMENT (Table 1: arXiv 1904.10554)
# ==============================================================================

class TradingEnv:
    def __init__(self, n_agents=5):
        self.kappa, self.theta, self.sigma = 0.1, 10.0, 0.01
        self.gamma, self.rho, self.eta = 0.02, 0.5, 0.05
        self.b1, self.b2, self.b3 = 0.1, 0.1, 0.01
        self.N, self.T, self.M = n_agents, 5.0, 10
        self.dt = self.T / self.M

    def reset(self):
        self.S, self.Y, self.t = 10.0, 0.0, 0.0
        self.inv = np.ones(self.N)
        return self._get_state(), self.inv.copy()

    def _get_state(self):
        # Normalized state as per Equation 20 in the paper
        total_sold = np.sum(1.0 - self.inv)
        return np.array([self.S / 10.0, self.t / self.T, total_sold, self.Y], dtype=np.float32)

    def step(self, actions):
        nu = np.array(actions).flatten()
        nu_bar = np.sum(nu)
        rewards = np.zeros(self.N)
        is_terminal = self.t >= self.T - self.dt - 1e-9
        
        for i in range(self.N):
            rewards[i] = -nu[i]*(self.S + self.b1*nu[i])*self.dt - self.b3*(self.inv[i]**2)*self.dt
            if is_terminal:
                q_T = self.inv[i] + nu[i]*self.dt
                rewards[i] += q_T * (self.S - self.b2*q_T)

        self.inv += nu * self.dt
        self.t += self.dt
        Y_old = self.Y
        h = np.sign(nu_bar) * np.sqrt(np.abs(nu_bar) + 1e-8)
        self.Y = (1 - self.rho*self.dt)*self.Y + self.gamma*h*self.dt
        drift = self.kappa*(self.theta - self.S) + self.eta*nu_bar
        self.S += drift*self.dt + (self.Y - Y_old) + self.sigma*np.sqrt(self.dt)*np.random.randn()
        return self._get_state(), self.inv.copy(), rewards, self.t >= self.T - 1e-9

# ==============================================================================
# II. NASH-DQN ARCHITECTURE (Eq 4.9 & 4.10)
# ==============================================================================

def _mlp(sizes):
    layers = []
    for i in range(len(sizes)-1):
        layers.append(nn.Linear(sizes[i], sizes[i+1]))
        if i < len(sizes)-2: layers.append(nn.SiLU())
    return nn.Sequential(*layers)

class NashDQN(nn.Module):
    def __init__(self, d_state=4, n_agents=5):
        super().__init__()
        self.n_agents = n_agents
        self.value_net = _mlp([d_state, 32, 32, 32, 32, 1])
        # Permutation-invariant Head (phi and sigma from Eq 4.10)
        self.phi = _mlp([1, 20, 20, 20])
        self.sigma_net = _mlp([1, 2])
        self.adv_main = _mlp([d_state + 32, 32, 32, 32, 32])
        self.adv_head = nn.Linear(32, 5)

    def get_params(self, x, inv):
        p_feat = self.sigma_net(self.phi(inv.unsqueeze(-1)).sum(dim=1))
        h = self.adv_main(torch.cat([x, p_feat], dim=-1))
        raw = self.adv_head(h)
        mu = raw[:, 0]
        P11 = raw[:, 1].pow(2) + 1e-6 # Cholesky constraint for concavity
        P12, P22, psi = raw[:, 2], raw[:, 3], raw[:, 4]
        def expand(t): return t.unsqueeze(1).expand(-1, self.n_agents).contiguous()
        return expand(mu), expand(P11), expand(P12), expand(P22), expand(psi)

    def forward(self, x, inv, u):
        V = self.value_net(x).expand(-1, self.n_agents)
        mu, P11, P12, P22, psi = self.get_params(x, inv)
        delta = u - mu
        delta_others = delta.sum(dim=1, keepdim=True) - delta
        A = (-P11*delta**2 - P12*delta*delta_others - P22*delta_others**2 + psi*delta_others)
        return V + A, psi

    def nash_action(self, x, inv):
        mu, _, _, _, _ = self.get_params(x, inv)
        return mu

# ==============================================================================
# III. EVALUATION & VISUALIZATION
# ==============================================================================

def run_evaluation(env, model, episodes=100):
    nash_rewards, twap_rewards = [], []
    device = next(model.parameters()).device
    
    for _ in range(episodes):
        # 1. Evaluate Nash-DQN
        s, q = env.reset()
        ep_r = 0
        for _ in range(env.M):
            st, qt = torch.FloatTensor(s).to(device).unsqueeze(0), torch.FloatTensor(q).to(device).unsqueeze(0)
            a = model.nash_action(st, qt).detach().cpu().numpy().flatten()
            s, q, r, _ = env.step(a)
            ep_r += np.mean(r)
        nash_rewards.append(ep_r)

        # 2. Evaluate TWAP (Benchmark: constant liquidation rate)
        s, q = env.reset()
        ep_r_twap = 0
        twap_action = np.ones(env.N) * (1.0 / env.T) # Liquidate 1.0 over time T
        for _ in range(env.M):
            s, q, r, _ = env.step(-twap_action) # Selling
            ep_r_twap += np.mean(r)
        twap_rewards.append(ep_r_twap)

    return nash_rewards, twap_rewards

def plot_results(nash_r, twap_r, losses, final_inv):
    plt.figure(figsize=(15, 5))
    
    # 1. Reward Comparison Box Plot
    plt.subplot(1, 3, 1)
    sns.boxplot(data=[nash_r, twap_r], palette="Set2")
    plt.xticks([0, 1], ['Nash-DQN', 'TWAP'])
    plt.title("Reward Distribution Comparison")
    
    # 2. Learning Curve
    plt.subplot(1, 3, 2)
    plt.plot(losses, color='royalblue', alpha=0.6)
    plt.yscale('log')
    plt.title("Training Loss (TD + Beta-Reg)")
    plt.xlabel("Step")

    # 3. Final Inventory
    plt.subplot(1, 3, 3)
    plt.bar(range(len(final_inv)), final_inv, color='coral')
    plt.title("Remaining Inventory per Agent")
    plt.xlabel("Agent ID")
    plt.show()

# ==============================================================================
# IV. MAIN TRAINING LOOP
# ==============================================================================

def train_and_visualize():
    env = TradingEnv(n_agents=3)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = NashDQN(n_agents=3).to(device)
    optimizer = optim.Adam(model.parameters(), lr=3e-4)
    memory = deque(maxlen=50000)
    Transition = namedtuple('T', ('s', 'q', 'a', 'r', 's2', 'q2', 'd'))

    episodes, batch_size, beta = 1500, 64, 5.0
    sigma, sigma_min, decay = 0.3, 0.05, 0.999
    loss_history = []

    print("Training Nash-DQN...")
    for ep in range(episodes):
        s, q = env.reset()
        for _ in range(env.M):
            st, qt = torch.FloatTensor(s).to(device).unsqueeze(0), torch.FloatTensor(q).to(device).unsqueeze(0)
            mu = model.nash_action(st, qt).detach().cpu().numpy()
            noise = np.random.normal(0, sigma, size=env.N); noise -= noise.mean() 
            a = np.clip(mu + noise, -2.0, 2.0).flatten()
            
            s2, q2, r, done = env.step(a)
            memory.append(Transition(s, q, a, r, s2, q2, done))
            
            if len(memory) > batch_size:
                b = random.sample(memory, batch_size)
                batch = Transition(*zip(*b))
                bs, bq = torch.FloatTensor(np.array(batch.s)).to(device), torch.FloatTensor(np.array(batch.q)).to(device)
                ba, br = torch.FloatTensor(np.array(batch.a)).to(device), torch.FloatTensor(np.array(batch.r)).to(device) / 10.0
                bd = torch.FloatTensor(np.array(batch.d)).to(device).unsqueeze(1)
                
                # Target bootstrapping from Nash action
                with torch.no_grad():
                    q_next, _ = model(torch.FloatTensor(np.array(batch.s2)).to(device), 
                                      torch.FloatTensor(np.array(batch.q2)).to(device), 
                                      model.nash_action(torch.FloatTensor(np.array(batch.s2)).to(device), 
                                                       torch.FloatTensor(np.array(batch.q2)).to(device)))
                    y = br + 0.95 * q_next * (1 - bd)

                q_pred, psi = model(bs, bq, ba)
                loss = F.smooth_l1_loss(q_pred, y) + beta * psi.abs().mean()
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                loss_history.append(loss.item())
            
            s, q = s2, q2
        sigma = max(sigma_min, sigma * decay)
        if ep % 200 == 0: print(f"Episode {ep} | Sigma: {sigma:.3f} | Final Inventory: {q}")

    # Results
    print("\n--- Final Results ---")
    nash_r, twap_r = run_evaluation(env, model)
    print(f"Mean Reward: Nash-DQN = {np.mean(nash_r):.4f} | TWAP = {np.mean(twap_r):.4f}")
    
    # Nash Deviation Check: Unilateral deviation of +0.5 to action
    st_eval, qt_eval = torch.FloatTensor(s).to(device).unsqueeze(0), torch.FloatTensor(q).to(device).unsqueeze(0)
    mu_eval = model.nash_action(st_eval, qt_eval)
    dev_a = mu_eval.clone(); dev_a += 0.5
    q_nash, _ = model(st_eval, qt_eval, mu_eval)
    q_dev, _ = model(st_eval, qt_eval, dev_a)
    print(f"Nash Verification: Q(Nash) = {q_nash:.4f} | Q(Deviate) = {q_dev:.4f}")
    print(f"Regret (Deviation Loss): {max(0, q_nash.item() - q_dev.item()):.4f}")

    plot_results(nash_r, twap_r, loss_history, q)

if __name__ == "__main__":
    train_and_visualize()