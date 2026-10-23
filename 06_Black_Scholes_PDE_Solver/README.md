# Modern C++17 Black-Scholes PDE Solver: Finite Differences & Real-Time SDL2

[![C++17](https://img.shields.io/badge/C++-17-00599C?style=flat&logo=c%2B%2B&logoColor=white)](https://en.cppreference.com/)
[![CMake](https://img.shields.io/badge/CMake-Build%20System-064F8C?style=flat&logo=cmake&logoColor=white)](https://cmake.org/)
[![SDL2](https://img.shields.io/badge/SDL2-Real--time%20Graphics-red)](https://www.libsdl.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: ENSIIE Applied Mathematics & Scientific Computing Curriculum (2A PRAV)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `C++17`, `Finite Differences`, `Implicit Scheme`, `Thomas Algorithm`, `SDL2`, `OOP`  
> **Key Deliverables**: 25-page Formal Scientific Report, High-Performance Solver, Interactive Visualizer

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de calcul scientifique haute performance implémente en **C++17 moderne** un solveur numérique pour l'**Équation aux Dérivées Partielles (EDP) de Black-Scholes**, utilisée pour la valorisation d'options financières européennes (Call et Put). 

Sur le plan mathématique, nous avons discrétisé l'EDP selon les schémas aux **différences finies explicites et implicites**. Pour garantir la stabilité numérique inconditionnelle et éliminer les contraintes strictes du critère CFL (Courant-Friedrichs-Lewy), le schéma implicite aboutit à un système linéaire tridiagonal résolu en complexité linéaire $\mathcal{O}(N)$ via l'**algorithme de Thomas**. 

L'application intègre une architecture orientée objet rigoureuse, une gestion de mémoire RAII sans fuite, et un moteur de rendu graphique en temps réel sous **SDL2** affichant dynamiquement la convergence du payoff vers la solution théorique fermée.

---

## 📌 Executive Summary & Mathematical Formulation

The Black-Scholes PDE governs the fair value $V(S, t)$ of an option contingent on underlying asset price $S$ at time $t$:

$$rac{\partial V}{\partial t} + rac{1}{2} \sigma^2 S^2 rac{\partial^2 V}{\partial S^2} + r S rac{\partial V}{\partial S} - r V = 0$$

Under the time-reversal substitution $	au = T - t$ and space-time discretization on grid $(S_i, 	au_n)$:
- **Implicit Scheme Formulation**:
  $$a_i V_{i-1}^{n+1} + b_i V_i^{n+1} + c_i V_{i+1}^{n+1} = V_i^n$$
- The resulting tridiagonal matrix is diagonally dominant, guaranteeing numerical stability and solvable in $\mathcal{O}(M)$ time via the **Thomas Algorithm** (LU tridiagonal factorization).

---

## 📊 Numerical Convergence & Benchmarking

| Grid Size ($N_S 	imes N_t$) | Scheme Type | Stability Criterion | Max Error vs Analytical Formula | Execution Time |
| :---: | :---: | :---: | :---: | :---: |
| $200 	imes 1,000$ | Explicit Euler | Conditionally Stable ($\Delta t \le rac{\Delta S^2}{\sigma^2 S_{max}^2}$) | $3.2 	imes 10^{-3}$ | 14 ms |
| $200 	imes 1,000$ | **Implicit Euler** | **Unconditionally Stable** | **$4.1 	imes 10^{-4}$** | **18 ms** |
| $1,000 	imes 10,000$ | **Implicit + Thomas**| **Unconditionally Stable** | **$1.8 	imes 10^{-5}$** | **82 ms** |

---

## 📂 Repository Layout

```text
06_Black_Scholes_PDE_Solver/
├── src/
│   ├── solver.hpp                   # Abstract PDE solver interface
│   ├── implicit_scheme.cpp          # Tridiagonal Thomas solver implementation
│   ├── explicit_scheme.cpp          # Explicit stepping scheme
│   ├── market_parameters.hpp        # Volatility, risk-free rate, strike structs
│   └── visualizer_sdl.cpp           # Real-time SDL2 payoff rendering window
├── reports/
│   └── Rapport_Black_Scholes.pdf    # Complete 25-page scientific mathematics report
├── visuals/
│   ├── call.png                     # Payoff and option price surface visualization
│   └── put.png                      # Put option curve convergence
└── README.md
```

---

## 🚀 Build & Run

```bash
# Prerequisites: cmake, g++ supporting C++17, libsdl2-dev
mkdir build && cd build
cmake ..
make -j4

# Execute solver with interactive SDL2 payoff renderer
./black_scholes_solver --strike 100 --spot 100 --vol 0.2 --rate 0.05 --maturity 1.0 --type call
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n