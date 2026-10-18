# Canadian Retail Time Series: Statistical Modeling & SARIMA Forecasting

> **Cadre académique** : McMaster University (Canada) — STATS 4A03 (Time Series Analysis)  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Applied Statistics & Macroeconomic Time Series Forecasting`  
> **Stack Technique** : `R` `R Markdown` `SARIMA` `Box-Cox Transformations` `ACF / PACF` `Ljung-Box Tests` `Forecast Package`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet d'économétrie appliquée a été réalisé dans le cadre du cours de séries temporelles avancées **STATS 4A03** à **McMaster University** (Canada). L'étude porte sur la modélisation statistique et la prévision des séries chronologiques du commerce de détail canadien issues de **Statistique Canada**.

Les ventes au détail présentent une forte non-stationnarité caractérisée par une tendance structurelle à long terme couplée à une saisonnalité annuelle prononcée (pics d'achats du quatrième trimestre / fêtes de fin d'année). Le projet applique la méthodologie de **Box-Jenkins** pour identifier, estimer et valider des modèles de type **SARIMA** $(p, d, q) \times (P, D, Q)_s$.

---

## 🏗️ Structure du Répertoire

```text
11_McMaster_Canadian_Retail_Time_Series/
├── README.md                      # Présentation complète et diagnostic
├── reports/
│   └── Canadian_Retail_Time_Series_Report.pdf # Rapport académique complet du projet
├── src/
│   ├── Project.Rmd                # Code source R Markdown de l'analyse et des graphiques
│   └── Project.R                  # Script R autonome exécutant l'ensemble des modélisations
└── assignments/                   # Devoirs et travaux dirigés du cours STATS 4A03
    ├── Assignment_1.Rmd           # TD 1 : Processus stationnaires et fonctions d'autocovariance
    ├── Assignent2.Rmd             # TD 2 : Modèles AR(p) et MA(q)
    ├── Assignment 3/              # TD 3 : Propriétés ARMA et inversibilité
    ├── Assignment 4/              # TD 4 : Estimation des paramètres et critères AIC/BIC
    └── Assignment 5/              # TD 5 : Prévision et intervalles de confiance
```

---

## ⚙️ Démarche Méthodologique (Box-Jenkins)

1. **Stabilisation de la Variance & Stationnarisation** :
   - Transformation de puissance **Box-Cox** $(\lambda)$ pour stabiliser l'hétéroscédasticité.
   - Différenciation d'ordre 1 ($\nabla$) pour éliminer la tendance stochastique.
   - Différenciation saisonnière d'ordre 12 ($\nabla_{12}$) pour corriger la saisonnalité annuelle.
2. **Identification des Ordres $(p, d, q) \times (P, D, Q)_{12}$** :
   - Analyse visuelle de l'Autocorrélation Simple (ACF) et Partielle (PACF).
   - Sélection compétitive des ordres par minimisation de l'AICc.
3. **Diagnostic des Résidus** :
   - Test de blancheur de Ljung-Box confirmant l'absence d'autocorrélation résiduelle.
   - Test de normalité de Shapiro-Wilk et droite de Henry (Q-Q Plot).
4. **Prévision & Intervalles de Confiance** :
   - Extrapolation hors-échantillon à horizon 12 et 24 mois avec cônes d'incertitude à 80% et 95%.

---

## 🚀 Guide d'Exécution sous R

### Prérequis
```R
install.packages(c("forecast", "tseries", "ggplot2", "knitr", "rmarkdown"))
```

### Génération du Rapport PDF
```R
rmarkdown::render("src/Project.Rmd", output_format = "pdf_document")
```
Ou exécuter directement le script R :
```R
source("src/Project.R")
```

---

## 📄 Preuves & Rapports Inclus
- 📄 **Rapport d'Analyse Économétrique** : [`reports/Canadian_Retail_Time_Series_Report.pdf`](reports/Canadian_Retail_Time_Series_Report.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
