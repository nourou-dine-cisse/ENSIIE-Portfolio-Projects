# Spielberg AI Platform: Data Centralization & Multi-Agent Orchestration

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

> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).

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

---

## 🇫🇷 Résumé Rapide en Français

Durant mon stage d'ingénieur au sein de **Prodigious France (Publicis Groupe)**, j'ai conçu et déployé la plateforme **Spielberg**, une infrastructure centralisée unifiant les données opérationnelles et techniques dispersées de multiples agences (Altair, Roar, OneClick). 

Au-delà de l'unification relationnelle sous **PostgreSQL**, le cœur de mon travail a porté sur l'orchestration de systèmes multi-agents sous **LangGraph** articulés autour d'un **Superviseur** d'intentions et d'un **Orchestrateur** de sous-tâches opérationnelles. J'ai également implémenté un pipeline **RAG** (Retrieval-Augmented Generation) complet avec stratégie de découpage sémantique contextuel (`chunking.py`), optimisé pour conserver l'intégrité technique des documents internes.

Ce travail a abouti à un rapport d'ingénieur de **54 pages**, une soutenance de **22 slides** devant jury académique et d'entreprise, et a posé les bases techniques d'une future spin-off IA data interne.

---

## 👤 Author & Academic Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n
