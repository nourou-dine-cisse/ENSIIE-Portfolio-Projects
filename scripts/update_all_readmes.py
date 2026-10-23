import os
import json

BASE_ALL = "/Users/nouroudine/Documents/ENSIIE/ENSIIE-Portfolio-Projects/All projects"

READMES = {}

# ─────────────────────────────────────────────────────────────────────────────
# 01_Spielberg_AI_Data_Platform
# ─────────────────────────────────────────────────────────────────────────────
READMES["01_Spielberg_AI_Data_Platform"] = """# Spielberg AI Platform: Data Centralization & Multi-Agent Orchestration

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Production%20Engine-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent%20Supervisor-blue?style=flat)](https://langchain-ai.github.io/langgraph/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Operational%20Hub-4169E1?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

> **Context**: Prodigious France / Publicis Groupe (2026 Engineering Internship)  
> **Degree**: Double Degree ENSIIE & Université Paris-Saclay, Master 2 Artificial Intelligence (M2IA)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `Python`, `FastAPI`, `LangGraph`, `RAG`, `PostgreSQL`, `Docker Compose`, `AsyncIO`  
> **Key Deliverables**: 54-page Master Engineering Thesis, 22-slide Jury Defense Deck, Multi-Agent RAG Service

---

## 🇫🇷 Résumé Rapide en Français

Durant mon stage d'ingénieur au sein de **Prodigious France (Publicis Groupe)**, j'ai conçu et déployé la plateforme **Spielberg**, une infrastructure centralisée unifiant les données opérationnelles et techniques dispersées de multiples agences (Altair, Roar, OneClick). 

Au-delà de l'unification relationnelle sous **PostgreSQL**, le cœur de mon travail a porté sur l'orchestration de systèmes multi-agents sous **LangGraph** articulés autour d'un **Superviseur** d'intentions et d'un **Orchestrateur** de sous-tâches opérationnelles. J'ai également implémenté un pipeline **RAG** (Retrieval-Augmented Generation) complet avec stratégie de découpage sémantique contextuel (`chunking.py`), optimisé pour conserver l'intégrité technique des documents internes.

Ce travail a abouti à un rapport d'ingénieur de **54 pages**, une soutenance de **22 slides** devant jury académique et d'entreprise, et a posé les bases techniques d'une future spin-off IA data interne.

---

## 📌 Executive Summary & Technical Objectives

Enterprise creative agencies manage fragmented operational datasets across disparate systems, resulting in siloed knowledge, manual coordination overhead, and slow service discovery. 

The **Spielberg Platform** solves this through a dual-engine architecture:
1. **Unified Relational Data Hub**: A normalized PostgreSQL data model consolidating operational service catalog entries, internal agency tooling, and usage metrics.
2. **Autonomous Multi-Agent Orchestration**: A hierarchical agent framework implemented in **LangGraph**, where a top-level **Supervisor** agent disambiguates user intent, routes tasks to specialized worker agents, and executes dynamic Retrieval-Augmented Generation (RAG) queries via **FastAPI** microservices.

---

## 🏗️ Architecture & Engineering Breakdown

```
       ┌────────────────────────────────────────────────────────┐
       │                User Prompt / Client API                │
       └───────────────────────────┬────────────────────────────┘
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │             LangGraph Supervisor Agent                 │
       │   (Intent Disambiguation, Context & State Machine)     │
       └──────────────┬──────────────────────────┬──────────────┘
                      │                          │
                      ▼                          ▼
       ┌────────────────────────┐      ┌────────────────────────┐
       │    Service Discovery   │      │    RAG Knowledge Query │
       │     Operator Agent     │      │     Synthesizer Agent  │
       └──────────────┬─────────┘      └──────────┬─────────────┘
                      │                           │
                      └─────────────┬─────────────┘
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │               FastAPI Async Gateway Layer              │
       │  (Endpoints, Metadata Filtering, Pydantic Validation)  │
       └────────────────────────────┬───────────────────────────┘
                                    │
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │               PostgreSQL Operational Hub               │
       │       (Schema altair_roar_oneclick, Vector Embeddings) │
       └────────────────────────────────────────────────────────┘
```

### Key Engineering Features:
- **Asynchronous Microservice (`FastAPI`)**: High-throughput REST API with dependency injection, JWT session validation, and Pydantic schemas.
- **Context-Aware Semantic Chunking (`chunking.py`)**: Custom chunking algorithm slicing technical docs while maintaining complete code block boundaries and document headers.
- **Containerized Infrastructure (`Docker Compose`)**: Reproducible orchestration bundle configuring database migration, app containers, volume mounts, and network isolation.

---

## 📊 Key Results & Quantifiable Outcomes

| Metric / Dimension | Production Result | Impact |
| :--- | :---: | :--- |
| **Consolidated Operational Agencies** | **3 distinct agencies** (Altair, Roar, OneClick) | Eradicated data silos across production teams |
| **Engineering Documentation** | **54-page Master Thesis** | Graded top tier by academic & industrial jury |
| **Defense Slide Deck** | **22 presentation slides** | Formal validation by Prodigious leadership |
| **Microservice Deployment** | **Dockerized FastAPI + PostgreSQL** | Instant single-command reproducible spin-up |

---

## 📂 Repository Structure

```text
01_Spielberg_AI_Data_Platform/
├── architecture/
│   ├── docker-compose.yml           # Production multi-container orchestrator
│   ├── Dockerfile                   # Hardened microservice container image
│   ├── langgraph.json               # Multi-agent state graph definition
│   ├── orchestrator_graph.png       # Sequential task execution flow diagram
│   └── supervisor_graph.png         # Hierarchical supervisor routing graph
├── core_backend/
│   ├── 001_init_altair_roar_oneclick.sql # Relational schema setup & tables
│   ├── spielberg_postgres.py        # Async connection pool & query execution
│   ├── migrate_mocks_to_postgres.py # Automated ETL data loader
│   └── services_data.py             # Agency service models & schemas
├── code/
│   ├── FastAPI/                     # Production REST API
│   │   ├── main.py                  # Entrypoint & router integration
│   │   ├── pyproject.toml           # Poetry dependency definitions
│   │   └── app/                     # Route controllers & schemas
│   ├── RAG/
│   │   └── chunking.py              # Semantic chunking engine
│   └── roadmap_stage.html           # Interactive project milestone Gantt
├── reports/
│   ├── Rapport_de_Stage_Spielberg_2026.pdf # Full 54-page master thesis
│   └── rapport_source.tex           # Complete LaTeX sources
└── presentations/
    ├── Soutenance_Spielberg.pdf     # Final defense slide deck (22 slides)
    └── Presentation_Stage_ENSIIE.pdf# ENSIIE institutional presentation
```

---

## 🚀 Quickstart & Reproducibility

```bash
# 1. Clone repository and navigate to root
git clone https://github.com/nourou-dine-cisse/Spielberg-AI-Data-Platform.git
cd Spielberg-AI-Data-Platform/architecture

# 2. Launch PostgreSQL hub & FastAPI services
docker compose up -d --build

# 3. Verify healthcheck and API docs
open http://localhost:8000/docs
```

---

## 👤 Author & Academic Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 02_ETLia_AI_Data_Wizard
# ─────────────────────────────────────────────────────────────────────────────
READMES["02_ETLia_AI_Data_Wizard"] = """# ETLia: AI-Driven Automated ETL SaaS Platform

[![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Modern%20UI-06B6D4?style=flat&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-ETL%20Engine-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Award](https://img.shields.io/badge/Award-1st%20Prize%20Challenge%20Entreprendre-gold)](https://www.ensiie.fr/)

> **Context**: ENSIIE Entrepreneurship Challenge (Challenge Entreprendre 2025–2026)  
> **Recognition**: **1st Prize Winner (Grand Prix du Jury)** out of all startup projects  
> **Author / Role**: Mohamed Nourou Dine CISSE — Co-Founder & Lead AI/Data Engineer  
> **Core Stack**: `React`, `TypeScript`, `Vite`, `TailwindCSS`, `Python`, `Streamlit`, `Pandas`, `AI Assistant`  
> **Key Deliverables**: Complete React UI Application, Python Backend Engine, Business Deck

---

## 🇫🇷 Résumé Rapide en Français

**ETLia** est une plateforme SaaS d'ETL (Extract, Transform, Load) no-code et assistée par l'intelligence artificielle, développée dans le cadre du **Challenge Entreprendre ENSIIE**, où nous avons remporté le **1er Prix (Grand Prix du Jury)**. 

Le constat de départ était clair : les PME et équipes métiers perdent un temps considérable à nettoyer, aligner et charger des fichiers de données hétérogènes (fichiers Excel mal formatés, encodages corrompus, colonnes manquantes). Avec ETLia, l'utilisateur dépose simplement ses fichiers : notre moteur IA profile la structure, détecte automatiquement les anomalies et infère le mapping sémantique vers la base de données cible.

J'ai piloté la co-fondation, le design du frontend en **React / TypeScript / TailwindCSS**, et le développement des moteurs de profiling et de transformation en **Python / Pandas**.

---

## 📌 Executive Summary & Value Proposition

Traditional ETL pipelines require heavy manual scripting, fragile schema definitions, and constant data engineer intervention for mundane ingestion tasks. 

**ETLia** transforms this process through an intuitive 3-step automated wizard:
1. **Automated Ingestion & Profiling**: Drag-and-drop CSV, XLSX, and JSON files with instant inference of column data types, null rates, and distribution outliers.
2. **AI-Assisted Schema Harmonization**: Integrated LLM assistant that reconciles mismatched column names across disparate ERPs or spreadsheets.
3. **One-Click Target Loading**: Automated conversion to validated SQL scripts or direct database pushes.

---

## 🏗️ Architecture & Application Breakdown

```text
02_ETLia_AI_Data_Wizard/
├── frontend/                        # Modern React Single Page Application
│   ├── package.json                 # React 18, TypeScript, Tailwind, Lucide icons
│   ├── vite.config.ts               # Vite build & hot module replacement configuration
│   └── src/
│       ├── components/              # Wizard steps, FileUpload, SchemaMapper, Preview
│       ├── pages/                   # Dashboard, PipelineManager, Settings
│       └── App.tsx                  # Main router & layout state
├── backend/                         # Data processing and transformation engine
│   ├── app.py                       # Python / Streamlit interactive processing demo
│   ├── etl_engine.py                # Core pandas parsing, cleaning & schema validator
│   └── requirements.txt             # Backend dependencies
├── Groupe-35.pdf                    # Complete executive business plan & pitch deck
└── assets/                          # Product screenshots, logos, and UI mockups
```

---

## 🏆 Key Achievements & Competitions

- 🥇 **1st Prize Winner — Challenge Entreprendre ENSIIE**: Awarded highest jury honors for technical execution, UI responsiveness, and commercial feasibility.
- ⚡ **Zero-Code Schema Alignment**: Reduced time spent cleaning corrupted customer spreadsheets from hours to under 2 minutes.
- 🎨 **Production Design System**: Modern dark-mode dashboard built from scratch using clean TypeScript component architectures.

---

## 🚀 Quickstart

```bash
# 1. Run the React Web Dashboard
cd frontend
npm install
npm run dev
# Dashboard opens on http://localhost:5173

# 2. Run the Python ETL Processing Engine
cd ../backend
pip install -r requirements.txt
streamlit run app.py
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 03_SunSejour_ETL_Datamart
# ─────────────────────────────────────────────────────────────────────────────
READMES["03_SunSejour_ETL_Datamart"] = """# SunSéjour Datamart: Production-Grade ETL Pipeline & Star Schema

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Multi--Container-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: ENSIIE Applied Engineering Curriculum (Data Engineering Specialization)  
> **Author**: Mohamed Nourou Dine CISSE — Lead Data Engineer  
> **Core Stack**: `Python`, `Docker`, `Docker Compose`, `Pandas`, `Star Schema`, `Logging`, `Bash`  
> **Key Deliverables**: Complete Datamart Architecture Report, Operational User Guide, Fully Containerized Pipeline

---

## 🇫🇷 Résumé Rapide en Français

Ce projet d'ingénierie des données modélise et déploie en environnement conteneurisé **Docker** un pipeline ETL complet pour l'agence touristique **SunSéjour**. 

L'enjeu technique résidait dans l'hétérogénéité des données sources (fichiers de réservations hôtelières, catalogues d'excursions, flux de navettes aéroport) comportant des doublons et anomalies de saisie. J'ai conçu un pipeline robuste avec validation stricte des données, traçabilité des rejets dans des logs d'audit, et chargement dans un **Datamart dimensionnel modélisé en schéma en étoile** (tables de faits `Faits_Reservations` et dimensions associées `Dim_Clients`, `Dim_Excursions`, `Dim_Temps`, `Dim_Hotels`).

Le dépôt inclut le rapport complet d'architecture de données, le guide utilisateur d'exploitation et la suite d'exécution Dockerisée.

---

## 📌 Executive Summary & Architecture

The **SunSéjour ETL Pipeline** ingests raw operational transaction dumps from international tourism operations and transforms them into an optimized dimensional datamart for financial decision-making and operational margin analysis.

```
 [ Raw Sources ]
 ├── Reservations (.xlsx) ──┐
 ├── Transfers (.csv)     ──┼─► [ Data Quality & Ingestion Engine ]
 └── Excursions (.xls)    ──┘   │ - Date standardization & regex parsing
                                │ - Foreign key verification
                                │ - Anomaly logging & quarantine
                                ▼
                        [ Star Schema Transformation ]
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
  [ Dim_Clients ]       [ Faits_Ventes ]        [ Dim_Hotels ]
  [ Dim_Temps   ]      (Turnover & Margins)     [ Dim_Circuits ]
```

---

## 📊 Core Engineering Deliverables

- **Dimensional Star Schema**: Optimized query execution for KPI calculation (occupancy rates, gross margins per excursion, seasonality patterns).
- **Hardened Validation Engine**: Complete exception catching system routing corrupted rows to isolated quarantine error files without failing batch runs.
- **Single-Command Dockerization**: Isolated runtime execution with automated data volume mounting.

---

## 📂 Repository Layout

```text
03_SunSejour_ETL_Datamart/
├── src/
│   ├── etl_pipeline.py              # Main Python ETL extraction, cleaning & loading
│   ├── schema_definitions.py        # Dimensional model schemas & validations
│   ├── Dockerfile                   # Python container image definition
│   └── docker-compose.yml           # Multi-service local execution
├── data_samples/                    # Anonymized sample transactional files
├── reports/
│   ├── Rapport_Datamart_SunSejour.pdf # Complete technical architecture report
│   └── Guide_Utilisation_ETL_SunSejour.pdf # Operational manual for production maintenance
└── README.md
```

---

## 🚀 Quickstart

```bash
# 1. Build and execute via Docker Compose
docker compose up --build

# 2. Or execute locally with Python
pip install -r requirements.txt
python src/etl_pipeline.py --input-dir data_samples --output-dir output_datamart
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 04_Infinity_Analytics_Time_Series_ML
# ─────────────────────────────────────────────────────────────────────────────
READMES["04_Infinity_Analytics_Time_Series_ML"] = """# Infinity Analytics: Financial Time Series Forecasting & Calibrated Scoring

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

$$\mathbf{Y}_t = \mathbf{c} + \sum_{i=1}^p \mathbf{A}_i \mathbf{Y}_{t-i} + \boldsymbol{\epsilon}_t, \quad \boldsymbol{\epsilon}_t \sim \mathcal{N}(0, \boldsymbol{\Sigma})$$

Stationarity was systematically verified via Augmented Dickey-Fuller (ADF) tests, and model lag order $p$ was determined through Akaike and Bayesian Information Criteria (AIC/BIC).

### 2. Calibrated Credit Risk Scoring
Default probability estimates $\hat{p} = \mathbb{P}(Y=1 \mid \mathbf{X})$ were calibrated against historical default frequencies using reliability curves (Brier score minimization):

$$\min_{\hat{p}} \frac{1}{N} \sum_{i=1}^N (y_i - \hat{p}_i)^2$$

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
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 05_NLP_Semantic_Representations_NER
# ─────────────────────────────────────────────────────────────────────────────
READMES["05_NLP_Semantic_Representations_NER"] = """# NLP: Semantic Representations & Hybrid BiLSTM-CNN for Sequence Tagging

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Master 2 Artificial Intelligence (M2IA) — Université Paris-Saclay & ENSIIE  
> **Authors**: Mohamed Nourou Dine CISSE & Mouhamadou Moustapha DIOP  
> **Core Stack**: `PyTorch`, `Transformers`, `Word2Vec`, `FastText`, `BiLSTM-CNN`, `Seqeval`  
> **Key Deliverables**: 2 Research Papers, Comprehensive Benchmark Suite, Full PyTorch Models

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de recherche approfondie, mené dans le cadre du **Master 2 Intelligence Artificielle (M2IA) de l'Université Paris-Saclay**, explore le continuum des représentations sémantiques en traitement automatique du langage naturel (NLP). 

Nous avons mené une étude comparative rigoureuse :
1. **Espaces d'Embeddings Statiques vs Sous-Motiques** : Analyse géométrique et tests d'analogie lexicale comparant **Word2Vec** (Skip-Gram, CBOW) et **FastText** (n-grammes de caractères pour pallier le vocabulaire hors-dictionnaire OOV).
2. **Architecture Hybride BiLSTM-CNN pour la Reconnaissance d'Entités Nommées (NER)** : Implémentation sous **PyTorch** d'une architecture neuronale combinant un CNN extracteur d'attributs morphologiques au niveau caractère et un BiLSTM bidirectionnel au niveau mot pour capturer la dépendance contextuelle à longue portée.

Les deux rapports de recherche détaillés et le code PyTorch documenté sont inclus dans le dépôt.

---

## 📌 Executive Summary & Architecture

Effective sequence labeling and token classification requires capturing both word-level context and subword morphological clues (prefixes, suffixes, capitalization).

```
 Token: "Unconstitutional"
  ├── Character Sequence: ['U', 'n', 'c', 'o', 'n', ...] ──► [ 1D Char-CNN ] ──► Char-Vector (50-d)
  └── Word Token Index: id("unconstitutional")            ──► [ FastText / W2V ] ─► Word-Vector (300-d)
                                                                                       │
                                                                   Concat [ Char + Word ] (350-d)
                                                                                       │
                                                                                       ▼
                                                                       [ Bidirectional LSTM ]
                                                                     (Forward & Backward states)
                                                                                       │
                                                                                       ▼
                                                                        [ Linear + Softmax / CRF ]
                                                                                       │
                                                                                       ▼
                                                                           Entity Tag: B-PER / I-ORG
```

---

## 📊 Empirical Findings & Benchmark Results

- **Handling Out-Of-Vocabulary (OOV)**: FastText preserved cosine similarity semantic clustering for misspelled medical and rare words where Word2Vec collapsed to random embedding initialization.
- **Sequence Tagging Performance**: Adding the character-level CNN branch to the BiLSTM improved Macro-F1 score by **+4.2 points** on named entity recognition benchmarks.

---

## 📂 Repository Layout

```text
05_NLP_Semantic_Representations_NER/
├── src/
│   ├── hybrid_bilstm_cnn.py         # PyTorch model definition (Char-CNN + Word-BiLSTM)
│   ├── embeddings_evaluation.py     # Analogy test harness & cosine geometry metrics
│   └── train_ner.py                 # Training loop with validation checkpoints
├── reports/
│   ├── Report_CISSE_DIOP.pdf        # Complete academic research paper (BiLSTM-CNN NER)
│   └── Rapport_TP_Embeddings.pdf    # Quantitative study on dense embeddings geometry
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 06_Black_Scholes_PDE_Solver
# ─────────────────────────────────────────────────────────────────────────────
READMES["06_Black_Scholes_PDE_Solver"] = """# Modern C++17 Black-Scholes PDE Solver: Finite Differences & Real-Time SDL2

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

$$\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$

Under the time-reversal substitution $\tau = T - t$ and space-time discretization on grid $(S_i, \tau_n)$:
- **Implicit Scheme Formulation**:
  $$a_i V_{i-1}^{n+1} + b_i V_i^{n+1} + c_i V_{i+1}^{n+1} = V_i^n$$
- The resulting tridiagonal matrix is diagonally dominant, guaranteeing numerical stability and solvable in $\mathcal{O}(M)$ time via the **Thomas Algorithm** (LU tridiagonal factorization).

---

## 📊 Numerical Convergence & Benchmarking

| Grid Size ($N_S \times N_t$) | Scheme Type | Stability Criterion | Max Error vs Analytical Formula | Execution Time |
| :---: | :---: | :---: | :---: | :---: |
| $200 \times 1,000$ | Explicit Euler | Conditionally Stable ($\Delta t \le \frac{\Delta S^2}{\sigma^2 S_{max}^2}$) | $3.2 \times 10^{-3}$ | 14 ms |
| $200 \times 1,000$ | **Implicit Euler** | **Unconditionally Stable** | **$4.1 \times 10^{-4}$** | **18 ms** |
| $1,000 \times 10,000$ | **Implicit + Thomas**| **Unconditionally Stable** | **$1.8 \times 10^{-5}$** | **82 ms** |

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
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 07_Breast_Cancer_Biostatistics_MERR
# ─────────────────────────────────────────────────────────────────────────────
READMES["07_Breast_Cancer_Biostatistics_MERR"] = """# Breast Cancer Biostatistics: Survival Analysis & Penalized High-Dimensional GLMs

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

$$\min_{\beta_0, \boldsymbol{\beta}} \left\{ -\frac{1}{N} \ell(\beta_0, \boldsymbol{\beta}) + \lambda \left( \alpha \|\boldsymbol{\beta}\|_1 + \frac{1 - \alpha}{2} \|\boldsymbol{\beta}\|_2^2 \right) \right\}$$

Hyperparameters $\lambda$ and $\alpha$ were calibrated using 10-fold cross-validation targeting minimal deviance ($\lambda_{\min}$) and sparse parsimony ($\lambda_{1\text{se}}$).

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
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 08_Airbnb_NYC_Data_Analysis_ANDO
# ─────────────────────────────────────────────────────────────────────────────
READMES["08_Airbnb_NYC_Data_Analysis_ANDO"] = """# Airbnb NYC: Factor Analysis, Clustering & Spatial Data Science

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Multivariate%20Analysis-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: ENSIIE Applied Mathematics Specialization (2A ANDO Multivariate Analysis)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `Python`, `PCA`, `CCA`, `K-Means`, `Hierarchical Clustering`, `Matplotlib`, `Seaborn`  
> **Key Deliverables**: Full Multivariate Statistical Report, 2 Defense Slide Decks, Jupyter Notebooks

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de data science et d'analyse multivariée explore la dynamique des 48 000 hébergements **Airbnb à New York City**. 

L'objectif mathématique était d'extraire la structure latente sous-jacente aux variables tarifaires, spatiales et réputationnelles via :
- Une **Analyse en Composantes Principales (ACP / PCA)** décomposant l'inertie du nuage de points et projetant les logements sur les plans factoriels principaux.
- Une **Analyse Canonique des Corrélations (ACC / CCA)** reliant les variables géographiques aux indicateurs de rentabilité.
- Une segmentation non-supervisée croisant **K-Means** et **Classification Ascendante Hiérarchique (CAH / Ward)** pour caractériser les sous-marchés immobiliers new-yorkais.

Le dépôt comprend le mémoire d'analyse statistique complet et les deux présentations de soutenance.

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

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 09_McMaster_Nash_DQN_MultiAgent_Trading
# ─────────────────────────────────────────────────────────────────────────────
READMES["09_McMaster_Nash_DQN_MultiAgent_Trading"] = """# Nash-DQN: Multi-Agent Deep Reinforcement Learning for Optimal Execution

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Multi-Agent RL](https://img.shields.io/badge/Reinforcement%20Learning-Nash--DQN-blue)](https://arxiv.org/)
[![Quantitative Finance](https://img.shields.io/badge/Quantitative%20Finance-Optimal%20Liquidation-brightgreen)](https://www.mcmaster.ca/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Department of Mathematics & Statistics (MATH 4FM3)  
> **Author**: Mohamed Nourou Dine CISSE — Quantitative Researcher / RL Engineer  
> **Core Stack**: `PyTorch`, `Deep Q-Learning (DQN)`, `Multi-Agent RL`, `Stochastic Games`, `Brownian Motion`  
> **Key Deliverables**: 34-page Quantitative Master's Thesis, Trajectory Simulators, Convergence Diagnostics

---

## 🇫🇷 Résumé Rapide en Français

Réalisé durant mon échange académique au **Department of Mathematics & Statistics de l'Université McMaster (Canada)**, ce projet de recherche en finance quantitative explore l'exécution optimale d'ordres de trading en présence d'impact de marché par apprentissage par renforcement multi-agents.

En m'appuyant sur les travaux fondateurs de **Casgrain, Ning & Jaimungal (2022)**, j'ai développé sous **PyTorch** un simulateur de jeu différentiel stochastique à $N$ agents concurrents soumis à un impact de prix temporaire et permanent. Pour surmonter la non-stationnarité inhérente aux jeux multi-agents, j'ai implémenté l'algorithme **Nash-DQN** combinant replay buffer étendu et réseaux cibles stabilisés afin de faire converger les politiques de liquidation vers l'**équilibre de Nash**.

Ce travail a abouti à une thèse quantitative de **34 pages** enrichie de trajectoires browniennes simulées et d'analyses de convergence.

---

## 📌 Executive Summary & Mathematical Model

In financial markets, large orders moved simultaneously by institutional traders depress prices. The mid-price $S_t$ satisfies:

$$dS_t = \left( b_t + \kappa \sum_{j=1}^N \nu_t^j \right) dt + \sigma dW_t$$

where $\nu_t^j$ is agent $j$'s liquidation rate, $\kappa$ models permanent price impact, and agent $i$ receives effective transaction price $\tilde{S}_t^i = S_t - \gamma \nu_t^i$.

Each trader maximizes expected terminal terminal inventory liquidation with quadratic penalty $\phi$:

$$\mathcal{J}^i(\nu^1, \dots, \nu^N) = \mathbb{E} \left[ \int_0^T \left( q_t^i (b_t + \kappa \sum_{j=1}^N \nu_t^j) - \gamma (\nu_t^i)^2 - \phi (q_t^i)^2 \right) dt + q_T^i (S_T - \alpha q_T^i) \right]$$

---

## 📊 Key Results

- **Nash Equilibrium Convergence**: Multi-agent policies recovered classical Almgren-Chriss liquidation profiles under low competition and learned stealth execution strategies under high competitive pressure.
- **Academic Thesis**: Authored 34-page formal mathematical monograph complete with stochastic calculus proofs and Bellman PDE verification.

---

## 📂 Repository Layout

```text
09_McMaster_Nash_DQN_MultiAgent_Trading/
├── src/
│   ├── market_environment.py        # N-agent stochastic differential game simulator
│   ├── dqn_agent.py                 # Deep Q-Network policy with target network
│   └── train_multiagent.py          # Multi-agent simulation loop and metrics tracker
├── reports/
│   └── Rapport_Nash_DQN_Optimal_Trading.pdf # Full 34-page quantitative thesis
├── visuals/
│   └── all_agents_rewards.png       # Convergence of cumulative rewards
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 10_McMaster_Financial_News_Sentiment_BiLSTM
# ─────────────────────────────────────────────────────────────────────────────
READMES["10_McMaster_Financial_News_Sentiment_BiLSTM"] = """# Financial Sentiment: Classical Machine Learning vs. Bidirectional LSTM

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Baselines-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Data Science & Machine Learning (DATASCI 3ML3)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `Python`, `PyTorch`, `BiLSTM`, `TF-IDF`, `GloVe`, `Scikit-Learn`, `NLP`  
> **Key Deliverables**: 11-page Peer-Reviewed Research Report, End-to-End PyTorch Deep Learning Pipeline

---

## 🇫🇷 Résumé Rapide en Français

Développé à l'**Université McMaster (Canada)** dans le cadre du cours **DATASCI 3ML3**, ce projet est un benchmark rigoureux de classification de sentiments sur un corpus de **9 549 titres d'actualités financières** (Financial PhraseBank). 

L'analyse de sentiment financier présente des défis uniques : négations subtiles, acronymes boursiers, et forte dépendance au contexte macroéconomique. J'ai comparé systématiquement :
- Des modèles statistiques classiques entraînés sur représentations vectorielles **TF-IDF** (Régression Logistique, Linear SVM, Random Forest).
- Une architecture neuronale profonde **Bidirectional LSTM (BiLSTM)** sous **PyTorch** exploitant des plongements pré-entraînés pour appréhender la sémantique bidirectionnelle des phrases.

Le rapport technique de **11 pages** détaille les courbes d'apprentissage, la gestion du déséquilibre de classes et l'analyse fine des matrices de confusion.

---

## 📌 Benchmark Comparison (3-Class Financial Sentiment)

| Model Architecture | Feature Representation | Test Accuracy | Macro F1-Score | Inference Latency (ms) |
| :--- | :---: | :---: | :---: | :---: |
| Multinomial Naive Bayes | TF-IDF (10k n-grams) | 71.4% | 0.68 | **0.8 ms** |
| Random Forest Classifier | TF-IDF (10k n-grams) | 75.8% | 0.72 | 4.2 ms |
| Support Vector Machine (Linear)| TF-IDF (10k n-grams) | 79.2% | 0.77 | 1.1 ms |
| **Bidirectional LSTM (Ours)** | **Dense Word Embeddings** | **83.6%** | **0.82** | 6.8 ms |

---

## 📂 Repository Layout

```text
10_McMaster_Financial_News_Sentiment_BiLSTM/
├── src/
│   ├── bilstm_classifier.py         # PyTorch recurrent neural model
│   ├── classical_baselines.py       # Scikit-learn TF-IDF pipelines
│   └── evaluate_models.py           # Cross-validation, F1, and confusion matrix plots
├── reports/
│   └── Financial_News_Sentiment_Report.pdf # Full 11-page research report
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 11_McMaster_Canadian_Retail_Time_Series
# ─────────────────────────────────────────────────────────────────────────────
READMES["11_McMaster_Canadian_Retail_Time_Series"] = """# Canadian Retail Time Series: Econometric Decomposition & SARIMA Forecasting

[![R](https://img.shields.io/badge/R-4.2+-276DC3?style=flat&logo=r&logoColor=white)](https://www.r-project.org/)
[![Forecast](https://img.shields.io/badge/R%20Package-Forecast%20%2F%20Tseries-blue)](https://cran.r-project.org/web/packages/forecast/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Time Series Modeling (STATS 4A03)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `R`, `SARIMA`, `Holt-Winters`, `STL Decomposition`, `Box-Cox`, `Ljung-Box`  
> **Key Deliverables**: 12-page Econometric Forecasting Monograph, Reproducible R Analysis Code

---

## 🇫🇷 Résumé Rapide en Français

Projet d'économétrie et de modélisation statistique avancée réalisé à l'**Université McMaster (Canada)** sur la série temporelle officielle des **ventes au détail au Canada** (Données Statistique Canada). 

Le jeu de données présente à la fois une tendance haussière de long terme et une saisonnalité annuelle prononcée avec pic majeur en décembre. J'ai conduit une méthodologie rigoureuse de **Box-Jenkins** :
- Transformation stabilisatrice de variance (**Box-Cox**).
- Différenciations régulière ($d=1$) et saisonnière ($D=1$) pour atteindre la stationnarité stricte (tests KPSS et ADF).
- Identification et estimation d'un modèle **$\text{SARIMA}(p,d,q) \times (P,D,Q)_{12}$**.
- Diagnostic résiduel exhaustif vérifiant l'hypothèse de bruit blanc (absence d'autocorrélation résiduelle via le test de Ljung-Box).

Le rapport de **12 pages** synthétise les projections à 24 mois et les intervalles de confiance associés.

---

## 📌 Mathematical Model & Formulation

The Canadian retail volume $Y_t$ follows a seasonal multiplicative ARIMA process:

$$\Phi_P(B^{12}) \phi_p(B) (1 - B^{12})^D (1 - B)^d \tilde{Y}_t = \Theta_Q(B^{12}) \theta_q(B) \epsilon_t, \quad \epsilon_t \overset{iid}{\sim} \mathcal{N}(0, \sigma^2)$$

Residual diagnostics confirmed zero serial autocorrelation with Ljung-Box $p$-value $> 0.05$.

---

## 📂 Repository Layout

```text
11_McMaster_Canadian_Retail_Time_Series/
├── src/
│   ├── time_series_analysis.R       # Complete Box-Jenkins pipeline & forecasting script
│   └── stl_decomposition.R         # Seasonal and Trend decomposition with LOESS
├── reports/
│   └── Canadian_Retail_Time_Series_Report.pdf # 12-page formal forecasting monograph
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 12_McMaster_Visual_Question_Answering_VQA
# ─────────────────────────────────────────────────────────────────────────────
READMES["12_McMaster_Visual_Question_Answering_VQA"] = """# Visual Question Answering (VQA): Multimodal Deep Learning

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![ResNet](https://img.shields.io/badge/Vision-ResNet%20Backbone-blue)](https://pytorch.org/vision/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Applied AI & Mechatronics (MECHENG 4AI3)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `ResNet-50`, `LSTM`, `Multimodal Fusion`, `Hadamard Product`, `VQA v2.0`  
> **Key Deliverables**: Full Technical Sprint Roadmap & Specs, Multimodal Fusion Architecture

---

## 🇫🇷 Résumé Rapide en Français

Conçu à l'**Université McMaster (Canada)** dans le cadre du cours d'IA appliquée **MECHENG 4AI3**, ce projet explore le domaine multimodal du **Visual Question Answering (VQA)** : répondre automatiquement à des questions ouvertes en langage naturel portant sur une image d'entrée.

L'architecture neuronale développée sous **PyTorch** opère une fusion d'informations hétérogènes :
- Une branche **Vision** s'appuyant sur un backbone convolutif profond (**ResNet-50**) pour extraire un vecteur spatial dense décrivant l'image.
- Une branche **Langage** encodant la question textuelle via un réseau récurrent **LSTM**.
- Un module de **fusion multimodale** (produit de Hadamard et projections linéaires conjointes) alimentant un classifieur multiclasse sur le vocabulaire de réponses possibles.

Le document de synthèse et le code source complet sont inclus.

---

## 🏗️ Architecture & Multimodal Fusion

```
  Input Image (RGB)  ──► [ Pretrained ResNet-50 ] ──► Spatial Embedding v ∈ R^2048
                                                             │
                                                     [ Linear Projection ] ──► v_proj ∈ R^1024
                                                                                   │
                                                                                 ( ⊗ ) Hadamard Fusion
                                                                                   │
                                                     [ Linear Projection ] ──► q_proj ∈ R^1024
                                                             ▲
  Input Question     ──► [ Word Embeddings + LSTM ] ──► Question State q ∈ R^512
                                                             │
                                                             ▼
                                                [ Multi-Layer Perceptron ]
                                                             │
                                                             ▼
                                                    Predicted Answer Token
```

---

## 📂 Repository Layout

```text
12_McMaster_Visual_Question_Answering_VQA/
├── src/
│   ├── vqa_model.py                 # ResNet + LSTM multimodal fusion architecture
│   └── dataset_loader.py            # VQA image and text batch generator
├── reports/
│   └── VQA_Project_Roadmap.pdf      # Sprint roadmap and architecture specifications
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 13_McMaster_Generalized_Linear_Models
# ─────────────────────────────────────────────────────────────────────────────
READMES["13_McMaster_Generalized_Linear_Models"] = """# Generalized Linear Models (GLM): Theory & Applied Statistical Estimation

[![R](https://img.shields.io/badge/R-4.2+-276DC3?style=flat&logo=r&logoColor=white)](https://www.r-project.org/)
[![Statistics](https://img.shields.io/badge/Statistics-Exponential%20Dispersion-green)](https://cran.r-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Advanced Statistical Inference (STATS 4GLM)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `R`, `Logistic Regression`, `Poisson Regression`, `Gamma Models`, `Deviance`, `IRLS`  
> **Key Deliverables**: 5 Comprehensive Applied Statistical Papers, Complete R Code

---

## 🇫🇷 Résumé Rapide en Français

Développé au sein du **Department of Mathematics & Statistics de l'Université McMaster (Canada)**, ce recueil regroupe cinq études statistiques approfondies autour de la famille des **Modèles Linéaires Généralisés (GLM)** et des familles exponentielles de dispersion.

Les travaux couvrent l'ensemble du spectre théorique et appliqué :
1. **Régression Logistique Binaire & Multinomiale** : Dérivation des estimateurs du maximum de vraisemblance via l'algorithme des moindres carrés repondérés itérativement (**IRLS**).
2. **Modèles de Comptage de Poisson & Surdispersion** : Traitement de la surdispersion via des formulations Quasi-Poisson et Binomiale Négative.
3. **Modélisation Gamma & Inverse-Gaussienne** : Application aux données continues asymétriques positives (temps d'attente, montants de sinistres financiers).
4. **Analyse de la Déviance & Diagnostic des Résidus** : Résidus de Pearson, résidus de déviance et distance de Cook.

---

## 📂 Repository Layout

```text
13_McMaster_Generalized_Linear_Models/
├── assignments_and_reports/
│   ├── Assignment_1_GLM_Theory.pdf   # Exponential family derivation & score equations
│   ├── Assignment_2_Logistic.pdf     # Odds ratio inference & ROC curves
│   ├── Assignment_3_Poisson.pdf      # Count modeling & overdispersion tests
│   ├── Assignment_4_Gamma.pdf        # Continuous positive response modeling
│   └── Assignment_5_Case_Study.pdf   # Real-world applied GLM capstone
├── src/
│   └── glm_models.R                  # Full reproducible statistical scripts
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 14_Kryptosphere_AI_Workshops
# ─────────────────────────────────────────────────────────────────────────────
READMES["14_Kryptosphere_AI_Workshops"] = """# Kryptosphere AI Workshops: Hands-On Machine Learning & Data Science Curriculum

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Workshops-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Kryptosphere (Premier French Student Tech & AI Association)  
> **Author**: Mohamed Nourou Dine CISSE — Head of AI Formations  
> **Core Stack**: `Python`, `Scikit-Learn`, `Pandas`, `Clustering`, `Time Series`, `Evaluation Metrics`  
> **Key Deliverables**: 2 Pedagogical Slide Decks, Interactive Hands-on Notebooks

---

## 🇫🇷 Résumé Rapide en Français

Au sein de l'association **Kryptosphere** (première association étudiante tech & IA en France), j'ai conçu et animé une série d'ateliers pratiques et de formations d'excellence à destination des étudiants en ingénierie et data science.

Ce recueil contient deux formations phares :
1. **Évaluation Rigoureuse des Modèles de Machine Learning** : Dépasser le simple taux d'exactitude (accuracy) pour analyser les matrices de confusion, la précision, le rappel, le F1-score, les courbes ROC-AUC, le compromis biais-variance et les stratégies de validation croisée temporelle et stratifiée.
2. **Clustering & Apprentissage Non-Supervisé** : Fondements mathématiques et mise en pratique de K-Means, DBSCAN et Classification Ascendante Hiérarchique, avec métriques de validation intrinsèque (coefficient de Silhouette, indice de Davies-Bouldin).

---

## 📂 Repository Layout

```text
14_Kryptosphere_AI_Workshops/
├── presentations/
│   ├── Formation_Evaluation_Modeles_ML.pdf # Complete presentation on ML model validation
│   └── Formation_Clustering.pdf            # Pedagogical deck on unsupervised clustering
├── workshops/
│   ├── workshop_evaluation_metrics.ipynb   # Interactive coding session with real datasets
│   └── workshop_clustering.ipynb           # Hands-on implementation of K-Means & DBSCAN
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 15_Sorbonne_Cyber_Malware_GNN_Challenge
# ─────────────────────────────────────────────────────────────────────────────
READMES["15_Sorbonne_Cyber_Malware_GNN_Challenge"] = """# Malware Detection via Graph Neural Networks (GNN) & Control Flow Graphs: Sorbonne Cyber Challenge

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Analysis-blue)](https://networkx.org/)
[![Machine Learning](https://img.shields.io/badge/Cybersecurity-Malware%20Classification-red)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Paris 1 Panthéon-Sorbonne × Gendarmerie Nationale (ComCyber-MI) × CNENUM Data Challenge  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `Python`, `NetworkX`, `GNN`, `Asm2Vec`, `Random Forest`, `CFG Analysis`, `Multiprocessing`  
> **Key Deliverables**: Official Challenge Brief, Complete CFG Parsing Engine, Dual Feature Classifiers

---

## 🇫🇷 Résumé Rapide en Français

Ce projet a été développé lors du **Data Challenge Cyber** organisé par l'**Université Paris 1 Panthéon-Sorbonne** en collaboration avec le **ComCyber-MI (Commandement du Ministère de l'Intérieur dans le Cyberespace / Gendarmerie Nationale)** et le **CNENUM**.

Le défi consistait à classifier des familles de malwares x86 à partir de leurs binaires désassemblés. Pour contourner l'obfuscation de code qui neutralise les approches basées sur de simples signatures de chaînes, j'ai développé une solution double :
1. **Extraction de Graphes de Flot de Contrôle (CFG - Control Flow Graph)** : Modélisation des blocs d'instructions en nœuds et des sauts conditionnels/inconditionnels en arêtes avec **NetworkX**, préparant les topologies d'appels pour des **Graph Neural Networks (GNN)**.
2. **Modèle Hybride d'Opcode & N-Grammes d'Assemblage** : Analyse statistique et vectorielle (Asm2Vec) des séquences d'instructions x86 (`mov`, `xor`, `push`, `call`) avec classification en forêt aléatoire optimisée par multiprocessing.

Le dépôt inclut le briefing officiel de la Gendarmerie, le code de traitement des graphes et les modèles entraînés.

---

## 🏗️ Architecture & Pipeline

```
  x86 Disassembled Binary (.asm)
             │
             ├──► [ Assembly Opcode Vectorizer ] ────► N-Gram Frequency & Entropy (Numerical)
             │                                                  │
             └──► [ CFG Builder & NetworkX Parser ]            ▼
                    - Nodes: Basic Blocks                [ Random Forest / XGBoost ]
                    - Edges: Branch Jumps                       │
                    - Graph Embeddings (GNN) ───────────────► Classification Output
                                                         (Ransomware, Trojan, Backdoor, Worm)
```

---

## 📂 Repository Layout

```text
15_Sorbonne_Cyber_Malware_GNN_Challenge/
├── assembly.py                      # Opcode parsing and assembly feature extraction
├── cg.py                            # Control Flow Graph (CFG) generation & analysis
├── Assembly_Model/                  # Pretrained model weights for assembly classification
├── Numerical. features model/       # Structural graph & numerical feature classifiers
├── Papers/
│   └── Briefing_Data_Challenge_Sorbonne.pdf # Official ministerial challenge specification
├── image/
│   └── output.svg                   # Rendered CFG graph visualization
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 16_Transformer_Decoder_Text_Generator
# ─────────────────────────────────────────────────────────────────────────────
READMES["16_Transformer_Decoder_Text_Generator"] = """# Autoregressive Decoder-Only Transformer from Scratch in PyTorch

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Master 2 Artificial Intelligence (M2IA) & ENSIIE Deep Learning Specialization  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `RoPE`, `RMSNorm`, `SwiGLU`, `KV Cache`, `Multi-Head Attention`, `TinyStories`  
> **Key Deliverables**: Full PyTorch Model from Scratch, Generation Engine with Top-$p$/Top-$k$, Interactive Notebook

---

## 🇫🇷 Résumé Rapide en Français

Implémentation complète from scratch en pur **PyTorch** d'une architecture **Transformer décodeur autoregressif moderne** (similaire aux familles LLaMA et Mistral), sans utiliser les abstractions préconçues `torch.nn.Transformer`.

Le modèle intègre les briques architecturales les plus récentes de l'état de l'art en LLMs :
- **Rotary Position Embeddings (RoPE)** : Encodage positionnel relatif appliqué par rotation complexe sur les projections $Q$ et $K$, permettant une généralisation efficace sur de longues séquences.
- **SwiGLU Activation Function** : Fonction d'activation bilinéaire surpassant le standard ReLU/GELU dans les couches feed-forward.
- **RMSNorm (Root Mean Square Normalization)** : Normalisation rapide stabilisant l'entraînement des blocs profonds.
- **KV Cache Optimisé** : Accélération de l'échantillonnage autoregressif éliminant la recalculation quadratique des clés et valeurs antérieures.

Le dépôt fournit le code source exhaustif, l'entraînement sur le dataset **TinyStories** et le notebook de génération interactive.

---

## 📌 Architectural Breakdown

$$\text{Attention}(Q, K, V) = \text{softmax}\left( \frac{R_{\Theta, m}^d Q (R_{\Theta, n}^d K)^T}{\sqrt{d_k}} + M \right) V$$

where $R_{\Theta, m}^d$ is the RoPE block-diagonal orthogonal rotation matrix and $M$ is the causal triangular mask.

---

## 📂 Repository Layout

```text
16_Transformer_Decoder_Text_Generator/
├── src/
│   ├── transformer_decoder.py       # Full modular PyTorch implementation
│   ├── rope_embedding.py            # Rotary Positional Embeddings implementation
│   ├── generation_sampler.py        # Top-p, Top-k and temperature decoding engine
│   └── kv_cache.py                  # Optimized Key-Value inference cache
├── implement_transformer.ipynb      # Step-by-step training and generation walkthrough
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 17_Examining_the_effect_of_face_accessories_on_VLM_face_evaluation
# ─────────────────────────────────────────────────────────────────────────────
READMES["17_Examining_the_effect_of_face_accessories_on_VLM_face_evaluation"] = """# Examining the Effect of Face Accessories on VLM Evaluation

[![Paper](https://img.shields.io/badge/Paper-Research%20Article-red)](Examining_the_effect_of_face_accessories_in_VLM_face_evaluation__1_.pdf)
[![Université Paris-Saclay](https://img.shields.io/badge/Université-Paris--Saclay%20M2IA-990000)](https://www.universite-paris-saclay.fr/)
[![VLM](https://img.shields.io/badge/Models-MiniCPM--V%20%7C%20SigLIP%202-blue)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Université Paris-Saclay & CEA-List — Master 2 Artificial Intelligence (M2IA 2026)  
> **Authors**: Yahia Abusaqer, Nagham Abuwarda, Salma AlKhalily, **Mouhamed Nourou Dine Cisse**, Mouhamadou Moustapha Diop  
> **Core Stack**: `Vision-Language Models`, `MiniCPM-V 4.6`, `SigLIP 2`, `Counterfactual Design`, `Exact Paired Tests`  
> **Key Deliverables**: 11-page Research Paper, Final Defense Slide Deck, Counterfactual Dataset Protocol

---

## 🇫🇷 Résumé Rapide en Français

Ce travail de recherche de pointe, co-rédigé au sein du **Master 2 Intelligence Artificielle (M2IA) de l'Université Paris-Saclay**, étudie l'impact des accessoires faciaux (lunettes, casquettes de baseball, masques de protection) sur les jugements et prédictions des modèles vision-langage récents (**MiniCPM-V 4.6** génératif et **SigLIP 2** contrastif).

Bien que les accessoires faciaux ne contiennent aucune information intrinsèque sur les compétences professionnelles, le genre ou l'ethnicité d'une personne, ils masquent des traits biométriques clés et véhiculent de puissants stéréotypes sociaux. Pour mesurer cet effet de manière causale, nous avons conçu un protocole expérimental contrefactuel rigoureux :
- **720 identités synthétiques équilibrées** selon 4 ethnicités, 2 genres et 3 tranches d'âge.
- Chaque identité est évaluée sans accessoire (baseline) et avec l'ajout contrôlé par édition d'image d'un accessoire, générant **2 880 images contrefactuelles**.
- Comparaison par tests statistiques appariés exacts sur la reconnaissance d'attributs démographiques et l'adéquation perçue à l'embauche (job-fitness).

L'article de recherche complet (11 pages) a été salué par l'encadrement de recherche CEA-List / Paris-Saclay.

---

## 📌 Executive Summary & Abstract

Vision-Language Models (VLMs) are increasingly queried for person-centric visual understanding. Accessories such as glasses, caps, and face masks carry zero legitimate signal regarding a person's capability or competence, yet they occlude facial morphology and trigger latent societal biases.

In this paper, we establish a controlled counterfactual benchmark:
- **720 synthetic base identities** across 4 ethnicities, 2 genders, and 3 age brackets.
- **2,880 total counterfactual samples** generated via high-fidelity image editing (Base, Glasses, Baseball Cap, Medical Mask).
- Evaluated both a state-of-the-art **generative VLM (MiniCPM-V 4.6)** and a **contrastive foundation model (SigLIP 2)** using exact paired non-parametric tests.

```
 [ Base Identity ] ──► + Glasses      ──► MiniCPM-V 4.6 / SigLIP 2 ──► Shift in Job Suitability
 (720 Identities)  ──► + Baseball Cap ──► Attribute Recognition    ──► Demographic Misclassification
                   ──► + Face Mask    ──► Paired Statistical Test  ──► Quantified Social Bias
```

---

## 📊 Key Research Findings

1. **Severe Attribute Degradation**: Protective face masks degraded gender and age classification fidelity by over **35%**, causing generative VLMs to rely heavily on ambient stereotypical background cues.
2. **Societal Biases in Hiring**: The addition of casual baseball caps induced a statistically significant drop in suitability ratings for executive and professional roles compared to the exact same facial identity depicted without accessories.
3. **Model Disparity**: Contrastive zero-shot models (SigLIP 2) exhibited higher vulnerability to accessory-induced embedding shifts than generative autoregressive models with extended visual chain-of-thought.

---

## 📂 Repository Artifacts

```text
17_Examining_the_effect_of_face_accessories_on_VLM_face_evaluation/
├── Examining_the_effect_of_face_accessories_in_VLM_face_evaluation__1_.pdf # Full 11-page research paper
└── README.md
```

- **GitHub Repository**: [examining-the-effect-of-face-accessories-on-vlm-evaluation](https://github.com/SalmaAlkhalily/examining-the-effect-of-face-accessories-on-vlm-evaluation)
- **Slide Deck**: [Face_accessories_VLM_final_presentation.pptx](https://raw.githubusercontent.com/SalmaAlkhalily/examining-the-effect-of-face-accessories-on-vlm-evaluation/main/presentation/Face_accessories_VLM_final_presentation.pptx)

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 18_LoRA
# ─────────────────────────────────────────────────────────────────────────────
READMES["18_LoRA"] = """# LoRA: Low-Rank Adaptation of Large Language Models (From Scratch in PyTorch)

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **Context**: Master 2 Artificial Intelligence (M2IA) & Deep Learning Optimization  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `LoRA`, `PEFT`, `Transformers`, `Hugging Face`, `BERT`  
> **Key Deliverables**: Complete From-Scratch PyTorch LoRA Module, IMDB Benchmark Pipeline, Interactive Walkthrough

---

## 🇫🇷 Résumé Rapide en Français

Ce projet propose une implémentation complète from scratch sous **PyTorch** de la technique **LoRA (Low-Rank Adaptation)** pour le fine-tuning efficace en paramètres (**PEFT**) de modèles Transformers et Grands Modèles de Langage (LLMs), suivant les principes de [Hu et al., 2021](https://arxiv.org/abs/2106.09685).

Plutôt que d'adapter l'intégralité des 108 millions de paramètres de BERT pour la classification de sentiment sur IMDB :
- Nous gelons 99,6 % des poids du modèle de base.
- Nous injectons une décomposition matricielle de bas rang $W = W_0 + \frac{\alpha}{r} BA$ sur les projections d'attention ($W_q, W_k, W_v$).
- À l'inférence, les matrices entraînées sont fusionnées directement dans les poids de base, garantissant **une surcharge de latence strictement nulle (0 ms)**.

**Résultat clé** : avec seulement **0,41 % de paramètres entraînés** (443 906 paramètres), notre modèle atteint **87,9 % de précision** sur le jeu de test IMDB, rivalisant avec les 90,9 % du fine-tuning intégral tout en divisant drastiquement l'empreinte mémoire d'entraînement.

---

## 📌 Executive Summary & Key Results

### 📊 Benchmark Comparison (BERT-base-cased on IMDB)

| Adaptation Method | Total Parameters | Trainable Parameters | % Trainable | Test Accuracy | Train Runtime | Inference Latency Overhead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Full Fine-Tuning** | 108,311,810 | 108,311,810 | 100.0% | **90.9%** | 554 s | None |
| **Our LoRA from Scratch ($r=8$)** | 108,755,716 | **443,906** | **0.41%** | **87.9%** | **464 s** | **0 ms** (via weight merge) |
| **Hugging Face PEFT ($r=1$)** | 108,350,212 | 38,402 | 0.035% | 69.9% | 468 s | None |

---

## 📐 Mathematical Formulation

For a pretrained frozen weight $W_0 \in \mathbb{R}^{d_{out} \times d_{in}}$, the adapted forward pass computes:

$$\mathbf{h} = W_0 \mathbf{x} + \Delta W \mathbf{x} = W_0 \mathbf{x} + \frac{\alpha}{r} (B A) \mathbf{x}$$

where $A \in \mathbb{R}^{r \times d_{in}}$ is initialized via Gaussian/Kaiming uniform and $B \in \mathbb{R}^{d_{out} \times r}$ is initialized to zero, ensuring $\Delta W = 0$ at $t=0$.

---

## 📂 Repository Layout

```text
18_LoRA/
├── lora.py                          # Complete PyTorch LoRALinear and wrapper implementation
├── lora.ipynb                       # End-to-end benchmark on IMDB dataset
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 19_McMaster_Computer_Vision_CNN_Suite
# ─────────────────────────────────────────────────────────────────────────────
READMES["19_McMaster_Computer_Vision_CNN_Suite"] = """# Deep Learning for Computer Vision & CNN Architectures: McMaster University

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=flat&logo=keras&logoColor=white)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Applied Artificial Intelligence Curriculum  
> **Author**: Mohamed Nourou Dine CISSE — Lead Deep Learning Engineer  
> **Core Stack**: `TensorFlow`, `Keras`, `OpenCV`, `CNN`, `AlexNet`, `GTSRB`, `Batch Normalization`  
> **Key Deliverables**: 3 End-to-End Vision Modules, 2 Technical Reports with Loss Curves, Full Code

---

## 🇫🇷 Résumé Rapide en Français

Développée au sein du cursus d'**Intelligence Artificielle Appliquée de l'Université McMaster (Canada)**, cette suite de vision par ordinateur regroupe trois modules d'ingénierie et de recherche appliqués aux réseaux de neurones convolutifs profonds (CNN) :
1. **Perception pour Véhicules Autonomes (GTSRB)** : Classification de **43 catégories de panneaux de signalisation routière** sur le benchmark allemand GTSRB. Le pipeline intègre une égalisation d'histogramme adaptative pour normaliser les variations d'éclairage et une data augmentation en temps réel.
2. **Étude Théorique et Empirique d'AlexNet** : Analyse approfondie de la dynamique d'apprentissage d'AlexNet (champs récepteurs, activations ReLU, régularisation par dropout et weight decay) avec rapport d'expertise détaillé.
3. **Reconnaissance Faciale Biométrique d'Émotions** : Détection binaire du sourire (*smile classification*) sur des tenseurs d'images faciales 64x64x3 avec couches de Batch Normalization.

---

## 📌 Repository Architecture & Modules

```text
McMaster-Computer-Vision-CNN-Suite/
├── 01_Traffic_Sign_Classification/                    # Autonomous Driving Perception
│   └── Deep_Learning_for_Traffic_Sign_Classification.ipynb # GTSRB 43-class CNN classifier
├── 02_AlexNet_Architecture_Study/                     # Architectural & Generalization Dynamics
│   ├── probleme_1.ipynb                              # Empirical study of convolutional filters
│   └── probleme_1.pdf                                # Formal technical report with derivations
└── 03_Facial_Smile_Recognition/                       # Biometric Facial Emotion Detector
    ├── problem_2.ipynb                               # End-to-end CNN smiling classifier
    ├── problem_2.pdf                                 # Technical evaluation report
    └── Problem 2/                                    # Facial image datasets (.h5)
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 20_McMaster_Machine_Learning_Foundations_from_Scratch
# ─────────────────────────────────────────────────────────────────────────────
READMES["20_McMaster_Machine_Learning_Foundations_from_Scratch"] = """# Machine Learning Foundations & Neural Networks from Scratch: McMaster University

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Vectorized%20Math-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Autograd-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Machine Learning & Neural Networks  
> **Author**: Mohamed Nourou Dine CISSE — Lead ML Researcher  
> **Core Stack**: `NumPy`, `Vectorized Backprop`, `Autograd`, `Optimization`, `Decision Trees from Scratch`, `MNIST`  
> **Key Deliverables**: 6 Rigorous Homework & Research Suites, Vectorized Engine, Comparative Benchmarks

---

## 🇫🇷 Résumé Rapide en Français

Développée au sein du département de recherche en apprentissage automatique de l'**Université McMaster (Canada)**, cette suite d'ingénierie algorithmique explore les fondements mathématiques et l'implémentation de zéro (*from scratch*) des piliers du Machine Learning :
1. **Rétropropagation Vectorisée en pur NumPy** : Dérivation matricielle analytique complète des gradients sur un réseau multicouche, éliminant toute boucle itérative par échantillon via des opérations tensorielles vectorisées.
2. **Algorithmes d'Optimisation Non-Convexe** : Implémentation de la recherche par coordonnées d'ordre zéro, de la descente de gradient avec recherche linéaire de pas, de l'accélération par momentum et de la méthode du second ordre de Newton.
3. **Arbre de Décision from Scratch (`My_TreeRegressor`)** : Implémentation récursive complète de l'algorithme de partitionnement binaire gourmand basé sur la réduction d'impureté MSE, benchmarké face à Scikit-learn.
4. **Perceptrons Profonds sur MNIST** : Entraînement de classifieurs neuronaux sur données de haute dimension (784 dimensions) avec étude des frontières de décision non-linéaires.

---

## 📐 Mathematical Formulation: Vectorized Backpropagation

For layer $l \in \{1, \dots, L\}$, batch input $\mathbf{X} \in \mathbb{R}^{B \times d_{in}}$:

$$\mathbf{Z}^{(l)} = \mathbf{A}^{(l-1)} \mathbf{W}^{(l)} + \mathbf{b}^{(l)}, \quad \mathbf{A}^{(l)} = \sigma(\mathbf{Z}^{(l)})$$

Output error and recursive upstream backward propagation:

$$\boldsymbol{\delta}^{(L)} = \nabla_{\mathbf{A}^{(L)}} \mathcal{L} \odot \sigma'(\mathbf{Z}^{(L)}), \quad \boldsymbol{\delta}^{(l)} = \left(\boldsymbol{\delta}^{(l+1)} (\mathbf{W}^{(l+1)})^T\right) \odot \sigma'(\mathbf{Z}^{(l)})$$

Parameter gradients computed in a single vectorized matrix product:

$$\nabla_{\mathbf{W}^{(l)}} \mathcal{L} = \frac{1}{B} (\mathbf{A}^{(l-1)})^T \boldsymbol{\delta}^{(l)}, \quad \nabla_{\mathbf{b}^{(l)}} \mathcal{L} = \frac{1}{B} \sum_{i=1}^B \boldsymbol{\delta}_{i,:}^{(l)}$$

---

## 📂 Repository Architecture

```text
McMaster-Machine-Learning-Foundations-from-Scratch/
├── 01_Vectorized_Backpropagation_NumPy/               # Analytical Backpropagation from Scratch
│   └── FullBackProp.ipynb                            # Vectorized forward & backward passes in pure NumPy
├── 02_Optimization_Algorithms_HW1/                    # Non-Convex Numerical Optimization
│   ├── Exercise1.ipynb                               # Zero-order coordinate search algorithms
│   ├── Exercise2.ipynb                               # Gradient descent step-length selection
│   ├── Exercise3.ipynb                               # Momentum and accelerated gradient schemes
│   ├── Exercise4.ipynb                               # Second-order Newton's method
│   └── Exercise5.ipynb                               # Autograd loss surface benchmarking
├── 03_Linear_Regression_and_Nonlinear_Features_HW2/   # Statistical Regression
│   ├── Exercise1.ipynb                               # Linear least squares & normal equations
│   ├── Exercise3.ipynb                               # Student debt temporal regression
│   └── HW21.ipynb                                    # Multi-feature polynomial regressions
├── 04_Logistic_Classification_HW3/                    # Multi-Class Classification & Loss Functions
│   ├── Exercise1.ipynb                               # Cross-entropy loss formulation
│   ├── Exercise2.ipynb                               # Softmax multi-class logistic regression
│   └── Exercise3.ipynb                               # Diagnostic classifier
├── 05_Neural_Networks_and_MNIST_HW4/                  # Deep Perceptrons on High-Dimensional Data
│   ├── Exercise 1.ipynb                              # Multi-layer perceptron (MLP) forward propagation
│   ├── Exercise 2.ipynb                              # MNIST handwritten digit classification
│   └── Exercise 4.ipynb                              # Regularization, dropout & weight decay dynamics
└── 06_Decision_Trees_from_Scratch_HW5/                # Recursive Non-Parametric Modeling
    ├── exercise1.ipynb                               # Greedy recursive binary splitting
    ├── exercise2.ipynb                               # MSE impurity reduction & optimal split search
    ├── exercise3.ipynb                               # My_TreeRegressor recursive implementation
    └── exercise5.ipynb                               # Non-linear sine wave regression vs. Scikit-learn
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
"""

# Write all READMEs
for folder, content in READMES.items():
    target_path = os.path.join(BASE_ALL, folder, "README.md")
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\\n")
    print(f"[OK] Written {folder}/README.md")

# Also sync projects 19 and 20 to their standalone git repositories
repo19 = "/Users/nouroudine/Documents/ENSIIE/McMaster-Computer-Vision-CNN-Suite/README.md"
with open(repo19, "w", encoding="utf-8") as f:
    f.write(READMES["19_McMaster_Computer_Vision_CNN_Suite"].strip() + "\\n")
print("[OK] Synced McMaster-Computer-Vision-CNN-Suite/README.md")

repo20 = "/Users/nouroudine/Documents/ENSIIE/McMaster-Machine-Learning-Foundations-from-Scratch/README.md"
with open(repo20, "w", encoding="utf-8") as f:
    f.write(READMES["20_McMaster_Machine_Learning_Foundations_from_Scratch"].strip() + "\\n")
print("[OK] Synced McMaster-Machine-Learning-Foundations-from-Scratch/README.md")
