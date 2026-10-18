# NLP: Semantic Representations, Named Entity Recognition & Deep Text Classification

> **Cadre académique** : ENSIIE — Module Traitement Automatique du Langage Naturel (NLP)  
> **Auteurs** : Mohamed Nourou Dine CISSE & DIOP  
> **Domaine** : `Natural Language Processing (NLP) & Deep Learning`  
> **Stack Technique** : `Python` `PyTorch` `Hugging Face Transformers` `BiLSTM` `CNN 1D` `Word2Vec` `SpaCy`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet académique explore les représentations sémantiques continues et les architectures de réseaux de neurones profonds appliquées au traitement automatique de la langue (TAL / NLP) :
1. **Plongements lexicaux sémantiques (*Word Embeddings*)** : Implémentation et évaluation des propriétés vectorielles (similarité cosinus, arithmétique sémantique du type *Roi - Homme + Femme = Reine*) via Word2Vec et FastText.
2. **Reconnaissance d'Entités Nommées (*NER*) & Classification de Documents** :
   - Conception d'un modèle hybride **BiLSTM + CNN** pour l'extraction d'entités au niveau token.
   - Implémentation d'un classifieur textuel à convolution 1D (**Kim CNN**).
   - *Fine-tuning* d'architectures **Transformers** (BERT / CamemBERT) pour la classification supervisée.

---

## 🏗️ Structure du Répertoire

```text
05_NLP_Semantic_Representations_NER/
├── README.md                      # Documentation technique complète
├── reports/
│   ├── Report_CISSE_DIOP.pdf      # Rapport complet sur le NER et les réseaux récurrents/convolutifs
│   └── Rapport_TP_Embeddings.pdf  # Compte-rendu d'expérimentation sur les word embeddings
└── src/
    ├── embeddings.ipynb           # Notebook d'analyse sémantique et géométrie des plongements
    └── scripts/
        ├── README.md              # Instructions spécifiques aux scripts
        ├── requirements.txt       # Dépendances Python (torch, transformers, seqeval, etc.)
        ├── run_lstm_cnn.sh        # Script shell automatisant les entraînements et métriques
        ├── ner_lstm_cnn.py        # Modèle BiLSTM + CNN pour le Named Entity Recognition
        ├── cnn_classification.py  # Modèle 1D-CNN pour la classification de phrases
        └── transformers_classification.py # Fine-tuning de modèles Transformers (Hugging Face)
```

---

## ⚙️ Détail des Modèles Développés

1. **Plongements Sémantiques (`embeddings.ipynb`)** :
   - Évaluation intrinsèque des représentations vectorielles, visualisation t-SNE des clusters sémantiques.
2. **NER BiLSTM-CNN (`ner_lstm_cnn.py`)** :
   - Encodage au niveau caractère par convolution 1D combiné à des embeddings de mots pré-entraînés.
   - Passage dans un BiLSTM bidirectionnel pour capturer le contexte bilatéral des tokens.
   - Métriques d'évaluation séquentielles (F1-score CoNLL via `seqeval`).
3. **Fine-tuning Transformers (`transformers_classification.py`)** :
   - Adaptation supervisée de checkpoints pré-entraînés avec warm-up et decay du taux d'apprentissage.

---

## 🚀 Guide d'Exécution

### Installation
```bash
cd src/scripts
pip install -r requirements.txt
```

### 1. Entraînement du modèle BiLSTM-CNN (NER)
```bash
bash run_lstm_cnn.sh
# ou directement :
python ner_lstm_cnn.py --epochs 10 --batch_size 32
```

### 2. Fine-tuning Transformer
```bash
python transformers_classification.py --model_name "bert-base-uncased" --epochs 3
```

---

## 📄 Preuves & Rapports
- 📄 **Rapport NER & Deep NLP** : [`reports/Report_CISSE_DIOP.pdf`](reports/Report_CISSE_DIOP.pdf)
- 📄 **Rapport Word Embeddings** : [`reports/Rapport_TP_Embeddings.pdf`](reports/Rapport_TP_Embeddings.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
