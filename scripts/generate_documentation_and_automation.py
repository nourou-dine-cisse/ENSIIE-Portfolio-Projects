import os
import json

ALL_PROJ_DIR = os.path.abspath("All projects")

catalog = [
    {
        "id": "01_spielberg",
        "folder": "01_Spielberg_AI_Data_Platform",
        "title_fr": "Plateforme Spielberg : Centralisation des Données & Agents IA (Publicis / Prodigious)",
        "title_en": "Spielberg Platform: Enterprise Data Centralization & AI RAG Agents",
        "category": "Enterprise AI & Data Engineering",
        "institution": "Publicis Groupe / Prodigious France",
        "year": "2026",
        "role": "Stagiaire Ingénieur IA & Data Engineering",
        "technologies": ["Python", "FastAPI", "RAG", "LLM", "Vector Databases", "Data Engineering", "AsyncIO", "Docker"],
        "keywords": ["rag", "llm", "agent", "fastapi", "api", "data platform", "centralisation", "vector search", "publicis", "embeddings", "backend"],
        "pitch_fr": "Conception et déploiement d'une plateforme d'entreprise unifiant les données opérationnelles des filiales et orchestrant des agents IA via un pipeline RAG haute précision avec FastAPI.",
        "pitch_en": "Engineered an enterprise platform unifying cross-agency operational data and orchestrating AI agents through a high-precision RAG pipeline built on FastAPI.",
        "star_bullet_points_fr": [
            "Conception d'une plateforme unifiée (FastAPI) pour l'ingestion, l'indexation et la centralisation des flux de données opérationnelles de plusieurs agences.",
            "Développement d'un pipeline RAG (Retrieval-Augmented Generation) avec chunking sémantique optimisé et filtrage par métadonnées pour des agents IA spécialisés.",
            "Rédaction d'un rapport de stage de 54 pages et présentation devant jury académique et industriel (soutenance de 22 slides)."
        ],
        "star_bullet_points_en": [
            "Architected an enterprise data hub using FastAPI to centralize operational data feeds across Publicis agencies.",
            "Engineered a production-ready RAG pipeline featuring optimized semantic chunking and metadata-aware vector retrieval for specialized AI agents.",
            "Authored a comprehensive 54-page engineering thesis and defended before an academic/corporate jury with 22 presentation slides."
        ],
        "reports": ["reports/Rapport_de_Stage_Spielberg_2026.pdf"],
        "presentations": ["presentations/Soutenance_Spielberg.pdf", "presentations/Presentation_Stage_ENSIIE.pdf"]
    },
    {
        "id": "02_etlia",
        "folder": "02_ETLia_AI_Data_Wizard",
        "title_fr": "ETLia : Plateforme ETL Augmentée par l'IA (Lauréat Challenge Entreprendre)",
        "title_en": "ETLia: AI-Driven No-Code ETL Platform (Winner Challenge Entreprendre)",
        "category": "Data Engineering & Fullstack AI SaaS",
        "institution": "ENSIIE (Challenge Entreprendre)",
        "year": "2025-2026",
        "role": "Co-fondateur & Développeur Lead AI / Data",
        "technologies": ["React", "TypeScript", "Vite", "TailwindCSS", "Python", "Streamlit", "Pandas", "ETL", "AI Assistants"],
        "keywords": ["etl", "saas", "startup", "react", "typescript", "data pipeline", "fullstack", "ui", "streamlit", "ingestion", "wizard"],
        "pitch_fr": "Co-fondation d'une solution SaaS d'ETL assistée par IA automatisant le profilage, le nettoyage et le chargement de données hétérogènes. Projet récompensé par le 1er prix du Challenge Entreprendre ENSIIE.",
        "pitch_en": "Co-founded an AI-assisted ETL SaaS streamlining profiling, data cleaning, and automated schema mapping. Won 1st place at ENSIIE Entrepreneurship Challenge.",
        "star_bullet_points_fr": [
            "Co-fondation et développement de la plateforme ETLia, récompensée par le 1er prix du Challenge Entreprendre ENSIIE.",
            "Développement d'une interface web moderne (React/TypeScript/Tailwind) et de moteurs de transformation de données en Python/Streamlit.",
            "Automatisation du mapping de schéma et de la détection d'anomalies de données à l'aide d'assistants IA intégrés."
        ],
        "star_bullet_points_en": [
            "Co-founded and engineered ETLia, winning 1st place in the ENSIIE Entrepreneurship Challenge.",
            "Built a modern React/TypeScript/Tailwind dashboard coupled with Python/Streamlit data processing engines.",
            "Automated schema mapping and data anomaly detection utilizing integrated AI models."
        ],
        "reports": [],
        "presentations": []
    },
    {
        "id": "03_sunsejour_etl",
        "folder": "03_SunSejour_ETL_Datamart",
        "title_fr": "Pipeline ETL de Production & Modélisation Datamart SunSéjour",
        "title_en": "Production-Grade ETL Pipeline & Star-Schema Datamart SunSéjour",
        "category": "Data Engineering & Data Warehousing",
        "institution": "Projet ENSIIE",
        "year": "2025-2026",
        "role": "Data Engineer Lead",
        "technologies": ["Python", "Docker", "Docker Compose", "Pandas", "Star Schema", "Data Validation", "Logging", "Bash"],
        "keywords": ["etl", "pipeline", "docker", "data engineer", "datamart", "star schema", "data warehouse", "pandas", "validation", "production"],
        "pitch_fr": "Conception d'un pipeline ETL conteneurisé sous Docker assurant l'ingestion, le nettoyage rigoureux, et la modélisation dimensionnelle (schéma en étoile) des flux d'excursions et transferts touristiques.",
        "pitch_en": "Designed a containerized Docker ETL pipeline managing ingestion, rigorous validation, and star-schema dimensional modeling for tourism operations.",
        "star_bullet_points_fr": [
            "Création d'un pipeline de bout en bout (Extract, Transform, Load) traitant des fichiers transactionnels hétérogènes (.xls, .xlsx).",
            "Mise en place d'une modélisation dimensionnelle en étoile (tables de faits et dimensions) pour le calcul automatisé du CA et des marges.",
            "Conteneurisation complète avec Docker et Docker Compose, intégrant des scripts de validation de données et de traçabilité des anomalies."
        ],
        "star_bullet_points_en": [
            "Engineered an end-to-end ETL pipeline processing heterogeneous transactional records with rigorous quality checks.",
            "Designed a dimensional star schema (facts & dimensions) automating revenue, margin, and operational metrics calculation.",
            "Containerized deployment using Docker & Docker Compose with full anomaly logging and validation suite."
        ],
        "reports": ["reports/Rapport_Datamart_SunSejour.pdf", "reports/Guide_Utilisation_ETL_SunSejour.pdf"],
        "presentations": []
    },
    {
        "id": "04_infinity_analytics",
        "folder": "04_Infinity_Analytics_Time_Series_ML",
        "title_fr": "Séries Temporelles & Scoring Prédictif ML (Infinity Analytics / Gainde 2000)",
        "title_en": "Financial Time Series Forecasting & Credit Scoring ML (Infinity Analytics)",
        "category": "Applied Machine Learning & Time Series",
        "institution": "Gainde 2000 / Bangath Systems",
        "year": "2024-2025",
        "role": "Stagiaire Data Scientist / ML",
        "technologies": ["Python", "Pandas", "Scikit-Learn", "Statsmodels", "SARIMAX", "VAR", "Deep Learning", "Credit Scoring", "Calibration"],
        "keywords": ["machine learning", "time series", "sarimax", "var", "scoring", "credit", "finance", "forecast", "forecasting", "data science"],
        "pitch_fr": "Modélisation prédictive de séries temporelles financières (SARIMAX, VAR, DLTS) et élaboration de modèles de scoring de crédit avec calibration probabiliste.",
        "pitch_en": "Predictive modeling of financial time series (SARIMAX, VAR, Deep Learning) and development of calibrated credit default risk scoring algorithms.",
        "star_bullet_points_fr": [
            "Modélisation économétrique et stochastique de flux financiers via SARIMA, SARIMAX et VAR (Vector Auto-Regression).",
            "Développement et calibration d'un modèle de scoring d'octroi de crédit (Use Case 7) avec optimisation des courbes de calibration et seuils de décision.",
            "Rédaction d'un rapport de stage complet et soutenance devant jury avec support de présentation de 23 slides."
        ],
        "star_bullet_points_en": [
            "Formulated multivariate econometric forecasting pipelines leveraging SARIMA, SARIMAX, and VAR models.",
            "Built and calibrated a credit default scoring model (Use Case 7) optimizing probability calibration curves and decision thresholds.",
            "Authored full technical internship report and delivered a 23-slide defense presentation."
        ],
        "reports": ["reports/Rapport_de_Stage.pdf", "reports/Rapport_Use_Case_7_Scoring.pdf"],
        "presentations": ["presentations/Presentation_de_Stage.pdf"]
    },
    {
        "id": "05_nlp_representations",
        "folder": "05_NLP_Semantic_Representations_NER",
        "title_fr": "Représentations Sémantiques, Classification & Reconnaissance d'Entités (NER)",
        "title_en": "Semantic Representations, Text Classification & Named Entity Recognition (NER)",
        "category": "Deep Learning & NLP",
        "institution": "ENSIIE (M2IA Master IA)",
        "year": "2025-2026",
        "role": "NLP & Deep Learning Engineer",
        "technologies": ["PyTorch", "Transformers", "Word2Vec", "FastText", "BiLSTM-CNN", "NER", "NLP", "Python", "Bash"],
        "keywords": ["nlp", "pytorch", "transformers", "word2vec", "fasttext", "lstm", "cnn", "ner", "deep learning", "embeddings", "classification"],
        "pitch_fr": "Entraînement et benchmark de représentations sémantiques (Word2Vec, FastText), classification de texte (CNN, Transformers) et reconnaissance d'entités nommées par architecture hybride BiLSTM-CNN.",
        "pitch_en": "Trained and evaluated dense semantic embeddings (Word2Vec, FastText), neural text classifiers (CNN, Transformers), and hybrid BiLSTM-CNN for Named Entity Recognition on French corpora.",
        "star_bullet_points_fr": [
            "Entraînement de modèles de plongements lexicaux (Word2Vec Skip-gram/CBOW, FastText) sur le corpus journalistique français QUAERO.",
            "Implémentation et comparaison d'architectures de classification de texte : Convolutions 1D (CNN) vs modèles Transformers.",
            "Conception d'une architecture neuronale hybride BiLSTM-CNN pour la reconnaissance d'entités nommées (NER) avec rapport de recherche détaillé."
        ],
        "star_bullet_points_en": [
            "Trained dense word representation models (Word2Vec Skip-Gram/CBOW, FastText) on the QUAERO French news corpus.",
            "Implemented and benchmarked deep text classification pipelines comparing 1D CNNs against Transformer architectures.",
            "Engineered a hybrid BiLSTM-CNN neural architecture for Named Entity Recognition (NER) and authored an extensive research report."
        ],
        "reports": ["reports/Report_CISSE_DIOP.pdf", "reports/Rapport_TP_Embeddings.pdf"],
        "presentations": []
    },
    {
        "id": "06_black_scholes",
        "folder": "06_Black_Scholes_PDE_Solver",
        "title_fr": "Solveur EDP Black-Scholes en C++ & Rendu Graphique Temps Réel SDL2",
        "title_en": "C++ Black-Scholes PDE Numerical Solver & Real-Time SDL2 Visualization",
        "category": "Quantitative Finance & Scientific Computing",
        "institution": "ENSIIE (2A PRAV)",
        "year": "2024-2025",
        "role": "Quantitative Developer",
        "technologies": ["C++17", "STL", "Différences Finies", "EDP", "Black-Scholes", "SDL2", "Algorithmique Numérique", "POO"],
        "keywords": ["c++", "finance quantitative", "black scholes", "edp", "pde", "options", "pricing", "greeks", "sdl2", "scientific computing", "quant"],
        "pitch_fr": "Développement en C++ moderne d'un moteur de pricing d'options européennes résolvant l'équation aux dérivées partielles de Black-Scholes par schéma implicite/explicite aux différences finies, avec rendu visuel SDL2.",
        "pitch_en": "Developed a high-performance C++ pricing engine for European options solving the Black-Scholes PDE via finite difference schemes with real-time SDL2 graphics.",
        "star_bullet_points_fr": [
            "Implémentation orientée objet (C++17) d'un solveur numérique pour l'EDP de Black-Scholes par méthode des différences finies (schémas implicite et explicite).",
            "Calcul dynamique des prix de Call/Put et des sensibilités financières (Grecs), avec convergence et analyse des erreurs résiduelles.",
            "Développement d'une interface graphique interactive temps réel avec la bibliothèque SDL2 pour tracer l'évolution temporelle des surfaces de prix."
        ],
        "star_bullet_points_en": [
            "Engineered an object-oriented C++17 numerical solver for the Black-Scholes PDE using explicit and implicit finite-difference schemes.",
            "Computed Call/Put pricing matrices and Greeks sensitivities with rigorous stability and residual error convergence analysis.",
            "Integrated real-time interactive graphic rendering of option payoff curves using the SDL2 library."
        ],
        "reports": ["reports/Rapport_Black_Scholes.pdf"],
        "presentations": []
    },
    {
        "id": "07_breast_cancer_merr",
        "folder": "07_Breast_Cancer_Biostatistics_MERR",
        "title_fr": "Modélisation Statistique & Prédiction de Survie du Cancer du Sein (METABRIC)",
        "title_en": "Biostatistical Survival & Recurrence Modeling on METABRIC Breast Cancer Data",
        "category": "Biostatistics & Machine Learning",
        "institution": "ENSIIE (2A MERR)",
        "year": "2024-2025",
        "role": "Biostatistician & Data Scientist",
        "technologies": ["R", "RMarkdown", "GLM", "Régression Logistique", "Lasso", "Ridge", "Elastic Net", "Sélection de Variables", "Courbes ROC"],
        "keywords": ["r", "statistiques", "biostatistique", "cancer", "metabric", "glm", "regression", "lasso", "ridge", "roc", "sante", "genomique"],
        "pitch_fr": "Étude biostatistique et modélisation binomiale de la survie à 5 ans de patientes atteintes de cancer du sein à partir de données cliniques et d'expression génomique (cohorte METABRIC).",
        "pitch_en": "Biostatistical modeling and binomial classification of 5-year patient survival using clinical and genomic expression profiles from the METABRIC cohort.",
        "star_bullet_points_fr": [
            "Exploration et prétraitement de données génomiques et cliniques haute dimension (cohorte METABRIC de 2000+ patientes).",
            "Ajustement de modèles linéaires généralisés (GLM binomial) et sélection parcimonieuse de covariables (AIC/BIC, régularisation Lasso/Elastic Net).",
            "Évaluation rigoureuse des performances prédictives via courbes ROC-AUC, matrice de confusion et validation croisée."
        ],
        "star_bullet_points_en": [
            "Curated and preprocessed high-dimensional clinical and gene expression features from the 2,000+ patient METABRIC cohort.",
            "Fitted binomial Generalized Linear Models (GLM) with penalized variable selection (Lasso, Elastic Net, Stepwise AIC/BIC).",
            "Evaluated classification performance through cross-validated ROC-AUC analysis, sensitivity/specificity tradeoffs, and calibration."
        ],
        "reports": ["reports/Rapport_Cancer_Survie_MERR.pdf"],
        "presentations": []
    },
    {
        "id": "08_airbnb_ando",
        "folder": "08_Airbnb_NYC_Data_Analysis_ANDO",
        "title_fr": "Analyse Factorielle & Clustering sur le Marché Airbnb New York City",
        "title_en": "Multivariate Analysis & Unsupervised Clustering of Airbnb NYC Listings",
        "category": "Unsupervised Learning & Data Analysis",
        "institution": "ENSIIE (2A ANDO)",
        "year": "2024-2025",
        "role": "Data Analyst / ML",
        "technologies": ["Python", "Scikit-Learn", "Pandas", "Matplotlib", "Seaborn", "ACP (PCA)", "ACC (CCA)", "K-Means", "Clustering Hiérarchique"],
        "keywords": ["analyse de donnees", "clustering", "pca", "acp", "cca", "kmeans", "airbnb", "unsupervised", "data science", "eda"],
        "pitch_fr": "Analyse multidimensionnelle et segmentation du marché locatif new-yorkais (48 000+ logements) par ACP, analyse canonique des corrélations (ACC) et clustering K-Means.",
        "pitch_en": "Multivariate exploratory analysis and market segmentation of 48,000+ NYC Airbnb listings using PCA, Canonical Correlation Analysis, and K-Means clustering.",
        "star_bullet_points_fr": [
            "Traitement et analyse exploratoire de 48 000+ observations du marché Airbnb New York.",
            "Réduction de dimensionnalité via Analyse en Composantes Principales (ACP) et analyse des relations multidimensionnelles par ACC.",
            "Segmentation des logements et des quartiers par K-Means et Classification Ascendante Hiérarchique (CAH) avec soutenance et rapport."
        ],
        "star_bullet_points_en": [
            "Processed and cleaned 48,000+ rental listings from the New York City Airbnb open dataset.",
            "Conducted dimensionality reduction with Principal Component Analysis (PCA) and multivariate correlation mapping with CCA.",
            "Segmented listings and neighborhood pricing profiles via K-Means and Hierarchical Clustering, presenting insights with 2 slide decks."
        ],
        "reports": ["reports/Rapport_Analyse_Donnees_ANDO.pdf"],
        "presentations": ["presentations/Presentation_Partie_1.pdf", "presentations/Presentation_Partie_2.pdf"]
    },
    {
        "id": "09_ml_econometrics",
        "folder": "09_Machine_Learning_Economics_DAMI",
        "title_fr": "Machine Learning Appliqué à l'Économétrie des Salaires (Wage Data)",
        "title_en": "Machine Learning in Econometrics: Wage Dynamics Modeling",
        "category": "Econometrics & Statistical Learning",
        "institution": "DAMI / Économie",
        "year": "2025-2026",
        "role": "Quantitative Researcher",
        "technologies": ["R", "RMarkdown", "ISLR2", "Glmnet", "Régression Polynomiale", "Cross-Validation", "Lasso", "Ridge"],
        "keywords": ["econometrie", "machine learning", "r", "lasso", "ridge", "cross-validation", "salaires", "statistiques", "economics"],
        "pitch_fr": "Modélisation de dynamiques salariales par régression polynomiale, sélection de sous-ensembles de variables et régularisation Lasso/Ridge avec validation croisée.",
        "pitch_en": "Statistical learning application to labor economics modeling wage dynamics through polynomial regression, subset selection, and cross-validated penalized shrinkage.",
        "star_bullet_points_fr": [
            "Modélisation prédictive des salaires à l'aide de régressions polynomiales d'ordres croissants et sélection par validation croisée.",
            "Application de techniques de régularisation (Lasso et Ridge) pour isoler les facteurs d'impact économiques prépondérants.",
            "Génération d'un rapport académique complet compilé sous RMarkdown."
        ],
        "star_bullet_points_en": [
            "Modeled wage curves through higher-order polynomial regressions selected via K-fold cross-validation.",
            "Implemented Lasso and Ridge shrinkage methods to identify key driving economic features.",
            "Published an end-to-end reproducible study compiled with RMarkdown."
        ],
        "reports": ["reports/Rapport_ML_Econometrics.pdf"],
        "presentations": []
    },
    {
        "id": "10_c_image_processing",
        "folder": "10_Image_Processing_C_PRIM",
        "title_fr": "Moteur de Traitement d'Images Bas Niveau en C (LUT, Convolutions, Filtres)",
        "title_en": "Low-Level C Image Processing Engine (LUT, Convolutions, Filters)",
        "category": "Systems & Computer Vision",
        "institution": "ENSIIE (1A PRIM)",
        "year": "2023-2024",
        "role": "Systems Software Developer",
        "technologies": ["C", "Make", "Algorithmique Bas Niveau", "Gestion Mémoire", "Convolutions 2D", "LUT", "Format PGM/PPM"],
        "keywords": ["c", "system", "image processing", "computer vision", "bas niveau", "memory", "filtres", "sobel", "convolution"],
        "pitch_fr": "Développement from scratch en langage C pur d'un moteur de manipulation et filtrage d'images numériques sans bibliothèque externe (matrices de convolution, égalisation LUT, Sobel, flou gaussien).",
        "pitch_en": "Engineered a pure low-level C image processing engine from scratch without external dependencies, implementing 2D convolutions, LUT transformations, and edge detectors.",
        "star_bullet_points_fr": [
            "Conception d'une bibliothèque modulaire en C pour la lecture, manipulation et sauvegarde de formats d'images matricielles PGM/PPM.",
            "Implémentation d'algorithmes de transformation de contraste par Look-Up Table (LUT) et filtres spatiaux par produit de convolution (Sobel, Gaussien).",
            "Gestion rigoureuse des pointeurs et allocations dynamiques sans fuite mémoire (validation Valgrind) avec rapport technique."
        ],
        "star_bullet_points_en": [
            "Developed a modular C library for reading, manipulating, and writing raw PGM/PPM raster images.",
            "Implemented Look-Up Table (LUT) contrast enhancement and spatial 2D convolution kernels (Sobel edge detectors, Gaussian blurs).",
            "Ensured zero memory leaks through disciplined pointer and buffer lifecycle management, validated via technical report."
        ],
        "reports": ["reports/Rapport_Projet_PRIM.pdf"],
        "presentations": []
    },
    {
        "id": "11_ocaml_functional",
        "folder": "11_Functional_Programming_OCaml",
        "title_fr": "Projet d'Algorithmique & Programmation Fonctionnelle en OCaml",
        "title_en": "Functional Algorithmic Engine & Interpreter in OCaml",
        "category": "Programming Languages & Algorithms",
        "institution": "ENSIIE (1A OCaml)",
        "year": "2023-2024",
        "role": "Software Developer",
        "technologies": ["OCaml", "Programmation Fonctionnelle", "Types Algébriques", "Pattern Matching", "Recursion", "Make"],
        "keywords": ["ocaml", "fonctionnel", "functional programming", "algorithmique", "types", "pattern matching"],
        "pitch_fr": "Implémentation d'algorithmes complexes et structures de données récursives en OCaml mettant à profit le système de types statique et le filtrage par motif.",
        "pitch_en": "Implemented recursive data structures and algorithmic evaluators leveraging OCaml's strong static type system and pattern matching.",
        "star_bullet_points_fr": [
            "Résolution de problématiques algorithmiques par paradigme fonctionnel pur en OCaml.",
            "Conception de types de données algébriques expressifs et fonctions d'ordre supérieur.",
            "Rédaction d'une suite de tests unitaires et d'un rapport technique explicatif."
        ],
        "star_bullet_points_en": [
            "Modeled algorithmic problem solving using pure functional paradigms in OCaml.",
            "Designed expressive algebraic data types and higher-order recursive evaluation engines.",
            "Delivered comprehensive unit test suites alongside a technical explanatory report."
        ],
        "reports": ["reports/Rapport_Projet_OCaml.pdf"],
        "presentations": []
    },
    {
        "id": "12_card_game_simulation",
        "folder": "12_Card_Game_Probabilistic_Simulation",
        "title_fr": "Simulation Stochastique & Modélisation Probabiliste de Jeu en C",
        "title_en": "Stochastic Game Simulation & Probabilistic Modeling in C",
        "category": "Applied Probability & Simulation",
        "institution": "ENSIIE (1A Math-Info)",
        "year": "2023-2024",
        "role": "Lead Simulation Developer",
        "technologies": ["C", "Monte-Carlo", "Probabilités Appliquées", "Gestion de Projet Gantt", "Make", "Simulation Stochastique"],
        "keywords": ["c", "simulation", "probabilites", "monte carlo", "stochastique", "gantt", "game theory"],
        "pitch_fr": "Modélisation mathématique et simulation informatique multijoueur d'un jeu de stratégie en C, benchmarking de stratégies stochastiques par méthodes de Monte-Carlo.",
        "pitch_en": "Mathematical modeling and multi-agent stochastic simulation of a strategy game in C, benchmarking playing strategies through Monte Carlo simulations.",
        "star_bullet_points_fr": [
            "Modélisation des états d'un jeu de stratégie complexe et implémentation modulaire en langage C.",
            "Conception d'expériences de simulation stochastique à large échelle pour mesurer empiriquement les distributions de probabilité de victoire.",
            "Pilotage de la planification agile avec diagramme de Gantt et rédaction d'un rapport d'expérimentation théorique."
        ],
        "star_bullet_points_en": [
            "Modeled complex strategic state transitions and engineered a modular C simulation engine.",
            "Conducted large-scale Monte Carlo experiments to measure win-rate distributions across heuristic strategies.",
            "Managed project timeline with Gantt charts and authored an empirical experimental report."
        ],
        "reports": ["docs/Rapport_Experience_Probabiliste.pdf"],
        "presentations": []
    },
    {
        "id": "13_kryptosphere_workshops",
        "folder": "13_Kryptosphere_AI_Workshops",
        "title_fr": "Formations & Ateliers Pratiques en Machine Learning (Kryptosphere IA)",
        "title_en": "Machine Learning & AI Educational Workshops (Kryptosphere AI)",
        "category": "AI Education & Technical Leadership",
        "institution": "Association Kryptosphere IA ENSIIE",
        "year": "2024-2025",
        "role": "Formateur Technique IA",
        "technologies": ["Python", "Jupyter", "Scikit-Learn", "Pandas", "Matplotlib", "Seaborn", "Clustering", "Séries Temporelles"],
        "keywords": ["formation", "pedagogie", "kryptosphere", "machine learning", "workshops", "presentation", "clustering", "time series"],
        "pitch_fr": "Création et animation de cycles de formation technique au sein de l'association étudiante Kryptosphere IA : préparation des données, évaluation de modèles, clustering et séries temporelles.",
        "pitch_en": "Authored and delivered comprehensive hands-on Machine Learning workshops for student engineers: data preprocessing, model evaluation metrics, clustering, and time series.",
        "star_bullet_points_fr": [
            "Conception de 4 supports de formation complets (slides PPTX/PDF et notebooks interactifs guidés).",
            "Animation d'ateliers techniques interactifs pour les étudiants de l'ENSIIE sur l'évaluation rigoureuse de modèles prédictifs et les algorithmes de clustering.",
            "Vulgarisation de concepts mathématiques avancés (matrices de confusion, inertie intra-classe, stationnarité)."
        ],
        "star_bullet_points_en": [
            "Authored 4 educational workshops consisting of presentation slide decks and interactive guided Jupyter notebooks.",
            "Led hands-on training sessions for engineering students on predictive model validation and unsupervised clustering.",
            "Distilled advanced statistical concepts (confusion matrices, ROC curves, intra-cluster inertia, stationarity)."
        ],
        "reports": [],
        "presentations": ["presentations/Formation_Evaluation_Modeles_ML.pdf", "presentations/Formation_Clustering.pdf"]
    },
    {
        "id": "14_javafx_parser",
        "folder": "14_JavaFX_Expression_Parser",
        "title_fr": "Analyseur Syntaxique d'Expressions Mathématiques & GUI JavaFX",
        "title_en": "Mathematical Expression Parser & Interactive JavaFX GUI",
        "category": "Software Engineering & OOP Design Patterns",
        "institution": "ENSIIE (1A OOP Java)",
        "year": "2023-2024",
        "role": "Software Engineer",
        "technologies": ["Java", "JavaFX", "Design Patterns", "AST", "Parser", "JUnit", "Logging"],
        "keywords": ["java", "javafx", "oop", "design patterns", "ast", "parser", "gui", "architecture"],
        "pitch_fr": "Conception d'un analyseur d'expressions mathématiques avec arbre syntaxique abstrait (AST) et interface graphique interactive en JavaFX appliquant les patrons de conception (Factory, Composite, Visitor).",
        "pitch_en": "Engineered an arithmetic expression parser with an Abstract Syntax Tree (AST) evaluator and interactive JavaFX interface implementing classic Gang of Four design patterns.",
        "star_bullet_points_fr": [
            "Implémentation robuste d'un parser d'expressions arithmétiques et logiques générant un arbre syntaxique abstrait (AST).",
            "Application rigoureuse des design patterns OOP (Composite pour l'arbre d'expression, Visitor pour l'évaluation, Factory pour la création des nœuds).",
            "Développement d'une interface graphique interactive en JavaFX avec journalisation structurée et tests automatisés."
        ],
        "star_bullet_points_en": [
            "Built a robust parser evaluating mathematical expressions into an Abstract Syntax Tree (AST).",
            "Applied software design patterns (Composite for expression tree, Visitor for evaluation, Factory for node generation).",
            "Developed an interactive JavaFX graphical user interface with structured logging and automated unit tests."
        ],
        "reports": [],
        "presentations": []
    },
    {
        "id": "15_face_data_readiness",
        "folder": "15_Face_Attributes_Data_Readiness",
        "title_fr": "Audit de Qualité de Données & Classification Multi-Attributs de Visages",
        "title_en": "Data Readiness Audit & Multi-Attribute Facial Classification",
        "category": "Computer Vision & Data Quality",
        "institution": "ENSIIE (3A Data Readiness)",
        "year": "2025-2026",
        "role": "Computer Vision / Data Quality Engineer",
        "technologies": ["Python", "PyTorch", "Torchvision", "Scikit-Learn", "Matplotlib", "Data Readiness", "Matrices de Confusion"],
        "keywords": ["computer vision", "data readiness", "pytorch", "classification", "qualite de donnees", "biais", "visages"],
        "pitch_fr": "Pipeline d'évaluation de la qualité des données (Data Readiness) et classification multi-attributs sur données d'images (âge, genre, port de lunettes) avec audit de biais par matrices de confusion.",
        "pitch_en": "Data readiness assessment and multi-task facial attribute classification (age, gender, eyeglasses) featuring comprehensive demographic bias auditing via confusion matrices.",
        "star_bullet_points_fr": [
            "Création d'un dataset customisé et de pipelines de prétraitement d'images sous PyTorch.",
            "Entraînement de modèles pour la prédiction conjointe d'attributs démographiques et d'accessoires.",
            "Audit approfondi des biais de représentativité et performance par matrices de confusion segmentées."
        ],
        "star_bullet_points_en": [
            "Engineered custom datasets and data augmentation pipelines using PyTorch and Torchvision.",
            "Trained convolutional models for multi-task facial attribute inference (demographics & accessories).",
            "Audited representation bias and demographic performance disparities using segmented confusion matrices."
        ],
        "reports": [],
        "presentations": []
    },
    {
        "id": "16_signal_processing",
        "folder": "16_Signal_Processing_Lab",
        "title_fr": "Laboratoire de Traitement du Signal, Débruitage de Wiener & Ondelettes",
        "title_en": "Digital Signal Processing Lab: Wiener Deconvolution & Wavelets",
        "category": "Signal & Image Processing",
        "institution": "ENSIIE (3A Signal Processing)",
        "year": "2025-2026",
        "role": "Signal Processing Engineer",
        "technologies": ["Python", "NumPy", "SciPy", "Matplotlib", "Filtrage de Wiener", "Densité Spectrale", "Ondelettes", "Audio & Image"],
        "keywords": ["signal processing", "traitement du signal", "wiener", "debruitage", "spectral", "fourier", "ondelettes", "audio", "image"],
        "pitch_fr": "Implémentation d'algorithmes de déconvolution et débruitage par filtre de Wiener, estimation de densité spectrale de puissance et analyse temps-fréquence sur signaux audio et images.",
        "pitch_en": "Implemented Wiener deconvolution denoising, power spectral density estimation, and time-frequency wavelet analysis across audio signals and digital images.",
        "star_bullet_points_fr": [
            "Développement de filtres optimaux de Wiener pour la déconvolution et la restauration de signaux corrompus par du bruit blanc gaussien.",
            "Estimation spectrale non paramétrique (périodogramme de Welch) et analyse fréquentielle FFT.",
            "Application à des cas pratiques de débruitage sonore et de filtrage 2D sur des images matricielles."
        ],
        "star_bullet_points_en": [
            "Developed optimal Wiener filters for signal restoration and deconvolution under additive Gaussian noise.",
            "Computed non-parametric spectral density estimates (Welch's periodogram) and FFT frequency transformations.",
            "Applied algorithms to real-world audio cleaning benchmarks and 2D digital image restoration."
        ],
        "reports": [],
        "presentations": []
    }
]

# Write catalog JSON
catalog_path = os.path.join(ALL_PROJ_DIR, "projects_catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)
print(f"[OK] projects_catalog.json created with {len(catalog)} projects.")

# Generate each project README.md
for p in catalog:
    p_dir = os.path.join(ALL_PROJ_DIR, p["folder"])
    readme_path = os.path.join(p_dir, "README.md")
    
    # Check deliverable links
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
- Élève-ingénieur en Mathématiques Appliquées & Intelligence Artificielle à l'**ENSIIE** (Évry-Courcouronnes, France)
- Semestre d'échange à l'**Université McMaster** (Canada)
- **Email** : [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com)
- **GitHub** : [@nourou-dine-mahy](https://github.com/nourou-dine-mahy)
- **LinkedIn** : [Mohamed Nourou Dine CISSE](https://www.linkedin.com)
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"  [README] Generated {p['folder']}/README.md")

# Generate Master Portfolio README.md
portfolio_path = os.path.join(ALL_PROJ_DIR, "README.md")
portfolio_md = """# 🚀 Portfolio de Projets — Mohamed Nourou Dine CISSE
### Étudiant-Ingénieur en Mathématiques Appliquées & Intelligence Artificielle (ENSIIE / McMaster University)
**Recherche active : Stage de Fin d'Études (PFE) / Stage 6 mois en Intelligence Artificielle, Data Science, Data Engineering ou Finance Quantitative.**

[![GitHub](https://img.shields.io/badge/GitHub-nourou--dine--mahy-181717?logo=github)](https://github.com/nourou-dine-mahy)
[![Email](https://img.shields.io/badge/Email-mouhamed.nouroudine.cisse%40gmail.com-EA4335?logo=gmail)](mailto:mouhamed.nouroudine.cisse@gmail.com)
[![Status](https://img.shields.io/badge/Disponible-PFE%202026-brightgreen)]()

---

## 🌟 Présentation & Points Forts

Bienvenue sur le portfolio centralisé de mes projets d'ingénierie, de recherche appliquée et d'entrepreneuriat.  
Ce recueil regroupe l'ensemble de mes travaux menés à l'**ENSIIE**, à l'**Université McMaster**, en entreprise (**Publicis Groupe**, **Infinity Analytics / Gainde 2000**) et dans le cadre de concours d'innovation (**1er prix Challenge Entreprendre**).

Chaque projet est fourni avec :
1. Son **code source propre et documenté**.
2. Ses **rapports techniques complets** (PDF / LaTeX / Word).
3. Ses **supports de soutenance et présentations** (PDF / PPTX).
4. Des **fiches récapitulatives au format STAR** (Situation, Task, Action, Result) adaptées aux recruteurs.

---

## 📑 Sommaire des Projets par Domaine d'Expertise

### 1. 🤖 Intelligence Artificielle, RAG & LLMs
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**01. Plateforme Spielberg (Publicis)**](./01_Spielberg_AI_Data_Platform) | Stage 2A/3A Publicis / Prodigious | FastAPI, RAG, Chunking, Vector DB, Async | [📄 Rapport (54 p.)](./01_Spielberg_AI_Data_Platform/reports/Rapport_de_Stage_Spielberg_2026.pdf) • [📊 Soutenance (22 pl.)](./01_Spielberg_AI_Data_Platform/presentations/Soutenance_Spielberg.pdf) |
| [**05. NLP & Représentations Sémantiques**](./05_NLP_Semantic_Representations_NER) | Master IA (M2IA) | PyTorch, Transformers, FastText, Word2Vec, BiLSTM-CNN | [📄 Rapport Recherche](./05_NLP_Semantic_Representations_NER/reports/Report_CISSE_DIOP.pdf) • [📄 Rapport Embeddings](./05_NLP_Semantic_Representations_NER/reports/Rapport_TP_Embeddings.pdf) |
| [**13. Ateliers & Formations IA Kryptosphere**](./13_Kryptosphere_AI_Workshops) | Assos Kryptosphere IA | Scikit-Learn, Pandas, Clustering, Time Series | [📊 Slides Modèles ML](./13_Kryptosphere_AI_Workshops/presentations/Formation_Evaluation_Modeles_ML.pdf) • [📊 Slides Clustering](./13_Kryptosphere_AI_Workshops/presentations/Formation_Clustering.pdf) |
| [**15. Data Readiness & Visages**](./15_Face_Attributes_Data_Readiness) | 3A ENSIIE | PyTorch, Data Readiness, Matrices de Confusion | 💻 Code PyTorch, visualisations de biais |

---

### 2. 🏗️ Data Engineering, Pipelines & Architecture SaaS
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**02. ETLia : Plateforme ETL Augmentée**](./02_ETLia_AI_Data_Wizard) | **1er Prix Challenge Entreprendre** | React, TypeScript, Tailwind, Python, Streamlit | 💻 Frontend React complet, Backend ETL, Branding |
| [**03. Datamart SunSéjour en Production**](./03_SunSejour_ETL_Datamart) | Projet Data Engineering | Python, Docker, Docker Compose, Star Schema | [📄 Rapport Datamart](./03_SunSejour_ETL_Datamart/reports/Rapport_Datamart_SunSejour.pdf) • [📖 Guide Utilisateur](./03_SunSejour_ETL_Datamart/reports/Guide_Utilisation_ETL_SunSejour.pdf) |

---

### 3. 📈 Machine Learning, Séries Temporelles & Biostatistiques
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**04. Infinity Analytics : Time Series & Scoring**](./04_Infinity_Analytics_Time_Series_ML) | Stage Gainde 2000 | SARIMAX, VAR, DLTS, Calibration ML, Scikit-Learn | [📄 Rapport Stage](./04_Infinity_Analytics_Time_Series_ML/reports/Rapport_de_Stage.pdf) • [📄 Rapport Scoring](./04_Infinity_Analytics_Time_Series_ML/reports/Rapport_Use_Case_7_Scoring.pdf) • [📊 Soutenance](./04_Infinity_Analytics_Time_Series_ML/presentations/Presentation_de_Stage.pdf) |
| [**07. Prédiction Survie Cancer METABRIC**](./07_Breast_Cancer_Biostatistics_MERR) | 2A MERR | R, GLM, Lasso, Elastic Net, Courbes ROC | [📄 Rapport Cancer Survie](./07_Breast_Cancer_Biostatistics_MERR/reports/Rapport_Cancer_Survie_MERR.pdf) |
| [**08. Analyse Factorielle Airbnb NYC**](./08_Airbnb_NYC_Data_Analysis_ANDO) | 2A ANDO | Python, ACP (PCA), ACC (CCA), K-Means, CAH | [📄 Rapport Analyse](./08_Airbnb_NYC_Data_Analysis_ANDO/reports/Rapport_Analyse_Donnees_ANDO.pdf) • [📊 Slides Partie 1](./08_Airbnb_NYC_Data_Analysis_ANDO/presentations/Presentation_Partie_1.pdf) • [📊 Slides Partie 2](./08_Airbnb_NYC_Data_Analysis_ANDO/presentations/Presentation_Partie_2.pdf) |
| [**09. Machine Learning Économétrique**](./09_Machine_Learning_Economics_DAMI) | Économétrie DAMI | R, Glmnet, ISLR2, Polynomial Reg, Cross-Val | [📄 Rapport ML Salaires](./09_Machine_Learning_Economics_DAMI/reports/Rapport_ML_Econometrics.pdf) |

---

### 4. 💹 Finance Quantitative & Calcul Scientifique
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**06. Solveur EDP Black-Scholes C++ & SDL2**](./06_Black_Scholes_PDE_Solver) | 2A PRAV | C++17, Schéma Implicite, Différences Finies, SDL2 | [📄 Rapport Black-Scholes](./06_Black_Scholes_PDE_Solver/reports/Rapport_Black_Scholes.pdf) • 🖼️ Courbes de Payoff & UML |
| [**12. Simulation Stochastique de Jeu en C**](./12_Card_Game_Probabilistic_Simulation) | 1A Math-Info | C, Méthodes de Monte-Carlo, Gantt | [📄 Rapport Probabilités](./12_Card_Game_Probabilistic_Simulation/docs/Rapport_Experience_Probabiliste.pdf) • 📅 Planning Gantt |
| [**16. Lab Traitement du Signal & Wiener**](./16_Signal_Processing_Lab) | 3A Signal Processing | Python, NumPy, SciPy, Filtre de Wiener, Ondelettes | 💻 Notebooks de débruitage audio/image |

---

### 5. 💻 Génie Logiciel, Systèmes & Programmation
| Projet | Contexte | Technologies | Livrables |
| :--- | :--- | :--- | :--- |
| [**10. Moteur Traitement d'Images en C**](./10_Image_Processing_C_PRIM) | 1A PRIM | C bas niveau, LUT, Convolutions 2D, PGM/PPM | [📄 Rapport C PRIM](./10_Image_Processing_C_PRIM/reports/Rapport_Projet_PRIM.pdf) |
| [**11. Programmation Fonctionnelle OCaml**](./11_Functional_Programming_OCaml) | 1A OCaml | OCaml, Types algébriques, Pattern Matching | [📄 Rapport OCaml](./11_Functional_Programming_OCaml/reports/Rapport_Projet_OCaml.pdf) |
| [**14. Parser d'Expressions & GUI JavaFX**](./14_JavaFX_Expression_Parser) | 1A OOP Java | Java, JavaFX, Design Patterns (Composite, Visitor) | 💻 Application complète JavaFX & tests |

---

## ⚡ Outil d'Automatisation des Candidatures

Un outil Python interactif et scriptable est inclus pour générer des candidatures ultra-ciblées en quelques secondes :

```bash
# Exemple 1 : Générer une candidature ciblée Data Science / Machine Learning
python3 automate_candidatures.py --profil ml --entreprise "TotalEnergies"

# Exemple 2 : Générer une candidature ciblée Data Engineering
python3 automate_candidatures.py --profil de --entreprise "Databricks"

# Exemple 3 : Analyser directement une offre d'emploi copiée dans un fichier texte
python3 automate_candidatures.py --offre offre_stage.txt --entreprise "BNP Paribas"
```

Cet outil produit automatiquement :
1. Une **lettre de motivation ultra-personnalisée** citant vos 3 projets les plus pertinents avec chiffres et méthodologies.
2. Un **message d'accroche pour recruteur** (LinkedIn / Email court).
3. Une section **"Projets Réalisés" prête pour votre CV** (puces STAR percutantes).
4. La liste exacte des **rapports PDF et présentations à joindre**.

---

## 📬 Contact & Liens
- **Candidat** : Mohamed Nourou Dine CISSE
- **Email** : [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com)
- **Téléphone** : +33 7 65 60 09 97
- **Profil GitHub** : [github.com/nourou-dine-mahy](https://github.com/nourou-dine-mahy)
- **Localisation** : Paris, France / Disponible mobilité nationale & internationale
"""

with open(portfolio_path, "w", encoding="utf-8") as f:
    f.write(portfolio_md)
print("[OK] Master README.md (Portfolio) generated.")

# Copy also to PORTFOLIO.md for explicit naming
shutil.copy2(portfolio_path, os.path.join(ALL_PROJ_DIR, "PORTFOLIO.md"))
print("[OK] PORTFOLIO.md created.")
