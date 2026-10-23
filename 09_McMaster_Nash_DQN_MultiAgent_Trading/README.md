# Nash-DQN: Multi-Agent Deep Reinforcement Learning for Optimal Execution

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Multi-Agent RL](https://img.shields.io/badge/Reinforcement%20Learning-Nash--DQN-blue)](https://arxiv.org/)
[![Quantitative Finance](https://img.shields.io/badge/Quantitative%20Finance-Optimal%20Liquidation-brightgreen)](https://www.mcmaster.ca/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Department of Mathematics & Statistics (MATH 4FM3)  
> **Author**: Mohamed Nourou Dine CISSE — Quantitative Researcher / RL Engineer  
> **Core Stack**: `PyTorch`, `Deep Q-Learning (DQN)`, `Multi-Agent RL`, `Stochastic Games`, `Brownian Motion`  
> **Key Deliverables**: 34-page Quantitative Master's Thesis, Trajectory Simulators, Convergence Diagnostics

---

## 🇫🇷 Résumé Rapide en Français

Réalisé durant mon échange académique au **Department of Mathematics & Statistics de l'Université McMaster (Canada)**, ce projet de recherche en finance quantitative explore l'exécution optimale d'ordres de trading en présence d'impact de marché par apprentissage par renforcement multi-agents.

En m'appuyant sur les travaux fondateurs de **Casgrain, Ning & Jaimungal (2022)**, j'ai développé sous **PyTorch** un simulateur de jeu différentiel stochastique à $N$ agents concurrents soumis à un impact de prix temporaire et permanent. Pour surmonter la non-stationnarité inhérente aux jeux multi-agents, j'ai implémenté l'algorithme **Nash-DQN** combinant replay buffer étendu et réseaux cibles stabilisés afin de faire converger les politiques de liquidation vers l'**équilibre de Nash**.

Ce travail a abouti à une thèse quantitative de **34 pages** enrichie de trajectoires browniennes simulées et d'analyses de convergence.

---

## 📌 Executive Summary & Mathematical Model

In financial markets, large orders moved simultaneously by institutional traders depress prices. The mid-price $S_t$ satisfies:

$$dS_t = \left( b_t + \kappa \sum_{j=1}^N 
u_t^j ight) dt + \sigma dW_t$$

where $
u_t^j$ is agent $j$'s liquidation rate, $\kappa$ models permanent price impact, and agent $i$ receives effective transaction price $	ilde{S}_t^i = S_t - \gamma 
u_t^i$.

Each trader maximizes expected terminal terminal inventory liquidation with quadratic penalty $\phi$:

$$\mathcal{J}^i(
u^1, \dots, 
u^N) = \mathbb{E} \left[ \int_0^T \left( q_t^i (b_t + \kappa \sum_{j=1}^N 
u_t^j) - \gamma (
u_t^i)^2 - \phi (q_t^i)^2 ight) dt + q_T^i (S_T - lpha q_T^i) ight]$$

---

## 📊 Key Results

- **Nash Equilibrium Convergence**: Multi-agent policies recovered classical Almgren-Chriss liquidation profiles under low competition and learned stealth execution strategies under high competitive pressure.
- **Academic Thesis**: Authored 34-page formal mathematical monograph complete with stochastic calculus proofs and Bellman PDE verification.

---

## 📂 Repository Layout

```text
09_McMaster_Nash_DQN_MultiAgent_Trading/
├── src/
│   ├── market_environment.py        # N-agent stochastic differential game simulator
│   ├── dqn_agent.py                 # Deep Q-Network policy with target network
│   └── train_multiagent.py          # Multi-agent simulation loop and metrics tracker
├── reports/
│   └── Rapport_Nash_DQN_Optimal_Trading.pdf # Full 34-page quantitative thesis
├── visuals/
│   └── all_agents_rewards.png       # Convergence of cumulative rewards
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n