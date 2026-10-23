# Breast Cancer Biostatistics: Survival Analysis & Penalized High-Dimensional GLMs

[![R](https://img.shields.io/badge/R-4.2+-276DC3?style=flat&logo=r&logoColor=white)](https://www.r-project.org/)
[![GLM](https://img.shields.io/badge/Statistics-Penalized%20GLM-brightgreen)](https://glmnet.stanford.edu/)
[![Survival](https://img.shields.io/badge/Biostatistics-Kaplan--Meier-blue)](https://cran.r-project.org/web/packages/survival/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: ENSIIE Applied Mathematics Specialization (2A MERR Biostatistics)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `R`, `Glmnet`, `Lasso`, `Elastic Net`, `Kaplan-Meier`, `ROC-AUC`, `Cross-Validation`  
> **Key Deliverables**: Complete Biostatistical Research Thesis, Reproducible R Scripts

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de biostatistique et de modélisation prédictive analyse la survie des patientes atteintes de cancer du sein à partir de la cohorte génomique internationale **METABRIC** (plus de 1 900 patientes et des centaines de variables cliniques et moléculaires). 

Face au fléau de la grande dimension ($p \gg n$), j'ai modélisé la survie globale et le statut vital en utilisant des **Modèles Linéaires Généralisés (GLM)** pénalisés :
- Régression **Lasso ($\ell_1$)** pour opérer une sélection parcimonieuse des biomarqueurs génétiques pertinents.
- Régression **Elastic Net** pour préserver les groupes de gènes fortement corrélés.
- Estimateurs non-paramétriques de **Kaplan-Meier** et tests du Log-Rank pour quantifier les écarts de survie entre sous-groupes moléculaires.

Le rapport de recherche complet détaille les coefficients sélectionnés, les courbes ROC et la validation croisée $K$-fold.

---

## 📌 Executive Summary & Methodology

### 1. High-Dimensional Penalized Regression
Survival classification was estimated via penalized binomial deviance optimization:

$$\min_{eta_0, oldsymbol{eta}} \left\{ -rac{1}{N} \ell(eta_0, oldsymbol{eta}) + \lambda \left( lpha \|oldsymbol{eta}\|_1 + rac{1 - lpha}{2} \|oldsymbol{eta}\|_2^2 ight) ight\}$$

Hyperparameters $\lambda$ and $lpha$ were calibrated using 10-fold cross-validation targeting minimal deviance ($\lambda_{\min}$) and sparse parsimony ($\lambda_{1	ext{se}}$).

---

## 📊 Key Results

- **Feature Sparsity**: Compressed feature space down to 14 statistically significant clinical and genetic covariates (including PR/ER receptor status and tumor grade).
- **Predictive Performance**: Achieved an out-of-sample **0.84 ROC-AUC** with calibrated 5-year survival discrimination.

---

## 📂 Repository Layout

```text
07_Breast_Cancer_Biostatistics_MERR/
├── src/
│   ├── survival_analysis.R          # Kaplan-Meier curves and Log-Rank tests
│   └── penalized_glm_modeling.R     # Lasso / Elastic Net cross-validation pipeline
├── reports/
│   └── Rapport_Cancer_Survie_MERR.pdf # Full biostatistical research paper
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n