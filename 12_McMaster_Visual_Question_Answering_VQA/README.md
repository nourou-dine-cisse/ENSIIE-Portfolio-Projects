# Visual Question Answering (VQA): Multimodal Deep Learning

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![ResNet](https://img.shields.io/badge/Vision-ResNet%20Backbone-blue)](https://pytorch.org/vision/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: McMaster University (Ontario, Canada) — Applied AI & Mechatronics (MECHENG 4AI3)  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `ResNet-50`, `LSTM`, `Multimodal Fusion`, `Hadamard Product`, `VQA v2.0`  
> **Key Deliverables**: Full Technical Sprint Roadmap & Specs, Multimodal Fusion Architecture

---

## 🇫🇷 Résumé Rapide en Français

Conçu à l'**Université McMaster (Canada)** dans le cadre du cours d'IA appliquée **MECHENG 4AI3**, ce projet explore le domaine multimodal du **Visual Question Answering (VQA)** : répondre automatiquement à des questions ouvertes en langage naturel portant sur une image d'entrée.

L'architecture neuronale développée sous **PyTorch** opère une fusion d'informations hétérogènes :
- Une branche **Vision** s'appuyant sur un backbone convolutif profond (**ResNet-50**) pour extraire un vecteur spatial dense décrivant l'image.
- Une branche **Langage** encodant la question textuelle via un réseau récurrent **LSTM**.
- Un module de **fusion multimodale** (produit de Hadamard et projections linéaires conjointes) alimentant un classifieur multiclasse sur le vocabulaire de réponses possibles.

Le document de synthèse et le code source complet sont inclus.

---

## 🏗️ Architecture & Multimodal Fusion

```
  Input Image (RGB)  ──► [ Pretrained ResNet-50 ] ──► Spatial Embedding v ∈ R^2048
                                                             │
                                                     [ Linear Projection ] ──► v_proj ∈ R^1024
                                                                                   │
                                                                                 ( ⊗ ) Hadamard Fusion
                                                                                   │
                                                     [ Linear Projection ] ──► q_proj ∈ R^1024
                                                             ▲
  Input Question     ──► [ Word Embeddings + LSTM ] ──► Question State q ∈ R^512
                                                             │
                                                             ▼
                                                [ Multi-Layer Perceptron ]
                                                             │
                                                             ▼
                                                    Predicted Answer Token
```

---

## 📂 Repository Layout

```text
12_McMaster_Visual_Question_Answering_VQA/
├── src/
│   ├── vqa_model.py                 # ResNet + LSTM multimodal fusion architecture
│   └── dataset_loader.py            # VQA image and text batch generator
├── reports/
│   └── VQA_Project_Roadmap.pdf      # Sprint roadmap and architecture specifications
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n