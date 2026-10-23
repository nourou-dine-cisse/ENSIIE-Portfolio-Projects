# Financial Sentiment: Classical Machine Learning vs. Bidirectional LSTM

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
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n