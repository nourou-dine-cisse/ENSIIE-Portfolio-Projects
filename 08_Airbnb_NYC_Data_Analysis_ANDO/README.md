# Airbnb NYC Data Analysis: Factor Analysis, PCA, CCA & Unsupervised Clustering

> **Cadre académique** : ENSIIE — Module ANDO (Analyse Numérique des Données)  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Multivariate Statistics, Data Mining & Unsupervised Learning`  
> **Stack Technique** : `Python` `Pandas` `Scikit-learn` `PCA` `CCA (Analyse Canonique)` `K-Means` `CAH (Clustering Hiérarchique)` `Seaborn`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet d'analyse multivariée explore le jeu de données **New York City Airbnb 2019** (environ 49 000 hébergements, caractéristiques tarifaires, géographiques et d'avis clients). L'objectif est de dégager les structures latentes gouvernant le marché locatif new-yorkais à l'aide des outils fondamentaux de la statistique factorielle et du machine learning non-supervisé.

L'étude s'articule autour de quatre axes majeurs :
1. **Nettoyage et analyse exploratoire** : Traitement des valeurs aberrantes de prix, log-transformation, analyse spatiale par arrondissement (Manhattan, Brooklyn, Queens, etc.).
2. **Analyse en Composantes Principales (ACP / PCA)** : Réduction de dimension, cercle des corrélations, valeurs propres et interprétation des axes d'inertie.
3. **Analyse Canonique des Corrélations (ACC / CCA)** : Étude des relations linéaires conjointes entre deux groupes de variables (attributs du logement vs indicateurs de réputation et disponibilité).
4. **Clustering & Segmentation d'hôtes** : Regroupement par K-Means et Classification Ascendante Hiérarchique (dendrogramme, méthode du coude et score silhouette).

---

## 🏗️ Structure du Répertoire

```text
08_Airbnb_NYC_Data_Analysis_ANDO/
├── README.md                      # Documentation complète du projet
├── data/
│   └── AB_NYC_2019.csv            # Dataset Airbnb NYC 2019 (Kaggle)
├── notebooks/
│   ├── projet.ipynb               # Nettoyage, préparation des données et tests d'hypothèses
│   ├── PCA.ipynb                  # Analyse en Composantes Principales (cercles de corrélation, variance expliquée)
│   ├── CCA.ipynb                  # Analyse Canonique des Corrélations entre blocs de variables
│   ├── clustering.ipynb           # K-Means, CAH, segmentation des profils d'hébergement
│   └── ANDO.ipynb                 # Synthèse générale et analyse spatiale
├── presentations/
│   ├── Presentation_Partie_1.pdf  # Soutenance intermédiaire (statistiques descriptives & ACP)
│   └── Presentation_Partie_2.pdf  # Soutenance finale (clustering, CCA et synthèse)
└── reports/
    ├── Rapport_Analyse_Donnees_ANDO.pdf # Rapport d'analyse complet
    └── rapport_source.tex         # Code source LaTeX du rapport
```

---

## ⚙️ Méthodes & Résultats Clés

- **ACP** : Le premier plan factoriel capture l'opposition entre les logements à forte capacité/prix élevé situés à Manhattan et les hébergements économiques plus excentrés.
- **Analyse Canonique** : Révèle une corrélation canonique significative entre la disponibilité annuelle et la dynamique de rotation des commentaires clients.
- **Clustering** : Identification de 3 profils types d'hôtes :
  1. Les logements occasionnels ou individuels à faible rotation.
  2. Les hébergements touristiques à forte attractivité centrale.
  3. Les gestionnaires professionnels multi-propriétés à taux d'occupation optimisé.

---

## 🚀 Guide d'Exécution

```bash
# Installation des dépendances
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Lancement des notebooks
jupyter notebook notebooks/
```

---

## 📄 Preuves & Rapports Inclus
- 📄 **Rapport d'Analyse Numérique** : [`reports/Rapport_Analyse_Donnees_ANDO.pdf`](reports/Rapport_Analyse_Donnees_ANDO.pdf)
- 📊 **Présentations de Soutenance** : [`presentations/Presentation_Partie_1.pdf`](presentations/Presentation_Partie_1.pdf) & [`presentations/Presentation_Partie_2.pdf`](presentations/Presentation_Partie_2.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
