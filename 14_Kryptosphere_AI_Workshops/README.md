# Kryptosphere AI Workshops: Hands-On Machine Learning & Data Science Training Suite

> **Cadre associatif & pédagogique** : KRYPTOSPHERE (Association Étudiante d'Innovation Technologique & IA)  
> **Formateur & Concepteur** : Mohamed Nourou Dine CISSE — Responsable Formations IA  
> **Domaine** : `Applied Data Science, Machine Learning Pedagogy & Technical Training`  
> **Stack Technique** : `Python` `Jupyter Notebook` `Pandas` `Scikit-learn` `Seaborn` `Time Series` `Clustering`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce dépôt regroupe l'ensemble du matériel pédagogique (supports de cours, slides PowerPoint/PDF, jeux de données d'exercice et notebooks interactifs avec solutions) conçu et dispensé lors des **formations en Intelligence Artificielle et Data Science de l'association KRYPTOSPHERE**.

Destiné aux étudiants ingénieurs débutants et intermédiaires, le cursus privilégie une approche par la pratique (*learning by doing*) à travers 4 ateliers modulaires :
1. **Atelier 1 — Manipulation & Visualisation de Données** : Exploration du jeu de données des joueurs FIFA (`fifa_players.csv`), indexation Pandas, traitement des valeurs nulles et visualisations Seaborn / Matplotlib.
2. **Atelier 2 — Prétraitement & Évaluation de Modèles** : Encodage (*One-Hot*, *Label Encoding*), normalisation, division train/test sans fuite de données (*data leakage*), matrices de confusion, compromis biais-variance et métriques de classification/régression.
3. **Atelier 3 — Apprentissage Non-Supervisé & Clustering** : Algorithme des K-Moyennes (*K-Means*), méthode du coude (*Elbow Method*), indice silhouette et projection PCA.
4. **Atelier 4 — Introduction aux Séries Temporelles** : Analyse de la fréquentation aérienne historique (`AirPassengers.csv`), décomposition de tendance et saisonnalité.

---

## 🏗️ Structure du Répertoire

```text
14_Kryptosphere_AI_Workshops/
├── README.md                      # Présentation générale du cycle de formation
├── presentations/                 # Diaporama de cours dispensés (PowerPoint & PDF)
│   ├── Formation_Evaluation_Modeles_ML.pdf / .pptx  # Support complet Atelier 2
│   └── Formation_Clustering.pdf / .pptx            # Support complet Atelier 3
└── workshops/                     # Dossiers d'exercices pratiques par atelier
    ├── 01_data_manipulation_viz/
    │   ├── data_manip_viz.ipynb   # Notebook pas-à-pas de manipulation Pandas & Seaborn
    │   └── fifa_players.csv       # Dataset d'apprentissage FIFA
    ├── 02_preprocessing_evaluation/
    │   ├── Preprocessing_ML.ipynb # Notebook de nettoyage, feature engineering et validation croisée
    │   ├── train.csv              # Jeu d'entraînement
    │   └── test.csv               # Jeu de test
    ├── 03_clustering/
    │   └── Clustering.ipynb       # Notebook d'implémentation K-Means et visualisation
    └── 04_time_series/
        ├── series_temporelles.ipynb # Notebook d'initiation aux séries temporelles
        └── AirPassengers.csv      # Dataset classique AirPassengers
```

---

## 🎯 Objectifs Pédagogiques & Compétences Transmises

- **Bonnes pratiques en ingénierie de données** : Structuration de pipelines Scikit-learn reproductibles.
- **Rigueur méthodologique** : Choix des métriques adaptées aux déséquilibres de classes (F1-score vs Accuracy).
- **Communication technique** : Capacité à vulgariser les concepts mathématiques sous-jacents auprès d'un public technique.

---

## 🚀 Guide d'Exécution pour les Participants

```bash
# Installation de l'environnement Python d'atelier
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Démarrage de Jupyter
jupyter notebook workshops/
```

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
