# NLP: Semantic Representations & Hybrid BiLSTM-CNN for Sequence Tagging

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Master 2 Artificial Intelligence (M2IA) — Université Paris-Saclay & ENSIIE  
> **Authors**: Mohamed Nourou Dine CISSE & Mouhamadou Moustapha DIOP  
> **Core Stack**: `PyTorch`, `Transformers`, `Word2Vec`, `FastText`, `BiLSTM-CNN`, `Seqeval`  
> **Key Deliverables**: 2 Research Papers, Comprehensive Benchmark Suite, Full PyTorch Models



---

> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).

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

---

## 🇫🇷 Résumé Rapide en Français

Ce projet de recherche approfondie, mené dans le cadre du **Master 2 Intelligence Artificielle (M2IA) de l'Université Paris-Saclay**, explore le continuum des représentations sémantiques en traitement automatique du langage naturel (NLP). 

Nous avons mené une étude comparative rigoureuse :
1. **Espaces d'Embeddings Statiques vs Sous-Motiques** : Analyse géométrique et tests d'analogie lexicale comparant **Word2Vec** (Skip-Gram, CBOW) et **FastText** (n-grammes de caractères pour pallier le vocabulaire hors-dictionnaire OOV).
2. **Architecture Hybride BiLSTM-CNN pour la Reconnaissance d'Entités Nommées (NER)** : Implémentation sous **PyTorch** d'une architecture neuronale combinant un CNN extracteur d'attributs morphologiques au niveau caractère et un BiLSTM bidirectionnel au niveau mot pour capturer la dépendance contextuelle à longue portée.

Les deux rapports de recherche détaillés et le code PyTorch documenté sont inclus dans le dépôt.

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n
