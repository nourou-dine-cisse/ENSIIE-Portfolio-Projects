# ETLia: AI-Driven Automated ETL SaaS Platform

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

> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).

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

---

## 🇫🇷 Résumé Rapide en Français

**ETLia** est une plateforme SaaS d'ETL (Extract, Transform, Load) no-code et assistée par l'intelligence artificielle, développée dans le cadre du **Challenge Entreprendre ENSIIE**, où nous avons remporté le **1er Prix (Grand Prix du Jury)**. 

Le constat de départ était clair : les PME et équipes métiers perdent un temps considérable à nettoyer, aligner et charger des fichiers de données hétérogènes (fichiers Excel mal formatés, encodages corrompus, colonnes manquantes). Avec ETLia, l'utilisateur dépose simplement ses fichiers : notre moteur IA profile la structure, détecte automatiquement les anomalies et infère le mapping sémantique vers la base de données cible.

J'ai piloté la co-fondation, le design du frontend en **React / TypeScript / TailwindCSS**, et le développement des moteurs de profiling et de transformation en **Python / Pandas**.

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n
