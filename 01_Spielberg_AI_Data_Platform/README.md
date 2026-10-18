# Spielberg AI Platform: Data Centralization & Multi-Agent Orchestration

> **Cadre institutionnel** : Prodigious France / Publicis Groupe (2026)  
> **Formation** : ENSIIE & Université Paris-Saclay (Double diplôme, Master 2 IA)  
> **Auteur** : Mohamed Nourou Dine CISSE — Élève-ingénieur & Développeur IA / Data  
> **Domaine** : `Enterprise AI & Multi-Agent Systems`  
> **Technologies** : `Python` `FastAPI` `LangGraph` `Multi-Agent Systems` `RAG` `PostgreSQL` `Docker` `Docker Compose`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet a été réalisé lors de mon stage d'ingénieur chez **Prodigious France (Publicis Groupe)**. La mission principale portait sur la fédération et l'unification des données opérationnelles et techniques dispersées au sein de l'agence, couplée à la conception d'un système d'automatisation basé sur des agents d'intelligence artificielle autonomes.

Le dépôt regroupe l'ensemble des livrables techniques, les schémas d'architecture LangGraph, les modules d'ingestion et de base de données PostgreSQL, l'API FastAPI, ainsi que le rapport de stage complet (54 pages) et les supports de soutenance.

---

## 🏗️ Architecture & Composants Développés

```text
01_Spielberg_AI_Data_Platform/
├── architecture/
│   ├── docker-compose.yml           # Déploiement multi-conteneurs (PostgreSQL, services)
│   ├── Dockerfile                   # Image d'exécution des microservices
│   ├── langgraph.json               # Configuration des graphes multi-agents LangGraph
│   ├── orchestrator_graph.png       # Diagramme du flux d'orchestration
│   └── supervisor_graph.png         # Diagramme du flux de supervision multi-agents
├── core_backend/
│   ├── 001_init_altair_roar_oneclick.sql # Script SQL d'initialisation du schéma relationnel
│   ├── spielberg_postgres.py        # Gestionnaire de connexion et requêtes PostgreSQL
│   ├── migrate_mocks_to_postgres.py # Script de migration et chargement des données
│   └── services_data.py             # Modélisation des données de services de l'agence
├── code/
│   ├── FastAPI/                     # Microservice FastAPI (endpoints d'interrogation)
│   │   ├── main.py
│   │   ├── pyproject.toml
│   │   └── app/
│   │       ├── app.py
│   │       └── schema.py
│   ├── RAG/
│   │   └── chunking.py              # Stratégie de découpage sémantique pour l'indexation RAG
│   └── roadmap_stage.html           # Frise chronologique interactive du projet
├── reports/
│   ├── Rapport_de_Stage_Spielberg_2026.pdf # Rapport complet de stage d'ingénieur (54 pages)
│   └── rapport_source.tex           # Sources LaTeX du rapport
└── presentations/
    ├── Soutenance_Spielberg.pdf     # Slides de soutenance finale (Prodigious / ENSIIE)
    ├── Presentation_Stage_ENSIIE.pdf# Présentation institutionnelle
    └── soutenance_source.tex        # Sources LaTeX de la présentation
```

### Détail des Réalisations :
1. **Modélisation & Centralisation PostgreSQL** :
   - Schéma relationnel adapté aux flux opérationnels multi-agences (`001_init_altair_roar_oneclick.sql`).
   - Module de connexion robuste et scripts de migration automatisée (`spielberg_postgres.py`, `migrate_mocks_to_postgres.py`).
2. **Orchestration Multi-Agents (LangGraph)** :
   - Conception de workflows agents sous LangGraph : un **Superviseur** qui route les intentions utilisateur et un **Orchestrateur** coordonnant l'exécution séquentielle/parallèle des sous-tâches opérationnelles.
3. **Pipeline RAG & Chunking Sémantique** :
   - Implémentation du chunking contextuel avec métadonnées (`chunking.py`) pour alimenter les bases vectorielles sans rupture de contexte technique.
4. **Exposition Microservices (FastAPI)** :
   - Endpoints REST documentés avec validation Pydantic pour intégrer les réponses des agents dans les outils internes.

---

## 📄 Livrables & Preuves Académiques

- 📄 **Rapport de Stage d'Ingénieur (54 pages)** : [`reports/Rapport_de_Stage_Spielberg_2026.pdf`](reports/Rapport_de_Stage_Spielberg_2026.pdf)
- 📊 **Support de Soutenance** : [`presentations/Soutenance_Spielberg.pdf`](presentations/Soutenance_Spielberg.pdf)
- 📐 **Diagramme d'Orchestration** : [`architecture/orchestrator_graph.png`](architecture/orchestrator_graph.png)
- 📐 **Diagramme de Supervision** : [`architecture/supervisor_graph.png`](architecture/supervisor_graph.png)

---

## 🚀 Exécution & Déploiement

### 1. Démarrage de la base de données avec Docker
```bash
cd architecture
docker compose up -d
```

### 2. Migration et initialisation des données PostgreSQL
```bash
python core_backend/migrate_mocks_to_postgres.py
```

### 3. Lancement de l'API FastAPI
```bash
cd code/FastAPI
uvicorn app.app:app --reload --port 8000
```
La documentation interactive est accessible sur `http://localhost:8000/docs`.

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-mahy](https://github.com/nourou-dine-mahy)
