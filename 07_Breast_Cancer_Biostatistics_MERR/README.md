# Breast Cancer Biostatistics: Survival Analysis & Logistic Modeling (METABRIC Cohort)

> **Cadre académique** : ENSIIE — Module MERR (Modèles Statistiques & Épidémiologie)  
> **Auteurs** : Mohamed Nourou Dine CISSE & Mohammed Yahya DAMI  
> **Domaine** : `Biostatistics, Survival Analysis & Clinical Outcome Prediction`  
> **Stack Technique** : `R` `R Markdown` `Survminer` `Survival` `Modèles de Cox` `Kaplan-Meier` `Régression Logistique` `Odds Ratios`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet de biostatistique applique les méthodes rigoureuses de l'analyse de survie et des modèles linéaires généralisés (famille binomiale) à la cohorte clinique et génomique de référence du cancer du sein **METABRIC** (publiée dans la revue *Nature*, 2012 : *The genomic and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups*).

L'analyse poursuit deux objectifs cliniques majeurs :
1. **Identifier les facteurs pronostiques influençant la survie globale** des patientes via des estimateurs non-paramétriques (Kaplan-Meier), des tests du Log-Rank et des régressions à risques proportionnels de Cox.
2. **Prédire le risque de récidive ou de décès à horizon fixé** à l'aide d'un modèle de régression logistique multivarié avec analyse des rapports de cotes (*Odds Ratios*), de la déviance résiduelle et de la courbe ROC.

---

## 🏗️ Structure du Répertoire

```text
07_Breast_Cancer_Biostatistics_MERR/
├── README.md                          # Présentation détaillée et synthèse clinique
├── reports/
│   ├── Rapport_Cancer_Survie_MERR.pdf # Rapport final complet de biostatistique
│   └── Reference_Nature_2012.pdf      # Article fondateur METABRIC (Curtis et al., Nature 2012)
└── src/
    ├── BINOMIAL_12_CISSE_DAMI.Rmd     # Script R Markdown complet (1 335 lignes de code & analyses)
    └── mrr_bio.Rdata                  # Jeu de données clinico-génomique RData
```

---

## ⚙️ Méthodologie Statistique Développée

### 1. Analyse de Survie (Time-to-Event)
- **Estimateur de Kaplan-Meier** : Tracé des courbes de survie stratifiées selon les sous-types moléculaires (ER+, HER2+, Triple Négatif) et le statut ganglionnaire.
- **Test du Log-Rank** : Comparaison formelle des distributions de survie entre sous-groupes cliniques.
- **Modèle de Cox Semi-Paramétrique** :
  - Estimation des Hazard Ratios (HR) avec intervalles de confiance à 95%.
  - Vérification de l'hypothèse de proportionnalité des risques par les résidus de Schoenfeld.

### 2. Régression Logistique (Famille Binomiale)
- Sélection des variables explicatives par minimisation du critère AIC (stratégie stepwise / backward).
- Interprétation des Odds Ratios ajustés pour les biomarqueurs et grades histologiques.
- Évaluation de la capacité discriminante par l'indice de concordance et la courbe ROC (AUC).

---

## 🚀 Reproduction des Résultats sous R

### Prérequis
Installer les bibliothèques R nécessaires :
```R
install.packages(c("survival", "survminer", "ggplot2", "dplyr", "knitr", "rmarkdown", "pROC"))
```

### Génération du Rapport
Sous RStudio ou en ligne de commande :
```R
rmarkdown::render("src/BINOMIAL_12_CISSE_DAMI.Rmd", output_format = "pdf_document")
```

---

## 📄 Preuves & Publications Incluses
- 📄 **Rapport de Biostatistique** : [`reports/Rapport_Cancer_Survie_MERR.pdf`](reports/Rapport_Cancer_Survie_MERR.pdf)
- 📄 **Publication de Référence Nature 2012** : [`reports/Reference_Nature_2012.pdf`](reports/Reference_Nature_2012.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
