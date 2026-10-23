# Airbnb NYC: Factor Analysis, Clustering & Spatial Data Science

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Multivariate%20Analysis-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: ENSIIE Applied Mathematics Specialization (2A ANDO Multivariate Analysis)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `Python`, `PCA`, `CCA`, `K-Means`, `Hierarchical Clustering`, `Matplotlib`, `Seaborn`  
> **Key Deliverables**: Full Multivariate Statistical Report, 2 Defense Slide Decks, Jupyter Notebooks



---

> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).

---

## 📌 Executive Summary & Mathematical Techniques

1. **Principal Component Analysis (PCA)**: Eigendecomposition of the empirical covariance matrix $\mathbf{\Sigma} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^T$, identifying that the top 3 principal components account for **68% of total variance**.
2. **Unsupervised Spatial Clustering**: Silhouette score optimization identifying 4 distinct property profiles across Manhattan, Brooklyn, Queens, Bronx, and Staten Island.

---

## 📂 Repository Layout

```text
08_Airbnb_NYC_Data_Analysis_ANDO/
├── notebooks/
│   └── airbnb_multivariate_analysis.ipynb # PCA, correlation circle & cluster profiling
├── reports/
│   └── Rapport_Analyse_Donnees_ANDO.pdf   # Complete multivariate statistical paper
├── presentations/
│   ├── Presentation_Partie_1.pdf          # PCA & exploratory factor analysis defense
│   └── Presentation_Partie_2.pdf          # Unsupervised clustering & spatial analysis
└── README.md
```

---

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de data science et d'analyse multivariée explore la dynamique des 48 000 hébergements **Airbnb à New York City**. 

L'objectif mathématique était d'extraire la structure latente sous-jacente aux variables tarifaires, spatiales et réputationnelles via :
- Une **Analyse en Composantes Principales (ACP / PCA)** décomposant l'inertie du nuage de points et projetant les logements sur les plans factoriels principaux.
- Une **Analyse Canonique des Corrélations (ACC / CCA)** reliant les variables géographiques aux indicateurs de rentabilité.
- Une segmentation non-supervisée croisant **K-Means** et **Classification Ascendante Hiérarchique (CAH / Ward)** pour caractériser les sous-marchés immobiliers new-yorkais.

Le dépôt comprend le mémoire d'analyse statistique complet et les deux présentations de soutenance.

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n
