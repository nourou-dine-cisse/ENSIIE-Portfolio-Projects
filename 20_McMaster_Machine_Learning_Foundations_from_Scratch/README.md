# Machine Learning Foundations & Neural Networks from Scratch: McMaster University

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Vectorized%20Math-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Autograd-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Machine Learning & Neural Networks  
> **Author**: Mohamed Nourou Dine CISSE — Lead ML Researcher  
> **Core Stack**: `NumPy`, `Vectorized Backprop`, `Autograd`, `Optimization`, `Decision Trees from Scratch`, `MNIST`  
> **Key Deliverables**: 6 Rigorous Homework & Research Suites, Vectorized Engine, Comparative Benchmarks



---

> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).

---

## 📐 Mathematical Formulation: Vectorized Backpropagation

For layer $l \in \{1, \dots, L\}$, batch input $\mathbf{X} \in \mathbb{R}^{B 	imes d_{in}}$:

$$\mathbf{Z}^{(l)} = \mathbf{A}^{(l-1)} \mathbf{W}^{(l)} + \mathbf{b}^{(l)}, \quad \mathbf{A}^{(l)} = \sigma(\mathbf{Z}^{(l)})$$

Output error and recursive upstream backward propagation:

$$oldsymbol{\delta}^{(L)} = 
abla_{\mathbf{A}^{(L)}} \mathcal{L} \odot \sigma'(\mathbf{Z}^{(L)}), \quad oldsymbol{\delta}^{(l)} = \left(oldsymbol{\delta}^{(l+1)} (\mathbf{W}^{(l+1)})^T
ight) \odot \sigma'(\mathbf{Z}^{(l)})$$

Parameter gradients computed in a single vectorized matrix product:

$$
abla_{\mathbf{W}^{(l)}} \mathcal{L} = rac{1}{B} (\mathbf{A}^{(l-1)})^T oldsymbol{\delta}^{(l)}, \quad 
abla_{\mathbf{b}^{(l)}} \mathcal{L} = rac{1}{B} \sum_{i=1}^B oldsymbol{\delta}_{i,:}^{(l)}$$

---

## 📂 Repository Architecture

```text
McMaster-Machine-Learning-Foundations-from-Scratch/
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
│   └── HW21.ipynb                                    # Multi-feature polynomial regressions
├── 04_Logistic_Classification_HW3/                    # Multi-Class Classification & Loss Functions
│   ├── Exercise1.ipynb                               # Cross-entropy loss formulation
│   ├── Exercise2.ipynb                               # Softmax multi-class logistic regression
│   └── Exercise3.ipynb                               # Diagnostic classifier
├── 05_Neural_Networks_and_MNIST_HW4/                  # Deep Perceptrons on High-Dimensional Data
│   ├── Exercise 1.ipynb                              # Multi-layer perceptron (MLP) forward propagation
│   ├── Exercise 2.ipynb                              # MNIST handwritten digit classification
│   └── Exercise 4.ipynb                              # Regularization, dropout & weight decay dynamics
└── 06_Decision_Trees_from_Scratch_HW5/                # Recursive Non-Parametric Modeling
    ├── exercise1.ipynb                               # Greedy recursive binary splitting
    ├── exercise2.ipynb                               # MSE impurity reduction & optimal split search
    ├── exercise3.ipynb                               # My_TreeRegressor recursive implementation
    └── exercise5.ipynb                               # Non-linear sine wave regression vs. Scikit-learn
```

---

---

## 🇫🇷 Résumé Rapide en Français

Développée au sein du département de recherche en apprentissage automatique de l'**Université McMaster (Canada)**, cette suite d'ingénierie algorithmique explore les fondements mathématiques et l'implémentation de zéro (*from scratch*) des piliers du Machine Learning :
1. **Rétropropagation Vectorisée en pur NumPy** : Dérivation matricielle analytique complète des gradients sur un réseau multicouche, éliminant toute boucle itérative par échantillon via des opérations tensorielles vectorisées.
2. **Algorithmes d'Optimisation Non-Convexe** : Implémentation de la recherche par coordonnées d'ordre zéro, de la descente de gradient avec recherche linéaire de pas, de l'accélération par momentum et de la méthode du second ordre de Newton.
3. **Arbre de Décision from Scratch (`My_TreeRegressor`)** : Implémentation récursive complète de l'algorithme de partitionnement binaire gourmand basé sur la réduction d'impureté MSE, benchmarké face à Scikit-learn.
4. **Perceptrons Profonds sur MNIST** : Entraînement de classifieurs neuronaux sur données de haute dimension (784 dimensions) avec étude des frontières de décision non-linéaires.

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n
