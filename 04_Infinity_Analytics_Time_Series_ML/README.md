# Infinity Analytics: Financial Time Series Forecasting & Credit Scoring ML

> **Cadre professionnel** : Stage de Fin d'Année — Infinity Capital / Infinity Analytics (2025)  
> **Formation** : ENSIIE — Ingénierie Mathématique & Data Science  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Quantitative Finance, Time Series Analysis & Machine Learning`  
> **Stack Technique** : `Python` `Statsmodels` `Scikit-learn` `SARIMA / SARIMAX` `VAR` `Pandas` `Scoring ML`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet rassemble les travaux de modélisation statistique et de machine learning menés lors de mon stage chez **Infinity Analytics**. Les problématiques traitées couvraient deux volets complémentaires :
1. **Prévision de séries temporelles financières** : Analyse de stationnarité (ADF, KPSS), identification des ordres AR/MA via ACF/PACF, modélisation par processus **SARIMA**, intégration de variables exogènes avec **SARIMAX**, et modélisation vectorielle autorégressive (**VAR**) multivariée.
2. **Modèles de scoring et risque de crédit** :
   - **Use Case 2** : Analyse comportementale et prédiction des retards de paiement.
   - **Use Case 7** : Modèle de scoring calibré avec analyse de la courbe de calibration (`calibration_curve`), matrice de corrélation et poids d'importance des features.

---

## 🏗️ Structure du Répertoire

```text
04_Infinity_Analytics_Time_Series_ML/
├── README.md                      # Présentation complète et synthèse technique
├── models_and_data/
│   ├── BAQ.csv                    # Dataset historique d'activité financière
│   ├── API_data_sample.csv        # Échantillon de données d'API
│   └── use_case_7_calib_modele.pkl# Modèle de scoring calibré exporté (Pickle, 21 Mo)
├── notebooks/
│   ├── SARIMA.ipynb               # Modélisation univariée saisonnière (ACF/PACF, diagnostic résidus)
│   ├── SARIMAX.ipynb              # Modélisation avec variables explicatives exogènes
│   ├── VAR.ipynb                  # Vector AutoRegression multivariée
│   ├── usecase_2.ipynb            # Pipeline d'analyse et modélisation Use Case 2
│   └── usecase_7.ipynb            # Pipeline complet de scoring et calibration Use Case 7
├── reports/
│   ├── Rapport_de_Stage.pdf       # Rapport de stage complet (6,4 Mo)
│   ├── Rapport_Use_Case_2.pdf     # Rapport détaillé Use Case 2
│   ├── Rapport_Use_Case_7_Scoring.pdf # Rapport détaillé modèle de scoring Use Case 7
│   ├── Modele_de_Donnees.pdf      # Spécification du modèle de données
│   ├── Integration_ML.pdf         # Architecture d'intégration logicielle
│   ├── Use_Cases_ML_IA.pdf        # Panorama des cas d'usage ML/IA
│   └── figures/                   # Graphiques diagnostiques (décomposition, calibration, etc.)
└── presentations/
    └── Presentation_de_Stage.pdf  # Support de soutenance de stage
```

---

## ⚙️ Méthodologie & Diagnostics

### 1. Séries Temporelles (`SARIMA`, `SARIMAX`, `VAR`)
- Décomposition additive et multiplicative (tendance, saisonnalité, bruit résiduel).
- Tests formels de racine unitaire (Augmented Dickey-Fuller) et différentiation pour stationnarisation.
- Sélection de modèles par critères d'information (AIC / BIC) et tests de blancheur des résidus (Ljung-Box).

### 2. Scoring & Calibration (`usecase_7.ipynb`)
- Prétraitement et encodage des variables socio-démographiques et transactionnelles.
- Calibration des probabilités prédites (Brier score, calibration curve) pour assurer que les scores reflètent de véritables probabilités de défaut.
- Export et traçabilité du modèle final sérialisé (`use_case_7_calib_modele.pkl`).

---

## 🚀 Guide d'Exécution

```bash
# Installation de l'environnement scientifique
pip install pandas numpy statsmodels scikit-learn matplotlib seaborn jupyter

# Lancement des notebooks
jupyter notebook notebooks/
```

---

## 📄 Preuves & Rapports
- 📄 **Rapport Général de Stage** : [`reports/Rapport_de_Stage.pdf`](reports/Rapport_de_Stage.pdf)
- 📄 **Rapport Scoring Use Case 7** : [`reports/Rapport_Use_Case_7_Scoring.pdf`](reports/Rapport_Use_Case_7_Scoring.pdf)
- 📊 **Présentation de Stage** : [`presentations/Presentation_de_Stage.pdf`](presentations/Presentation_de_Stage.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
