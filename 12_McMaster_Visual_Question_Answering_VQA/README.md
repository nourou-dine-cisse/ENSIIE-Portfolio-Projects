# Visual Question Answering (VQA): Multimodal Vision-Language Deep Learning

> **Cadre académique** : McMaster University (Canada) — Multimodal Deep Learning & Computer Vision  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Multimodal AI (Vision & Language), Cross-Attention & Deep Learning`  
> **Stack Technique** : `Python` `PyTorch` `Transformers (BERT)` `ResNet (CNN)` `Streamlit` `Multimodal Fusion` `PIL`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

Ce projet aborde le problème du **Visual Question Answering (VQA)** : étant donné une image naturelle et une question formulée en langage naturel à son sujet, le modèle doit analyser conjointement le contenu sémantique de l'image et l'intention de la question pour prédire la réponse correcte sous forme d'une tâche de classification ouverte sur un vocabulaire fermé.

L'architecture développée combine :
1. **Un encodeur textuel (BERT)** : Pour extraire les représentations contextuelles denses de la question posée.
2. **Un encodeur visuel (CNN / ResNet)** : Pour extraire la carte de caractéristiques spatiales de l'image.
3. **Un module de fusion multimodale** : Combinant les vecteurs visuels et textuels par produit d'Hadamard et couches denses d'attention croisée.
4. **Une interface interactive (`src/app.py`)** : Permettant de charger une image, poser une question et visualiser la prédiction en direct.

---

## 🏗️ Structure du Répertoire

```text
12_McMaster_Visual_Question_Answering_VQA/
├── README.md                      # Documentation technique
├── reports/
│   └── VQA_Project_Roadmap.pdf    # Feuille de route technique et architecturale du projet
└── src/
    ├── app.py                     # Application interactive de démonstration (upload image + question)
    ├── data_local.ipynb           # Préparation des données, tokenisation et construction du vocabulaire
    ├── vqa_image_pipeline.ipynb   # Pipeline de prétraitement d'images et extraction de features CNN
    ├── train.ipynb                # Entraînement de l'architecture de fusion multimodale et évaluation
    ├── word_vocab.json            # Dictionnaire d'indexation des réponses cibles
    └── VQA_Dataset.csv            # Jeu de données d'annotations (paires questions/réponses/images)
```

---

## ⚙️ Pipeline Multimodal

1. **Extraction Textuelle** :
   - Tokenisation de la question avec `BertTokenizer`.
   - Extraction de l'embedding du token `[CLS]` ou pooling moyen des états cachés.
2. **Extraction Visuelle** :
   - Redimensionnement, normalisation ImageNet.
   - Passage dans les couches convolutives pré-entraînées d'un ResNet pour obtenir un vecteur visuel global.
3. **Fusion & Classification** :
   - Projection des deux modalités dans un espace de dimension commune ($d = 512$).
   - Fusion bilinéaire / concaténation et passage dans un classifieur multiclasse supervisé par cross-entropy.

---

## 🚀 Guide d'Exécution

### Installation
```bash
pip install torch torchvision transformers pillow pandas streamlit jupyter
```

### 1. Entraînement et Expérimentations
Ouvrir les notebooks pour reproduire le prétraitement et l'entraînement :
```bash
cd src
jupyter notebook
```
Exécuter successivement `data_local.ipynb`, `vqa_image_pipeline.ipynb`, puis `train.ipynb`.

### 2. Lancement de l'Application Interactive
```bash
cd src
streamlit run app.py
```

---

## 📄 Preuves & Feuilles de Route
- 📄 **Feuille de Route Technique** : [`reports/VQA_Project_Roadmap.pdf`](reports/VQA_Project_Roadmap.pdf)

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
