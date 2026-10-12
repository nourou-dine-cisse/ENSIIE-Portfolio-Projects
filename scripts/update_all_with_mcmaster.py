import os
import json
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_ENSIIE = os.path.abspath(".")
ALL_PROJ_DIR = os.path.join(BASE_ENSIIE, "All projects")
CATALOG_PATH = os.path.join(ALL_PROJ_DIR, "projects_catalog.json")

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Define McMaster projects to append
mcmaster_projects = [
    {
        "id": "17_mcmaster_nash_dqn",
        "folder": "17_McMaster_Nash_DQN_MultiAgent_Trading",
        "title_fr": "Nash-DQN : Deep Q-Learning pour Équilibres de Nash en Trading Multi-Agents",
        "title_en": "Nash-DQN: Deep Q-Learning for Nash Equilibria in Multi-Agent Optimal Execution",
        "category": "Quantitative Finance & Reinforcement Learning",
        "institution": "McMaster University (MATH 4FM3)",
        "year": "2026",
        "role": "Quantitative Researcher / RL Engineer",
        "technologies": ["Python", "PyTorch", "Deep Q-Learning (DQN)", "Multi-Agent RL", "Stochastic Games", "Optimal Execution", "Mouvement Brownien"],
        "keywords": ["reinforcement learning", "dqn", "multi-agent", "trading", "finance quantitative", "nash", "optimal execution", "pytorch", "mcmaster"],
        "pitch_fr": "Implémentation sous PyTorch d'un environnement de jeu stochastique à N agents (Casgrain, Ning & Jaimungal, 2022) et entraînement d'architectures Deep Q-Network (Nash-DQN) pour converger vers l'équilibre de Nash en exécution optimale d'ordres.",
        "pitch_en": "Engineered an N-agent stochastic market simulator and trained Deep Q-Networks (Nash-DQN) converging to Nash equilibrium for multi-agent optimal liquidation (Casgrain, Ning & Jaimungal, 2022).",
        "star_bullet_points_fr": [
            "Conception d'un simulateur de marché stochastique sous forme de jeu différentiel à N agents avec impact de marché temporaire et permanent.",
            "Développement d'un algorithme Nash-DQN avec replay buffer priorisé et réseaux cible pour l'apprentissage de politiques de trading compétitives.",
            "Rédaction d'une thèse de recherche mathématique de 34 pages accompagnée de visualisations des trajectoires browniennes et récompenses cumulées."
        ],
        "star_bullet_points_en": [
            "Architected an N-agent stochastic differential game environment modeling temporary and permanent market price impact.",
            "Trained a Nash-DQN multi-agent reinforcement learning policy with experience replay to discover competitive Nash equilibrium strategies.",
            "Authored a comprehensive 34-page quantitative research paper with extensive trajectory and convergence reward diagnostics."
        ],
        "reports": ["reports/Rapport_Nash_DQN_Optimal_Trading.pdf", "reports/Project_Roadmap.pdf"],
        "presentations": []
    },
    {
        "id": "18_mcmaster_financial_sentiment",
        "folder": "18_McMaster_Financial_News_Sentiment_BiLSTM",
        "title_fr": "Analyse de Sentiment de Titres Financiers : ML Classique vs BiLSTM",
        "title_en": "Financial News Sentiment Classification: Classical ML vs Bidirectional LSTM",
        "category": "NLP & Financial Deep Learning",
        "institution": "McMaster University (DATASCI 3ML3)",
        "year": "2026",
        "role": "NLP & Machine Learning Engineer",
        "technologies": ["Python", "PyTorch", "BiLSTM", "TF-IDF", "Scikit-Learn", "NLP", "Financial Sentiment", "Cross-Validation"],
        "keywords": ["sentiment", "finance", "nlp", "bilstm", "lstm", "deep learning", "pytorch", "classification", "mcmaster"],
        "pitch_fr": "Benchmark comparatif de modèles de classification de sentiments sur 9 549 titres d'actualité financière (Financial PhraseBank) comparant modèles classiques (SVM, Random Forest) et réseaux neuronaux récurrents bidirectionnels (BiLSTM).",
        "pitch_en": "Comparative benchmark for 3-class sentiment classification across 9,549 financial headlines comparing classical machine learning with Bidirectional LSTMs.",
        "star_bullet_points_fr": [
            "Traitement et vectorisation d'un corpus de 9 549 titres financiers avec analyse lexicale et gestion du déséquilibre de classes.",
            "Implémentation et optimisation d'une architecture neuronale Bidirectional LSTM sous PyTorch surpassant les baselines classiques.",
            "Rédaction d'un rapport de recherche académique de 11 pages détaillant les courbes d'apprentissage, F1-scores et analyses d'erreurs."
        ],
        "star_bullet_points_en": [
            "Curated and preprocessed 9,549 financial news headlines addressing class imbalance and specialized financial vocabularies.",
            "Implemented and trained a Bidirectional LSTM neural network in PyTorch achieving superior accuracy and macro F1 over classical baselines.",
            "Authored an 11-page comparative research paper detailing convergence dynamics, confusion matrices, and ablation findings."
        ],
        "reports": ["reports/Financial_News_Sentiment_Classification_Report.pdf", "reports/Sujet_FinalProject.pdf"],
        "presentations": []
    },
    {
        "id": "19_mcmaster_canadian_retail_ts",
        "folder": "19_McMaster_Canadian_Retail_Time_Series",
        "title_fr": "Prévision de la Demande Saisonnière dans le Commerce de Détail Canadien",
        "title_en": "Seasonal Demand Forecasting in Canadian Retail Trade (1992–2019)",
        "category": "Time Series & Applied Econometrics",
        "institution": "McMaster University (STATS 4A03)",
        "year": "2026",
        "role": "Time Series Analyst",
        "technologies": ["R", "RMarkdown", "SARIMA", "Holt-Winters", "Décomposition STL", "Tests de Stationnarité (ADF/KPSS)", "Validation Croisée"],
        "keywords": ["time series", "series temporelles", "sarima", "r", "retail", "prevision", "forecast", "holt winters", "mcmaster"],
        "pitch_fr": "Modélisation économétrique et prévision de séries temporelles sur 27 ans de ventes mensuelles du commerce de détail canadien (Statistique Canada) par décomposition STL, lissage exponentiel Holt-Winters et modèles SARIMA multiplicatifs.",
        "pitch_en": "Econometric modeling and 27-year time series forecasting of monthly Canadian retail sales data using STL decomposition, Holt-Winters exponential smoothing, and SARIMA models.",
        "star_bullet_points_fr": [
            "Analyse exploratoire et tests statistiques de stationnarité (ADF, KPSS) sur 27 années de séries mensuelles de consommation.",
            "Identification et estimation de modèles SARIMA multiplicatifs avec validation rigoureuse des résidus (Ljung-Box, normalité).",
            "Production d'un rapport de prévision de 12 pages compilé sous RMarkdown avec intervalles de confiance prospectifs."
        ],
        "star_bullet_points_en": [
            "Conducted stationarity diagnostics (ADF, KPSS tests) and seasonal decomposition on a 27-year macroeconomic time series.",
            "Identified and tuned multiplicative SARIMA models validating residual white noise assumptions via Ljung-Box tests.",
            "Delivered a reproducible 12-page RMarkdown technical forecasting paper providing multi-step forward horizon projections."
        ],
        "reports": ["reports/Canadian_Retail_Time_Series_Forecasting_Report.pdf"],
        "presentations": []
    },
    {
        "id": "20_mcmaster_vqa",
        "folder": "20_McMaster_Visual_Question_Answering_VQA",
        "title_fr": "Visual Question Answering (VQA) : Fusion Multimodale Vision & Langage",
        "title_en": "Visual Question Answering (VQA): Multimodal Vision-Language Deep Learning",
        "category": "Multimodal Deep Learning & Computer Vision",
        "institution": "McMaster University (MECHENG 4AI3)",
        "year": "2026",
        "role": "Multimodal Deep Learning Engineer",
        "technologies": ["Python", "PyTorch", "Torchvision", "CNN (ResNet)", "LSTM", "Multimodal Fusion", "VQA v2.0 Dataset", "Streamlit"],
        "keywords": ["vqa", "multimodal", "computer vision", "nlp", "pytorch", "deep learning", "resnet", "lstm", "fusion", "mcmaster"],
        "pitch_fr": "Système de Question-Réponse Visuelle (VQA) entraîné sur le dataset VQA v2.0 associant extraction de caractéristiques visuelles par CNN (ResNet), encodage linguistique par LSTM et module de fusion multimodale.",
        "pitch_en": "Multimodal Visual Question Answering architecture on VQA v2.0 dataset fusing deep convolutional image features (ResNet) with LSTM question embeddings.",
        "star_bullet_points_fr": [
            "Pipeline d'ingestion et d'alignement multimodal image-texte sur le benchmark VQA v2.0.",
            "Conception d'une architecture de fusion multimodale (produit tensoriel / concaténation dense) pour la génération de réponses visuelles.",
            "Déploiement d'une application de démonstration interactive avec roadmap de développement produit."
        ],
        "star_bullet_points_en": [
            "Engineered multimodal data preprocessing and spatial visual alignment pipeline on the standard VQA v2.0 dataset.",
            "Implemented multimodal fusion architectures combining deep visual representations with recurrent sentence encodings.",
            "Developed an interactive web application demo and structured sprint engineering roadmap."
        ],
        "reports": ["reports/VQA_Project_Roadmap.pdf"],
        "presentations": []
    },
    {
        "id": "21_mcmaster_glm",
        "folder": "21_McMaster_Generalized_Linear_Models",
        "title_fr": "Modèles Linéaires Généralisés : Régressions Poisson, Gamma & Binomiales",
        "title_en": "Applied Generalized Linear Models: Poisson, Gamma, and Logistic Regressions",
        "category": "Applied Statistics & GLM",
        "institution": "McMaster University (STATS 4GLM)",
        "year": "2026",
        "role": "Applied Statistician",
        "technologies": ["R", "RMarkdown", "GLM", "Régression Poisson", "Régression Gamma", "Régression Logistique", "Analyse de Déviance", "Surdispersion"],
        "keywords": ["glm", "statistiques", "poisson", "gamma", "r", "econometrie", "deviance", "mcmaster"],
        "pitch_fr": "Suite d'études statistiques approfondies appliquant la théorie des modèles linéaires généralisés (famille exponentielle, fonctions de lien, quasi-vraisemblance) sur des problématiques réelles d'assurance et d'épidémiologie.",
        "pitch_en": "Comprehensive statistical modeling assignments applying Generalized Linear Model theory (exponential dispersion family, link functions, quasi-likelihood) to actuarial and empirical datasets.",
        "star_bullet_points_fr": [
            "Ajustement de modèles GLM Poisson et quasi-Poisson pour données de comptage avec diagnostic de surdispersion.",
            "Modélisation de données continues positives asymétriques via GLM Gamma et sélection de variables par analyse de déviance.",
            "Production de 5 rapports d'analyse sous RMarkdown démontrant une maîtrise rigoureuse de l'inférence statistique."
        ],
        "star_bullet_points_en": [
            "Fitted Poisson and Quasi-Poisson GLMs for count data with diagnostics for overdispersion and zero inflation.",
            "Modeled right-skewed continuous responses using Gamma GLMs with deviance goodness-of-fit hypothesis testing.",
            "Authored 5 comprehensive reproducible RMarkdown statistical reports demonstrating deep mastery of statistical inference."
        ],
        "reports": [],
        "presentations": []
    }
]

# Avoid duplicating if re-run
existing_ids = {p["id"] for p in catalog}
for mp in mcmaster_projects:
    if mp["id"] not in existing_ids:
        catalog.append(mp)

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)
print(f"[OK] projects_catalog.json updated with {len(catalog)} total projects.")

# Generate README.md for new McMaster projects
for p in mcmaster_projects:
    p_dir = os.path.join(ALL_PROJ_DIR, p["folder"])
    readme_path = os.path.join(p_dir, "README.md")
    
    rep_md = ""
    if p["reports"]:
        rep_md = "\n".join([f"- 📄 **Rapport technique** : [{os.path.basename(r)}]({r})" for r in p["reports"]])
    else:
        rep_md = "- *Documentation technique & code source intégrés dans le dépôt.*"

    pres_md = ""
    if p["presentations"]:
        pres_md = "\n".join([f"- 📊 **Présentation / Soutenance** : [{os.path.basename(pr)}]({pr})" for pr in p["presentations"]])
    else:
        pres_md = "- *Pas de présentation diapositive distincte pour ce projet.*"

    tech_badges = " ".join([f"`{t}`" for t in p["technologies"]])
    star_bullets = "\n".join([f"- {b}" for b in p["star_bullet_points_fr"]])
    star_bullets_en = "\n".join([f"- {b}" for b in p["star_bullet_points_en"]])

    readme_content = f"""# {p['title_fr']}

> **Institution / Contexte** : {p['institution']} ({p['year']})  
> **Rôle** : {p['role']}  
> **Domaine** : `{p['category']}`  
> **Technologies** : {tech_badges}

---

## 📌 Présentation du Projet (Executive Summary)

**En français :**  
{p['pitch_fr']}

**In English :**  
{p['pitch_en']}

---

## 🏆 Réalisations Clés & Résultats (STAR Format)

### Version Française (CV & Entretiens) :
{star_bullets}

### English Version (Resume & Interviews) :
{star_bullets_en}

---

## 📂 Livrables Disponibles dans ce Répertoire

### 📄 Rapports & Documentation :
{rep_md}

### 📊 Présentations & Soutenances :
{pres_md}

---

## 🛠️ Stack Technique & Compétences Clés
{tech_badges}

---

## 🚀 À propos de l'Auteur
- **Mohamed Nourou Dine CISSE**
- Élève-ingénieur en Mathématiques Appliquées & Intelligence Artificielle à l'**ENSIIE** (France)
- Semestre d'échange à l'**Université McMaster** (Ontario, Canada)
- **Email** : [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com)
- **GitHub** : [@nourou-dine-mahy](https://github.com/nourou-dine-mahy)
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"  [README] Generated {p['folder']}/README.md")

# Update Master README.md / PORTFOLIO.md
portfolio_path = os.path.join(ALL_PROJ_DIR, "README.md")
portfolio_md = """# 🚀 Portfolio de Projets — Mohamed Nourou Dine CISSE
### Étudiant-Ingénieur en Mathématiques Appliquées & Intelligence Artificielle (ENSIIE & McMaster University)
**Recherche active : Stage de Fin d'Études (PFE) / Stage 6 mois en Intelligence Artificielle, Data Science, Data Engineering ou Finance Quantitative.**

[![GitHub](https://img.shields.io/badge/GitHub-nourou--dine--mahy-181717?logo=github)](https://github.com/nourou-dine-mahy)
[![Email](https://img.shields.io/badge/Email-mouhamed.nouroudine.cisse%40gmail.com-EA4335?logo=gmail)](mailto:mouhamed.nouroudine.cisse@gmail.com)
[![Status](https://img.shields.io/badge/Disponible-PFE%202026-brightgreen)]()

---

## 🌟 Présentation & Points Forts

Bienvenue sur le portfolio centralisé de mes projets d'ingénierie, de recherche appliquée et d'entrepreneuriat.  
Ce recueil regroupe l'ensemble des **21 projets majeurs** menés à l'**ENSIIE**, à l'**Université McMaster (Canada)**, en entreprise (**Publicis Groupe**, **Infinity Analytics / Gainde 2000**) et dans le cadre de concours d'innovation (**1er prix Challenge Entreprendre**).

Chaque projet est fourni avec son **code source propre**, ses **rapports d'expertise**, ses **supports de soutenance** et des **fiches récapitulatives STAR** prêtes pour les recruteurs.

---

## 📑 Sommaire des Projets par Domaine d'Expertise

### 1. 🤖 Intelligence Artificielle, RAG & LLMs
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**01. Plateforme Spielberg (Publicis)**](./01_Spielberg_AI_Data_Platform) | Stage 2A/3A Publicis / Prodigious | FastAPI, RAG, Chunking, Vector DB, Async | [📄 Rapport (54 p.)](./01_Spielberg_AI_Data_Platform/reports/Rapport_de_Stage_Spielberg_2026.pdf) • [📊 Soutenance (22 pl.)](./01_Spielberg_AI_Data_Platform/presentations/Soutenance_Spielberg.pdf) |
| [**05. NLP & Représentations Sémantiques**](./05_NLP_Semantic_Representations_NER) | Master IA (M2IA) | PyTorch, Transformers, FastText, Word2Vec, BiLSTM-CNN | [📄 Rapport Recherche](./05_NLP_Semantic_Representations_NER/reports/Report_CISSE_DIOP.pdf) • [📄 Rapport Embeddings](./05_NLP_Semantic_Representations_NER/reports/Rapport_TP_Embeddings.pdf) |
| [**18. NLP & Sentiment Financier BiLSTM**](./18_McMaster_Financial_News_Sentiment_BiLSTM) | **McMaster University** | PyTorch, BiLSTM, TF-IDF, Sentiment Analysis | [📄 Rapport Recherche (11 p.)](./18_McMaster_Financial_News_Sentiment_BiLSTM/reports/Financial_News_Sentiment_Classification_Report.pdf) |
| [**20. Visual Question Answering (VQA)**](./20_McMaster_Visual_Question_Answering_VQA) | **McMaster University** | PyTorch, CNN ResNet, LSTM, Fusion Multimodale | [📄 Roadmap & Spécifications](./20_McMaster_Visual_Question_Answering_VQA/reports/VQA_Project_Roadmap.pdf) |
| [**13. Ateliers & Formations IA Kryptosphere**](./13_Kryptosphere_AI_Workshops) | Assos Kryptosphere IA | Scikit-Learn, Pandas, Clustering, Time Series | [📊 Slides Modèles ML](./13_Kryptosphere_AI_Workshops/presentations/Formation_Evaluation_Modeles_ML.pdf) • [📊 Slides Clustering](./13_Kryptosphere_AI_Workshops/presentations/Formation_Clustering.pdf) |
| [**15. Data Readiness & Visages**](./15_Face_Attributes_Data_Readiness) | 3A ENSIIE | PyTorch, Data Readiness, Matrices de Confusion | 💻 Code PyTorch, visualisations de biais |

---

### 2. 💹 Finance Quantitative, Reinforcement Learning & Calcul Scientifique
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**17. Nash-DQN Multi-Agent Optimal Trading**](./17_McMaster_Nash_DQN_MultiAgent_Trading) | **McMaster University (MATH 4FM3)** | PyTorch, Multi-Agent RL, Deep Q-Learning, Mouvement Brownien | [📄 Thèse Quantitative (34 p.)](./17_McMaster_Nash_DQN_MultiAgent_Trading/reports/Rapport_Nash_DQN_Optimal_Trading.pdf) • 📈 Graphiques de convergence |
| [**06. Solveur EDP Black-Scholes C++ & SDL2**](./06_Black_Scholes_PDE_Solver) | 2A PRAV | C++17, Schéma Implicite, Différences Finies, SDL2 | [📄 Rapport Black-Scholes](./06_Black_Scholes_PDE_Solver/reports/Rapport_Black_Scholes.pdf) • 🖼️ Courbes de Payoff & UML |
| [**12. Simulation Stochastique de Jeu en C**](./12_Card_Game_Probabilistic_Simulation) | 1A Math-Info | C, Méthodes de Monte-Carlo, Gantt | [📄 Rapport Probabilités](./12_Card_Game_Probabilistic_Simulation/docs/Rapport_Experience_Probabiliste.pdf) • 📅 Planning Gantt |
| [**16. Lab Traitement du Signal & Wiener**](./16_Signal_Processing_Lab) | 3A Signal Processing | Python, NumPy, SciPy, Filtre de Wiener, Ondelettes | 💻 Notebooks de débruitage audio/image |

---

### 3. 🏗️ Data Engineering, Pipelines & Architecture SaaS
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**02. ETLia : Plateforme ETL Augmentée**](./02_ETLia_AI_Data_Wizard) | **1er Prix Challenge Entreprendre** | React, TypeScript, Tailwind, Python, Streamlit | 💻 Frontend React complet, Backend ETL, Branding |
| [**03. Datamart SunSéjour en Production**](./03_SunSejour_ETL_Datamart) | Projet Data Engineering | Python, Docker, Docker Compose, Star Schema | [📄 Rapport Datamart](./03_SunSejour_ETL_Datamart/reports/Rapport_Datamart_SunSejour.pdf) • [📖 Guide Utilisateur](./03_SunSejour_ETL_Datamart/reports/Guide_Utilisation_ETL_SunSejour.pdf) |

---

### 4. 📈 Machine Learning, Séries Temporelles & Biostatistiques
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**04. Infinity Analytics : Time Series & Scoring**](./04_Infinity_Analytics_Time_Series_ML) | Stage Gainde 2000 | SARIMAX, VAR, DLTS, Calibration ML, Scikit-Learn | [📄 Rapport Stage](./04_Infinity_Analytics_Time_Series_ML/reports/Rapport_de_Stage.pdf) • [📄 Rapport Scoring](./04_Infinity_Analytics_Time_Series_ML/reports/Rapport_Use_Case_7_Scoring.pdf) • [📊 Soutenance](./04_Infinity_Analytics_Time_Series_ML/presentations/Presentation_de_Stage.pdf) |
| [**19. Séries Temporelles Commerce Canadien**](./19_McMaster_Canadian_Retail_Time_Series) | **McMaster University (STATS 4A03)** | R, SARIMA, Holt-Winters, STL, Stationnarité | [📄 Rapport Prévision (12 p.)](./19_McMaster_Canadian_Retail_Time_Series/reports/Canadian_Retail_Time_Series_Forecasting_Report.pdf) |
| [**21. Modèles Linéaires Généralisés (GLM)**](./21_McMaster_Generalized_Linear_Models) | **McMaster University (STATS 4GLM)** | R, GLM Poisson, Gamma, Logistique, Déviance | 💻 5 Rapports d'analyse RMarkdown et scripts |
| [**07. Prédiction Survie Cancer METABRIC**](./07_Breast_Cancer_Biostatistics_MERR) | 2A MERR | R, GLM, Lasso, Elastic Net, Courbes ROC | [📄 Rapport Cancer Survie](./07_Breast_Cancer_Biostatistics_MERR/reports/Rapport_Cancer_Survie_MERR.pdf) |
| [**08. Analyse Factorielle Airbnb NYC**](./08_Airbnb_NYC_Data_Analysis_ANDO) | 2A ANDO | Python, ACP (PCA), ACC (CCA), K-Means, CAH | [📄 Rapport Analyse](./08_Airbnb_NYC_Data_Analysis_ANDO/reports/Rapport_Analyse_Donnees_ANDO.pdf) • [📊 Slides Partie 1](./08_Airbnb_NYC_Data_Analysis_ANDO/presentations/Presentation_Partie_1.pdf) |
| [**09. Machine Learning Économétrique**](./09_Machine_Learning_Economics_DAMI) | Économétrie DAMI | R, Glmnet, ISLR2, Polynomial Reg, Cross-Val | [📄 Rapport ML Salaires](./09_Machine_Learning_Economics_DAMI/reports/Rapport_ML_Econometrics.pdf) |

---

### 5. 💻 Génie Logiciel, Systèmes & Programmation
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**10. Moteur Traitement d'Images en C**](./10_Image_Processing_C_PRIM) | 1A PRIM | C bas niveau, LUT, Convolutions 2D, PGM/PPM | [📄 Rapport C PRIM](./10_Image_Processing_C_PRIM/reports/Rapport_Projet_PRIM.pdf) |
| [**11. Programmation Fonctionnelle OCaml**](./11_Functional_Programming_OCaml) | 1A OCaml | OCaml, Types algébriques, Pattern Matching | [📄 Rapport OCaml](./11_Functional_Programming_OCaml/reports/Rapport_Projet_OCaml.pdf) |
| [**14. Parser d'Expressions & GUI JavaFX**](./14_JavaFX_Expression_Parser) | 1A OOP Java | Java, JavaFX, Design Patterns (Composite, Visitor) | 💻 Application complète JavaFX & tests |

---

## ⚡ Outil d'Automatisation des Candidatures

```bash
# Générer une candidature ciblée en Finance Quantitative
python3 automate_candidatures.py --profil quant --entreprise "QRT"

# Générer une candidature IA / Deep Learning
python3 automate_candidatures.py --profil ai --entreprise "Mistral AI"
```
"""

with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(portfolio_md)
shutil.copy2(portfolio_path, os.path.join(ALL_PROJ_DIR, "PORTFOLIO.md"))
print("[OK] Master README.md et PORTFOLIO.md mis à jour.")

# Re-generate Word documents
doc = docx.Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

title_p = doc.add_paragraph()
title_run = title_p.add_run("PORTFOLIO GLOBAL DES PROJETS D'INGÉNIERIE & IA")
title_run.font.name = "Calibri"
title_run.font.size = Pt(22)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(16, 44, 87)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

sub_p = doc.add_paragraph()
sub_run = sub_p.add_run("Mohamed Nourou Dine CISSE — Élève-Ingénieur ENSIIE & McMaster University\nSpécialisation : Intelligence Artificielle, Data Engineering & Mathématiques Appliquées\nEmail : mouhamed.nouroudine.cisse@gmail.com | Tél : +33 7 65 60 09 97 | GitHub : github.com/nourou-dine-mahy")
sub_run.font.name = "Calibri"
sub_run.font.size = Pt(10.5)
sub_run.font.italic = True
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph("-" * 80)

p_intro = doc.add_paragraph()
r_intro = p_intro.add_run(f"Ce document rassemble la documentation exhaustive, les rapports d'expertise et les présentations de soutenance des {len(catalog)} projets réalisés au cours de mon cursus d'ingénieur à l'ENSIIE, de mon échange académique à McMaster University (Canada) et de mes expériences en entreprise (Publicis Groupe, Infinity Analytics / Gainde 2000, Challenge Entreprendre ENSIIE).")
r_intro.font.name = "Calibri"
r_intro.font.size = Pt(11)

doc.add_heading("Tableau Récapitulatif des 21 Projets", level=1)
table = doc.add_table(rows=1, cols=4)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Projet"
hdr_cells[1].text = "Domaine / Institution"
hdr_cells[2].text = "Stack Technique"
hdr_cells[3].text = "Livrables (Rapports & Slides)"

for cell in hdr_cells:
    for p in cell.paragraphs:
        for r in p.runs:
            r.font.bold = True
            r.font.size = Pt(9.5)

for p in catalog:
    row_cells = table.add_row().cells
    row_cells[0].text = p["title_fr"].split(":")[0].strip()
    row_cells[1].text = f"{p['category']}\n({p['institution']})"
    row_cells[2].text = ", ".join(p["technologies"][:4])
    
    livrables = []
    if p["reports"]:
        livrables.append(f"📄 Rapport ({len(p['reports'])})")
    if p["presentations"]:
        livrables.append(f"📊 Présentation ({len(p['presentations'])})")
    if not livrables:
        livrables.append("💻 Code & Dépôt")
    row_cells[3].text = " + ".join(livrables)

    for cell in row_cells:
        for para in cell.paragraphs:
            for r in para.runs:
                r.font.size = Pt(9)

doc.add_page_break()

for i, p in enumerate(catalog, 1):
    doc.add_heading(f"{i}. {p['title_fr']}", level=1)
    
    meta_p = doc.add_paragraph()
    m_run = meta_p.add_run(f"Contexte : {p['institution']} ({p['year']}) | Rôle : {p['role']}\nDomaine : {p['category']}\nTechnologies : {', '.join(p['technologies'])}")
    m_run.font.italic = True
    m_run.font.size = Pt(10)
    
    doc.add_heading("Synthèse Exécutive :", level=2)
    p_pitch = doc.add_paragraph()
    p_pitch.add_run(p["pitch_fr"])
    
    doc.add_heading("Réalisations Clés & Résultats (Format STAR) :", level=2)
    for b in p["star_bullet_points_fr"]:
        bp = doc.add_paragraph(style='List Bullet')
        bp.add_run(b)
        
    doc.add_heading("Livrables & Justificatifs Associés :", level=2)
    if p["reports"]:
        for r in p["reports"]:
            rp = doc.add_paragraph(style='List Bullet')
            rp.add_run(f"Rapport technique disponible : {r}")
    if p["presentations"]:
        for pr in p["presentations"]:
            prp = doc.add_paragraph(style='List Bullet')
            prp.add_run(f"Présentation / Soutenance : {pr}")
    if not p["reports"] and not p["presentations"]:
        np = doc.add_paragraph(style='List Bullet')
        np.add_run("Code source et documentation intégrés dans le dossier projet.")

    doc.add_paragraph("")

doc.save(os.path.join(ALL_PROJ_DIR, "All_Projects.docx"))
doc.save(os.path.join(BASE_ENSIIE, "All projects.docx"))
print("[OK] Fichiers Word mis à jour avec les 21 projets.")
