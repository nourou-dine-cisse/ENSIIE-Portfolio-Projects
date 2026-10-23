# LoRA: Low-Rank Adaptation of Large Language Models (From Scratch in PyTorch)

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=flat&logo=huggingface)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

> **Context**: Master 2 Artificial Intelligence (M2IA) & Deep Learning Optimization  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `LoRA`, `PEFT`, `Transformers`, `Hugging Face`, `BERT`  
> **Key Deliverables**: Complete From-Scratch PyTorch LoRA Module, IMDB Benchmark Pipeline, Interactive Walkthrough

---

## 🇫🇷 Résumé Rapide en Français

Ce projet propose une implémentation complète from scratch sous **PyTorch** de la technique **LoRA (Low-Rank Adaptation)** pour le fine-tuning efficace en paramètres (**PEFT**) de modèles Transformers et Grands Modèles de Langage (LLMs), suivant les principes de [Hu et al., 2021](https://arxiv.org/abs/2106.09685).

Plutôt que d'adapter l'intégralité des 108 millions de paramètres de BERT pour la classification de sentiment sur IMDB :
- Nous gelons 99,6 % des poids du modèle de base.
- Nous injectons une décomposition matricielle de bas rang $W = W_0 + rac{lpha}{r} BA$ sur les projections d'attention ($W_q, W_k, W_v$).
- À l'inférence, les matrices entraînées sont fusionnées directement dans les poids de base, garantissant **une surcharge de latence strictement nulle (0 ms)**.

**Résultat clé** : avec seulement **0,41 % de paramètres entraînés** (443 906 paramètres), notre modèle atteint **87,9 % de précision** sur le jeu de test IMDB, rivalisant avec les 90,9 % du fine-tuning intégral tout en divisant drastiquement l'empreinte mémoire d'entraînement.

---

## 📌 Executive Summary & Key Results

### 📊 Benchmark Comparison (BERT-base-cased on IMDB)

| Adaptation Method | Total Parameters | Trainable Parameters | % Trainable | Test Accuracy | Train Runtime | Inference Latency Overhead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Full Fine-Tuning** | 108,311,810 | 108,311,810 | 100.0% | **90.9%** | 554 s | None |
| **Our LoRA from Scratch ($r=8$)** | 108,755,716 | **443,906** | **0.41%** | **87.9%** | **464 s** | **0 ms** (via weight merge) |
| **Hugging Face PEFT ($r=1$)** | 108,350,212 | 38,402 | 0.035% | 69.9% | 468 s | None |

---

## 📐 Mathematical Formulation

For a pretrained frozen weight $W_0 \in \mathbb{R}^{d_{out} 	imes d_{in}}$, the adapted forward pass computes:

$$\mathbf{h} = W_0 \mathbf{x} + \Delta W \mathbf{x} = W_0 \mathbf{x} + rac{lpha}{r} (B A) \mathbf{x}$$

where $A \in \mathbb{R}^{r 	imes d_{in}}$ is initialized via Gaussian/Kaiming uniform and $B \in \mathbb{R}^{d_{out} 	imes r}$ is initialized to zero, ensuring $\Delta W = 0$ at $t=0$.

---

## 📂 Repository Layout

```text
18_LoRA/
├── lora.py                          # Complete PyTorch LoRALinear and wrapper implementation
├── lora.ipynb                       # End-to-end benchmark on IMDB dataset
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n