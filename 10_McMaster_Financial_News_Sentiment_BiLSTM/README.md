# Financial News Sentiment Analysis: Bidirectional LSTM Deep Learning

> **Cadre académique** : McMaster University (Canada) — STATS 4A03 / Advanced Statistical Learning  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Financial NLP & Deep Learning Sentiment Classification`  
> **Stack Technique** : `Python` `TensorFlow / Keras` `BiLSTM` `Word Embeddings` `Scikit-learn` `Matplotlib`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet a été réalisé lors de mon semestre d'échange académique à **McMaster University** (Canada). Il aborde la classification automatique du sentiment exprimé dans les dépêches et flux d'actualités financières (impact haussier, baissier ou neutre sur les marchés).

La complexité du langage financier réside dans son vocabulaire spécialisé et la présence de nuances contextuelles où l'ordre des mots est déterminant (ex. *"earnings beat expectations but guidance was cut"*). Pour capturer cette dépendance bidirectionnelle, le projet met en œuvre une architecture de réseau récurrent profond **Bidirectional LSTM (BiLSTM)** précédée d'une couche d'embedding continu.

---

## 🏗️ Structure du Répertoire

```text
10_McMaster_Financial_News_Sentiment_BiLSTM/
├── README.md                      # Documentation technique
├── reports/
│   ├── Financial_News_Sentiment_Report.pdf # Rapport académique complet du projet
│   └── Sujet_Projet.pdf           # Cahier des charges et consignes McMaster
└── src/
    └── Project.ipynb              # Notebook interactif complet (pipeline, entraînement, métriques)
```

---

## ⚙️ Pipeline de Traitement & Modélisation

1. **Prétraitement Textuel** :
   - Nettoyage des caractères spéciaux, normalisation de la casse et filtrage des bruits de ponctuation.
   - Tokenisation et conversion en séquences d'entiers avec vocabulaire indexé.
   - Remplissage (*Zero-padding*) uniforme avec troncature aux longueurs maximales fixées.
2. **Architecture Neuronale** :
   - **Couche d'Embedding** projetant les tokens dans un espace dense continu.
   - **Couche Bidirectional LSTM** extrayant simultanément les dépendances passées et futures du texte.
   - Couches de régularisation par **Dropout** pour prévenir le surapprentissage.
   - **Couche Dense Softmax** produisant la distribution de probabilité sur les classes de sentiment.
3. **Évaluation** :
   - Matrice de confusion, précision, rappel et F1-score macro.

---

## 🚀 Guide d'Exécution

```bash
# Installation des librairies requises
pip install tensorflow numpy pandas scikit-learn matplotlib seaborn jupyter

# Lancement du notebook
cd src
jupyter notebook Project.ipynb
```

---

## 📄 Preuves & Rapports Inclus
- 📄 **Rapport de Projet McMaster** : [`reports/Financial_News_Sentiment_Report.pdf`](reports/Financial_News_Sentiment_Report.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
