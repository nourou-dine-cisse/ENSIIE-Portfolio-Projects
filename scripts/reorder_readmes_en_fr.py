import os
import re

BASE_ALL = "/Users/nouroudine/Documents/ENSIIE/ENSIIE-Portfolio-Projects/All projects"

def reorder_readme(file_path):
    if not os.path.exists(file_path):
        print(f"Skipping (not found): {file_path}")
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if ## 🇫🇷 Résumé Rapide en Français or ## 🇫🇷 Résumé exists
    fr_pattern = re.compile(r"(---\s*\n+## 🇫🇷 Résumé[^\n]*\n+)(.*?)(?=\n+---\s*\n+## |\n+## 👤|\n+## 📌|\n+## 🏗️|\n+## 📐|\n+## 📊|\n+## 📂|\n+## 🚀|\Z)", re.DOTALL)
    match = fr_pattern.search(content)

    if not match:
        print(f"No FR summary found in: {file_path}")
        return

    fr_section_full = match.group(0).strip()
    # Extract the pure FR section without boundary dividers
    fr_section_clean = re.sub(r"^---\s*\n*", "", fr_section_full).strip()

    # Remove the FR section from its current position
    content_without_fr = content[:match.start()] + content[match.end():]
    # Clean up double dividers ---
    content_without_fr = re.sub(r"---\s*\n+---\s*\n+", "---\n\n", content_without_fr)

    # Add the top indication under the main badges / blockquote if not already present
    indication = "> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).\n\n---\n\n"
    
    # Check if indication already exists
    if "Consulter le résumé en français" not in content_without_fr and "Accéder au résumé" not in content_without_fr:
        # Insert after the first blockquote or after the first `---`
        # Find the first `---`
        first_sep = content_without_fr.find("\n---\n")
        if first_sep != -1:
            idx = first_sep + len("\n---\n\n")
            content_without_fr = content_without_fr[:idx] + indication + content_without_fr[idx:]
        else:
            # Place after badges (first heading block)
            lines = content_without_fr.splitlines(keepends=True)
            insert_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("> **") or line.startswith("[!["):
                    insert_idx = i + 1
            if insert_idx > 0:
                lines.insert(insert_idx, "\n" + indication)
                content_without_fr = "".join(lines)

    # Now append the French summary at the end, right before `## 👤 Author` (or at the very end)
    author_match = re.search(r"(\n+## 👤 Author[^\n]*\n+.*|\n+## 📚 References[^\n]*\n+.*?\n+## 👤 Author.*)", content_without_fr, re.DOTALL)
    if author_match:
        # Place FR section right before author / references
        insert_pos = author_match.start()
        new_content = (
            content_without_fr[:insert_pos].rstrip() +
            "\n\n---\n\n" +
            fr_section_clean +
            "\n\n---\n\n" +
            content_without_fr[insert_pos:].lstrip()
        )
    else:
        new_content = content_without_fr.rstrip() + "\n\n---\n\n" + fr_section_clean + "\n"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content.strip() + "\n")
    print(f"[REORDERED] {file_path}")

# Process all 20 project folders
folders = sorted([d for d in os.listdir(BASE_ALL) if os.path.isdir(os.path.join(BASE_ALL, d)) and d[0].isdigit()])
for folder in folders:
    p = os.path.join(BASE_ALL, folder, "README.md")
    reorder_readme(p)

# Process standalone repos
standalone_repos = [
    "/Users/nouroudine/Documents/ENSIIE/LoRA-From-Scratch-PyTorch/README.md",
    "/Users/nouroudine/Documents/ENSIIE/McMaster-Computer-Vision-CNN-Suite/README.md",
    "/Users/nouroudine/Documents/ENSIIE/McMaster-Machine-Learning-Foundations-from-Scratch/README.md",
    "/Users/nouroudine/Documents/ENSIIE/Sorbonne-Cyber-Malware-GNN-Challenge/README.md",
    "/Users/nouroudine/Documents/ENSIIE/Kryptosphere-AI-Workshops/README.md",
]

# For LoRA, ensure its rich content is combined with the French summary
lora_standalone = "/Users/nouroudine/Documents/ENSIIE/LoRA-From-Scratch-PyTorch/README.md"
with open(lora_standalone, "r", encoding="utf-8") as f:
    lora_txt = f.read()

if "## 🇫🇷 Résumé Rapide en Français" not in lora_txt:
    lora_fr = """
---

## 🇫🇷 Résumé Rapide en Français

Ce projet propose une implémentation complète from scratch sous **PyTorch** de la technique **LoRA (Low-Rank Adaptation)** pour le fine-tuning économe en paramètres (**PEFT**) de modèles Transformers et Grands Modèles de Langage (LLMs), suivant les principes de [Hu et al., 2021](https://arxiv.org/abs/2106.09685).

Plutôt que d'adapter l'intégralité des 108 millions de paramètres de BERT pour la classification de sentiment sur IMDB :
- Nous gelons 99,6 % des poids du modèle de base.
- Nous injectons une décomposition matricielle de bas rang $W = W_0 + \\frac{\\alpha}{r} BA$ sur les projections d'attention ($W_q, W_k, W_v$).
- À l'inférence, les matrices entraînées sont fusionnées directement dans les poids de base, garantissant **une surcharge de latence strictement nulle (0 ms)**.

**Résultat clé** : avec seulement **0,41 % de paramètres entraînés** (443 906 paramètres), notre modèle atteint **87,9 % de précision** sur le jeu de test IMDB, rivalisant avec les 90,9 % du fine-tuning intégral tout en divisant drastiquement l'empreinte mémoire d'entraînement.
"""
    # Insert indication at top
    indication = "\n> 🇫🇷 **Note aux recruteurs francophones** : Un résumé rapide du projet en français est disponible en fin de document — [Consulter le résumé en français](#-résumé-rapide-en-français).\n\n---\n"
    first_sep = lora_txt.find("\n---\n")
    if first_sep != -1:
        idx = first_sep + len("\n---\n")
        lora_txt = lora_txt[:idx] + indication + lora_txt[idx:]
    
    # Insert FR section before Author
    author_pos = lora_txt.find("## 👤 Author")
    if author_pos != -1:
        lora_txt = lora_txt[:author_pos].rstrip() + lora_fr + "\n---\n\n" + lora_txt[author_pos:]
    else:
        lora_txt = lora_txt.rstrip() + lora_fr

    with open(lora_standalone, "w", encoding="utf-8") as f:
        f.write(lora_txt.strip() + "\n")
    print(f"[UPDATED] {lora_standalone}")

for r in standalone_repos:
    if r != lora_standalone:
        reorder_readme(r)

# Reorder Master README.md and PORTFOLIO.md
master_readme = os.path.join(BASE_ALL, "README.md")
reorder_readme(master_readme)
with open(master_readme, "r", encoding="utf-8") as f:
    master_c = f.read()
with open(os.path.join(BASE_ALL, "PORTFOLIO.md"), "w", encoding="utf-8") as f:
    f.write(master_c)
print("[SYNCED] PORTFOLIO.md")
