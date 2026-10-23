# Examining the Effect of Face Accessories on VLM Evaluation

[![Paper](https://img.shields.io/badge/Paper-Research%20Article-red)](Examining_the_effect_of_face_accessories_in_VLM_face_evaluation__1_.pdf)
[![Université Paris-Saclay](https://img.shields.io/badge/Université-Paris--Saclay%20M2IA-990000)](https://www.universite-paris-saclay.fr/)
[![VLM](https://img.shields.io/badge/Models-MiniCPM--V%20%7C%20SigLIP%202-blue)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Context**: Université Paris-Saclay & CEA-List — Master 2 Artificial Intelligence (M2IA 2026)  
> **Authors**: Yahia Abusaqer, Nagham Abuwarda, Salma AlKhalily, **Mouhamed Nourou Dine Cisse**, Mouhamadou Moustapha Diop  
> **Core Stack**: `Vision-Language Models`, `MiniCPM-V 4.6`, `SigLIP 2`, `Counterfactual Design`, `Exact Paired Tests`  
> **Key Deliverables**: 11-page Research Paper, Final Defense Slide Deck, Counterfactual Dataset Protocol

---

## 🇫🇷 Résumé Rapide en Français

Ce travail de recherche de pointe, co-rédigé au sein du **Master 2 Intelligence Artificielle (M2IA) de l'Université Paris-Saclay**, étudie l'impact des accessoires faciaux (lunettes, casquettes de baseball, masques de protection) sur les jugements et prédictions des modèles vision-langage récents (**MiniCPM-V 4.6** génératif et **SigLIP 2** contrastif).

Bien que les accessoires faciaux ne contiennent aucune information intrinsèque sur les compétences professionnelles, le genre ou l'ethnicité d'une personne, ils masquent des traits biométriques clés et véhiculent de puissants stéréotypes sociaux. Pour mesurer cet effet de manière causale, nous avons conçu un protocole expérimental contrefactuel rigoureux :
- **720 identités synthétiques équilibrées** selon 4 ethnicités, 2 genres et 3 tranches d'âge.
- Chaque identité est évaluée sans accessoire (baseline) et avec l'ajout contrôlé par édition d'image d'un accessoire, générant **2 880 images contrefactuelles**.
- Comparaison par tests statistiques appariés exacts sur la reconnaissance d'attributs démographiques et l'adéquation perçue à l'embauche (job-fitness).

L'article de recherche complet (11 pages) a été salué par l'encadrement de recherche CEA-List / Paris-Saclay.

---

## 📌 Executive Summary & Abstract

Vision-Language Models (VLMs) are increasingly queried for person-centric visual understanding. Accessories such as glasses, caps, and face masks carry zero legitimate signal regarding a person's capability or competence, yet they occlude facial morphology and trigger latent societal biases.

In this paper, we establish a controlled counterfactual benchmark:
- **720 synthetic base identities** across 4 ethnicities, 2 genders, and 3 age brackets.
- **2,880 total counterfactual samples** generated via high-fidelity image editing (Base, Glasses, Baseball Cap, Medical Mask).
- Evaluated both a state-of-the-art **generative VLM (MiniCPM-V 4.6)** and a **contrastive foundation model (SigLIP 2)** using exact paired non-parametric tests.

```
 [ Base Identity ] ──► + Glasses      ──► MiniCPM-V 4.6 / SigLIP 2 ──► Shift in Job Suitability
 (720 Identities)  ──► + Baseball Cap ──► Attribute Recognition    ──► Demographic Misclassification
                   ──► + Face Mask    ──► Paired Statistical Test  ──► Quantified Social Bias
```

---

## 📊 Key Research Findings

1. **Severe Attribute Degradation**: Protective face masks degraded gender and age classification fidelity by over **35%**, causing generative VLMs to rely heavily on ambient stereotypical background cues.
2. **Societal Biases in Hiring**: The addition of casual baseball caps induced a statistically significant drop in suitability ratings for executive and professional roles compared to the exact same facial identity depicted without accessories.
3. **Model Disparity**: Contrastive zero-shot models (SigLIP 2) exhibited higher vulnerability to accessory-induced embedding shifts than generative autoregressive models with extended visual chain-of-thought.

---

## 📂 Repository Artifacts

```text
17_Examining_the_effect_of_face_accessories_on_VLM_face_evaluation/
├── Examining_the_effect_of_face_accessories_in_VLM_face_evaluation__1_.pdf # Full 11-page research paper
└── README.md
```

- **GitHub Repository**: [examining-the-effect-of-face-accessories-on-vlm-evaluation](https://github.com/SalmaAlkhalily/examining-the-effect-of-face-accessories-on-vlm-evaluation)
- **Slide Deck**: [Face_accessories_VLM_final_presentation.pptx](https://raw.githubusercontent.com/SalmaAlkhalily/examining-the-effect-of-face-accessories-on-vlm-evaluation/main/presentation/Face_accessories_VLM_final_presentation.pptx)

---

## 👤 Author & Affiliation
- **Mohamed Nourou Dine CISSE**
- Double Degree Student: **ENSIIE** & **Université Paris-Saclay (Master 2 IA M2IA)**
- Academic Exchange: **McMaster University** (Winter 2026)
- Email: [mouhamed.nouroudine.cisse@gmail.com](mailto:mouhamed.nouroudine.cisse@gmail.com) | GitHub: [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)\n