# Infinity Analytics: Financial Time Series Forecasting & Calibrated Scoring

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-Econometrics-blue)](https://www.statsmodels.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Gainde 2000 / Infinity Analytics (Engineering Internship 2025)  
> **Author**: Mohamed Nourou Dine CISSE — Quantitative Data Science Intern  
> **Core Stack**: `Python`, `SARIMAX`, `VAR`, `DLTS`, `Scikit-Learn`, `Model Calibration`, `ROC-AUC`  
> **Key Deliverables**: 2 Formal Research Reports, Final Defense Slide Deck, Calibrated Credit Scoring Pipeline

---

## 🇫🇷 Résumé Rapide en Français

Durant mon stage au sein d'**Infinity Analytics (Gainde 2000)**, j'ai développé deux moteurs analytiques critiques :
1. **Prévision Économétrique Multivariée de Séries Temporelles** : Modélisation des flux financiers et macroéconomiques via des approches univariées (**SARIMAX**) et multivariées vectorielles (**VAR** - Vector AutoRegression), combinées à des décompositions de tendances et saisonnalités (DLTS).
2. **Modèle de Scoring et de Risque de Crédit Calibré** : Conception d'un pipeline de scoring client évaluant la probabilité de défaut. L'accent a été mis sur la calibration rigoureuse des probabilités (Isotonic Regression & Platt Scaling), garantissant que le score émis reflète fidèlement le taux de risque empirique.

Ce dépôt réunit les deux rapports d'expertise rédigés en entreprise, la présentation de soutenance, les notebooks d'expérimentation et le code source de production.

---

## 📌 Executive Summary & Mathematical Methodology

### 1. Multivariate Time Series Forecasting (SARIMAX & VAR)
Modeling multivariate financial indicators requires capturing both autoregressive lagged relationships and cross-series Granger causality:

$$\mathbf{Y}_t = \mathbf{c} + \sum_{i=1}^p \mathbf{A}_i \mathbf{Y}_{t-i} + oldsymbol{\epsilon}_t, \quad oldsymbol{\epsilon}_t \sim \mathcal{N}(0, oldsymbol{\Sigma})$$

Stationarity was systematically verified via Augmented Dickey-Fuller (ADF) tests, and model lag order $p$ was determined through Akaike and Bayesian Information Criteria (AIC/BIC).

### 2. Calibrated Credit Risk Scoring
Default probability estimates $\hat{p} = \mathbb{P}(Y=1 \mid \mathbf{X})$ were calibrated against historical default frequencies using reliability curves (Brier score minimization):

$$\min_{\hat{p}} rac{1}{N} \sum_{i=1}^N (y_i - \hat{p}_i)^2$$

---

## 📂 Repository Layout

```text
04_Infinity_Analytics_Time_Series_ML/
├── notebooks/
│   ├── time_series_forecasting_var_sarimax.ipynb # Econometric stationarity, AIC grids & forecasting
│   └── credit_scoring_and_calibration.ipynb     # Feature engineering, classification & calibration
├── reports/
│   ├── Rapport_de_Stage.pdf                     # Comprehensive engineering internship report
│   └── Rapport_Use_Case_7_Scoring.pdf           # Technical paper on credit scoring calibration
├── presentations/
│   └── Presentation_de_Stage.pdf                # Executive corporate defense presentation
├── models_and_data/                             # Anonymized financial series and test metrics
└── README.md
```

---

## 📊 Key Results

- **Stationarity & Invertibility**: Attained stable vector autoregression with eigenvalue moduli strictly inside the unit circle.
- **Probability Calibration**: Brier score improved by **18.4%** post-isotonic calibration over raw tree-based output probabilities.
- **Discriminative Power**: Achieved **0.86 ROC-AUC** on out-of-time credit default validation datasets.

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n