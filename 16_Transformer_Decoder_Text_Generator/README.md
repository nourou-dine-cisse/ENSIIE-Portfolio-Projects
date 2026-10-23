# Autoregressive Decoder-Only Transformer from Scratch in PyTorch

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Master 2 Artificial Intelligence (M2IA) & ENSIIE Deep Learning Specialization  
> **Author**: Mohamed Nourou Dine CISSE  
> **Core Stack**: `PyTorch`, `RoPE`, `RMSNorm`, `SwiGLU`, `KV Cache`, `Multi-Head Attention`, `TinyStories`  
> **Key Deliverables**: Full PyTorch Model from Scratch, Generation Engine with Top-$p$/Top-$k$, Interactive Notebook

---

## 🇫🇷 Résumé Rapide en Français

Implémentation complète from scratch en pur **PyTorch** d'une architecture **Transformer décodeur autoregressif moderne** (similaire aux familles LLaMA et Mistral), sans utiliser les abstractions préconçues `torch.nn.Transformer`.

Le modèle intègre les briques architecturales les plus récentes de l'état de l'art en LLMs :
- **Rotary Position Embeddings (RoPE)** : Encodage positionnel relatif appliqué par rotation complexe sur les projections $Q$ et $K$, permettant une généralisation efficace sur de longues séquences.
- **SwiGLU Activation Function** : Fonction d'activation bilinéaire surpassant le standard ReLU/GELU dans les couches feed-forward.
- **RMSNorm (Root Mean Square Normalization)** : Normalisation rapide stabilisant l'entraînement des blocs profonds.
- **KV Cache Optimisé** : Accélération de l'échantillonnage autoregressif éliminant la recalculation quadratique des clés et valeurs antérieures.

Le dépôt fournit le code source exhaustif, l'entraînement sur le dataset **TinyStories** et le notebook de génération interactive.

---

## 📌 Architectural Breakdown

$$	ext{Attention}(Q, K, V) = 	ext{softmax}\left( rac{R_{\Theta, m}^d Q (R_{\Theta, n}^d K)^T}{\sqrt{d_k}} + M ight) V$$

where $R_{\Theta, m}^d$ is the RoPE block-diagonal orthogonal rotation matrix and $M$ is the causal triangular mask.

---

## 📂 Repository Layout

```text
16_Transformer_Decoder_Text_Generator/
├── src/
│   ├── transformer_decoder.py       # Full modular PyTorch implementation
│   ├── rope_embedding.py            # Rotary Positional Embeddings implementation
│   ├── generation_sampler.py        # Top-p, Top-k and temperature decoding engine
│   └── kv_cache.py                  # Optimized Key-Value inference cache
├── implement_transformer.ipynb      # Step-by-step training and generation walkthrough
└── README.md
```

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n