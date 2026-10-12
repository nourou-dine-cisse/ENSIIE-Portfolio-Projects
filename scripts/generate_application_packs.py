import os
import subprocess

ALL_PROJ_DIR = os.path.abspath("All projects")
PACKS_DIR = os.path.join(ALL_PROJ_DIR, "candidatures_pretes")
os.makedirs(PACKS_DIR, exist_ok=True)

configs = [
    {
        "filename": "Candidature_AI_Machine_Learning_Engineer.md",
        "profil": "ai",
        "entreprise": "[Entreprise Cible — Ex: Mistral AI / Google / Meta]",
        "poste": "Stagiaire R&D Machine Learning & LLM (PFE 6 mois)",
        "lang": "fr"
    },
    {
        "filename": "Candidature_Data_Engineer.md",
        "profil": "de",
        "entreprise": "[Entreprise Cible — Ex: Datadog / Databricks / Snowflake]",
        "poste": "Stagiaire Data Engineer & Cloud Pipelines (PFE 6 mois)",
        "lang": "fr"
    },
    {
        "filename": "Candidature_Quantitative_Developer_Finance.md",
        "profil": "quant",
        "entreprise": "[Entreprise Cible — Ex: BNP Paribas / Société Générale / QRT]",
        "poste": "Stagiaire Quantitative Developer / Analyst (PFE 6 mois)",
        "lang": "fr"
    },
    {
        "filename": "Candidature_Data_Scientist.md",
        "profil": "ml",
        "entreprise": "[Entreprise Cible — Ex: Publicis / TotalEnergies / BCG]",
        "poste": "Stagiaire Data Scientist — Séries Temporelles & Prédiction (PFE 6 mois)",
        "lang": "fr"
    },
    {
        "filename": "Candidature_Biostatistician_Healthcare.md",
        "profil": "biostat",
        "entreprise": "[Entreprise Cible — Ex: Sanofi / Servier / Institut Curie]",
        "poste": "Stagiaire Biostatisticien & Data Scientist Santé (PFE 6 mois)",
        "lang": "fr"
    },
    {
        "filename": "Candidature_International_AI_Engineer_English.md",
        "profil": "ai",
        "entreprise": "[Target Company — Ex: Google DeepMind / OpenAI / Cohere]",
        "poste": "Research Engineer Intern — AI & Data Systems (6 Months)",
        "lang": "en"
    }
]

for cfg in configs:
    out_path = os.path.join(PACKS_DIR, cfg["filename"])
    cmd = [
        "python3",
        os.path.join(ALL_PROJ_DIR, "automate_candidatures.py"),
        "--profil", cfg["profil"],
        "--entreprise", cfg["entreprise"],
        "--poste", cfg["poste"],
        "--lang", cfg["lang"],
        "--output", out_path
    ]
    subprocess.run(cmd, check=True)
    print(f"[OK] Généré : {out_path}")

# Generate GitHub Profile README for nourou-dine-mahy
profile_readme_path = os.path.join(ALL_PROJ_DIR, "GITHUB_PROFILE_README.md")
profile_content = """# Hi there, I'm Mohamed Nourou Dine CISSE 👋

### Applied Mathematics & Artificial Intelligence Engineer
🎓 **ENSIIE** (Évry-Courcouronnes, France) • 🍁 **McMaster University** (Ontario, Canada)  
🎯 **Actively seeking a 6-month End-of-Studies Internship (PFE)** in AI / Machine Learning / Data Engineering / Quantitative Finance starting May/June 2026.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-181717?style=flat-square&logo=github)](https://github.com/nourou-dine-mahy)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-EA4335?style=flat-square&logo=gmail)](mailto:mouhamed.nouroudine.cisse@gmail.com)

---

## ⚡ What I Do & Core Technical Highlights

- 🤖 **Enterprise AI & RAG Agents** : Architected an operational data hub and multi-agent RAG pipeline at **Publicis Groupe / Prodigious France** (FastAPI, chunking, vector embeddings).
- 🏆 **Startup Co-Founder & Winner** : Co-founded **ETLia**, an AI-assisted automated ETL SaaS that won **1st place in the ENSIIE Entrepreneurship Challenge** (React/TypeScript + Python/Streamlit).
- 📈 **Time Series Forecasting & Credit Scoring** : Built multivariate forecasting engines (SARIMAX, VAR, DLTS) and calibrated credit risk models at **Infinity Analytics / Gainde 2000**.
- 💹 **Quantitative Computing** : Implemented a high-performance C++17 Black-Scholes PDE solver (finite difference explicit/implicit schemes) with real-time SDL2 payoff graphics.
- 🔤 **Deep NLP & Transformers** : Researched distributional semantics (Word2Vec, FastText), 1D CNN/Transformer classifiers, and hybrid BiLSTM-CNN for Named Entity Recognition.

---

## 🛠️ Tech Stack & Toolbox

| Domain | Technologies |
| :--- | :--- |
| **Languages** | Python, C++, C, R, TypeScript, JavaScript, SQL, OCaml, Java |
| **AI / Machine Learning** | PyTorch, Transformers, Scikit-Learn, Statsmodels, RAG, Word2Vec, FastText, GLM |
| **Data Engineering** | Docker, Docker Compose, Pandas, NumPy, FastAPI, Streamlit, Star Schema Datamarts |
| **Frontend & Visualization** | React, Vite, TailwindCSS, Matplotlib, Seaborn, SDL2 |
| **Tools & Environments** | Linux, Git, LaTeX, Make, Jupyter, Valgrind, Bash |

---

## 🌟 Featured Projects & Documentation

| Project | Highlights | Deliverables |
| :--- | :--- | :--- |
| **Projet Spielberg** | Enterprise AI platform unifying cross-agency data with RAG agents | [54-page Thesis](https://github.com/nourou-dine-mahy) • [22-slide Deck](https://github.com/nourou-dine-mahy) |
| **ETLia AI Data Wizard** | 1st Prize Winner — AI-driven automated no-code data profiling and loading | React Frontend & Python Engine |
| **SunSéjour ETL Pipeline** | Containerized tourism data pipeline with dimensional star-schema datamart | Technical Architecture Report |
| **Black-Scholes PDE Solver** | Modern C++17 options pricing engine solving Black-Scholes via finite differences | Scientific Research Paper & SDL2 GUI |
| **Cancer Survival Modeling** | Biostatistical survival inference on the 2000+ patient METABRIC cohort in R | Research Paper & ROC-AUC Benchmarks |

---

## 📬 Let's Connect!
- **Email** : [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com)
- **Phone** : +33 7 65 60 09 97
- **Location** : Paris, France (Available for nationwide and international mobility)
"""

with open(profile_readme_path, "w", encoding="utf-8") as f:
    f.write(profile_content)
print(f"[OK] GITHUB_PROFILE_README.md généré : {profile_readme_path}")
