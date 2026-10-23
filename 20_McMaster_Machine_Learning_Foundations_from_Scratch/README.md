# Machine Learning Foundations & Neural Networks from Scratch: McMaster University

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Vectorized%20Math-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Autograd-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A rigorous mathematical and algorithmic exploration of foundational machine learning, non-convex optimization, and deep neural network training implemented from first principles. Developed during the **Machine Learning & Neural Networks** graduate curriculum at **McMaster University (Hamilton, Canada)**.

---

## 📌 Repository Architecture

```text
McMaster-Machine-Learning-Foundations-from-Scratch/
├── README.md                                          # Mathematical derivations & architecture
├── 01_Vectorized_Backpropagation_NumPy/               # Analytical Backpropagation from Scratch
│   └── FullBackProp.ipynb                            # Vectorized forward & backward passes in pure NumPy
├── 02_Optimization_Algorithms_HW1/                    # Non-Convex Numerical Optimization
│   ├── Exercise1.ipynb                               # Zero-order coordinate search algorithms
│   ├── Exercise2.ipynb                               # Gradient descent step-length selection
│   ├── Exercise3.ipynb                               # Momentum and accelerated gradient schemes
│   ├── Exercise4.ipynb                               # Second-order Newton's method
│   └── Exercise5.ipynb                               # Autograd loss surface benchmarking
├── 03_Linear_Regression_and_Nonlinear_Features_HW2/   # Statistical Regression
│   ├── Exercise1.ipynb                               # Linear least squares & normal equations
│   ├── Exercise3.ipynb                               # Student debt temporal regression
│   ├── Exercise4.ipynb                               # Kleiber's Law allometric scaling
│   └── HW21.ipynb                                    # Multi-feature polynomial regressions
├── 04_Logistic_Classification_HW3/                    # Multi-Class Classification & Loss Functions
│   ├── Exercise1.ipynb                               # Cross-entropy loss formulation
│   ├── Exercise2.ipynb                               # Softmax multi-class logistic regression
│   ├── Exercise3.ipynb                               # Wisconsin Breast Cancer diagnostic classifier
│   └── Exercise4.ipynb                               # Credit risk classification with ROC-AUC analysis
├── 05_Neural_Networks_and_MNIST_HW4/                  # Deep Perceptrons on High-Dimensional Data
│   ├── Exercise 1.ipynb                              # Multi-layer perceptron (MLP) forward propagation
│   ├── Exercise 2.ipynb                              # MNIST handwritten digit classification (784-dim input)
│   ├── Exercise 4.ipynb                              # Regularization, dropout & weight decay dynamics
│   └── Exercise 6.ipynb                              # Non-linear decision boundaries & 2D span projection
└── 06_Decision_Trees_from_Scratch_HW5/                # Recursive Non-Parametric Modeling
    ├── exercise1.ipynb                               # Greedy recursive binary splitting
    ├── exercise2.ipynb                               # MSE impurity reduction & optimal split search
    ├── exercise3.ipynb                               # My_TreeRegressor recursive implementation
    └── exercise5.ipynb                               # Non-linear sine wave regression vs. Scikit-learn
```

---

## 📐 Mathematical Formulations & Implementations

### 1. Vectorized Analytical Backpropagation (Pure NumPy)
For a network with $L$ layers, input batch $\mathbf{X} \in \mathbb{R}^{B \times d_{in}}$, activations $\mathbf{A}^{(l)}$, weights $\mathbf{W}^{(l)}$, and biases $\mathbf{b}^{(l)}$:

- **Forward Propagation**:
  $$\mathbf{Z}^{(l)} = \mathbf{A}^{(l-1)} \mathbf{W}^{(l)} + \mathbf{b}^{(l)}, \quad \mathbf{A}^{(l)} = \sigma(\mathbf{Z}^{(l)})$$
- **Analytical Output Layer Gradient**:
  $$\boldsymbol{\delta}^{(L)} = \nabla_{\mathbf{A}^{(L)}} \mathcal{L} \odot \sigma'(\mathbf{Z}^{(L)})$$
- **Recursive Backpropagation Error**:
  $$\boldsymbol{\delta}^{(l)} = \left(\boldsymbol{\delta}^{(l+1)} (\mathbf{W}^{(l+1)})^T\right) \odot \sigma'(\mathbf{Z}^{(l)})$$
- **Parameter Gradients**:
  $$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \frac{1}{B} (\mathbf{A}^{(l-1)})^T \boldsymbol{\delta}^{(l)}, \quad \frac{\partial \mathcal{L}}{\partial \mathbf{b}^{(l)}} = \frac{1}{B} \sum_{i=1}^B \boldsymbol{\delta}_{i,:}^{(l)}$$

The vectorized implementation eliminates iterative Python loops over samples, achieving high throughput matrix multiplications via BLAS.

---

### 2. Numerical Optimization Suite
- **Zero-Order Coordinate Search**: Optimizes derivative-free objective functions by probing canonical coordinate axes with decaying step sizes.
- **Gradient Descent with Backtracking Line Search**:
  $$\mathbf{w}_{k+1} = \mathbf{w}_k - \alpha_k \nabla g(\mathbf{w}_k)$$
- **Momentum Acceleration**: Incorporates velocity vectors to traverse ill-conditioned ravines and escape shallow saddle points.

---

### 3. Decision Tree Regressor from First Principles
Implemented recursive binary splitting algorithm `My_TreeRegressor` from scratch:
- At each internal node, searches over all features $j$ and split thresholds $s$ to maximize Mean Squared Error (MSE) impurity reduction:
  $$\Delta \text{MSE} = \text{MSE}_{\text{parent}} - \left(\frac{N_L}{N} \text{MSE}_L + \frac{N_R}{N} \text{MSE}_R\right)$$
- Base cases: maximum tree depth $d_{\max}$ or minimum leaf size $N_{\min}$.
- Benchmarked on synthetic multi-frequency sine wave regressions against `sklearn.tree.DecisionTreeRegressor`.

---

## 🛠️ Quickstart

```bash
git clone https://github.com/nourou-dine-cisse/McMaster-Machine-Learning-Foundations-from-Scratch.git
cd McMaster-Machine-Learning-Foundations-from-Scratch
pip install numpy pandas matplotlib autograd tensorflow scikit-learn jupyter
jupyter notebook 01_Vectorized_Backpropagation_NumPy/FullBackProp.ipynb
```

---

## 👤 Author
**Mouhamed Nourou Dine Cisse**  
- **McMaster University** (Hamilton, ON, Canada) — Academic Exchange in Applied AI & Machine Learning  
- **Université Paris-Saclay & ENSIIE** — Master 2 in Artificial Intelligence (M2IA) & Diplôme d'Ingénieur  
- Portfolio: [nourouportfoliowebsite.vercel.app](https://nourouportfoliowebsite.vercel.app)  
- GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)  
- LinkedIn: [mouhamed-nourou-dine-cisse](https://linkedin.com/in/mouhamed-nourou-dine-cisse-094159327)
