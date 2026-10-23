# SunSéjour Datamart: Production-Grade ETL Pipeline & Star Schema

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
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n