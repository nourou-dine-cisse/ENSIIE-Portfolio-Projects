#!/usr/bin/env python3
"""
Outil d'automatisation des candidatures pour Stage de Fin d'Études (PFE)
Auteur : Mohamed Nourou Dine CISSE
École : ENSIIE (Évry-Courcouronnes) & McMaster University (Canada)
"""

import os
import sys
import json
import argparse
from datetime import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.path.join(CURRENT_DIR, "projects_catalog.json")

PROFILES = {
    "ai": ["01_spielberg", "05_nlp_representations", "04_infinity_analytics"],
    "ml": ["01_spielberg", "04_infinity_analytics", "05_nlp_representations"],
    "de": ["01_spielberg", "03_sunsejour_etl", "02_etlia"],
    "data_engineering": ["01_spielberg", "03_sunsejour_etl", "02_etlia"],
    "quant": ["06_black_scholes", "04_infinity_analytics", "09_ml_econometrics"],
    "finance": ["06_black_scholes", "04_infinity_analytics", "09_ml_econometrics"],
    "biostat": ["07_breast_cancer_merr", "08_airbnb_ando", "09_ml_econometrics"],
    "software": ["01_spielberg", "10_c_image_processing", "14_javafx_parser"]
}

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        print(f"Erreur : catalogue introuvable à {CATALOG_PATH}")
        sys.exit(1)
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def score_project(proj, text):
    text_lower = text.lower()
    score = 0
    for kw in proj.get("keywords", []):
        if kw in text_lower:
            score += 3
    for tech in proj.get("technologies", []):
        if tech.lower() in text_lower:
            score += 2
    if proj.get("category", "").lower() in text_lower:
        score += 2
    return score

def select_projects(catalog, profile=None, job_text=None, top_k=3):
    catalog_map = {p["id"]: p for p in catalog}
    
    if job_text:
        scored = []
        for p in catalog:
            s = score_project(p, job_text)
            scored.append((s, p))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for s, p in scored[:top_k]]
    
    if profile and profile.lower() in PROFILES:
        target_ids = PROFILES[profile.lower()]
        return [catalog_map[pid] for pid in target_ids if pid in catalog_map]
    
    # Default to top flagship projects
    return [catalog_map["01_spielberg"], catalog_map["02_etlia"], catalog_map["04_infinity_analytics"]]

def generate_cover_letter_fr(candidate, entreprise, poste, selected_projects):
    date_str = datetime.now().strftime("%d/%m/%Y")
    
    proj_paragraphs = []
    for p in selected_projects:
        bullets = "\n".join([f"    • {b}" for b in p["star_bullet_points_fr"][:2]])
        proj_paragraphs.append(
            f"**{p['title_fr']}** ({p['institution']}) :\n"
            f"{p['pitch_fr']}\n"
            f"{bullets}"
        )
    
    projects_block = "\n\n".join(proj_paragraphs)
    
    letter = f"""# Lettre de Motivation — Candidature Stage de Fin d'Études (PFE)

**Mohamed Nourou Dine CISSE**  
Élève-Ingénieur en Mathématiques Appliquées & Intelligence Artificielle  
ENSIIE (Évry-Courcouronnes) | Échange à l'Université McMaster (Canada)  
Email : mouhamed.nouroudine.cisse@gmail.com | Tél : +33 7 65 60 09 97  
GitHub : [github.com/nourou-dine-mahy](https://github.com/nourou-dine-mahy)  

À l'attention de l'équipe Recrutement / Responsable d'Équipe  
**{entreprise}**  
Date : {date_str}  

**Objet : Candidature au poste de {poste} (Stage de Fin d'Études — 6 mois)**

Madame, Monsieur,

Actuellement en dernière année du cycle ingénieur à l’**ENSIIE** (spécialité Intelligence Artificielle et Mathématiques Appliquées), après un semestre d'échange académique à l’**Université McMaster** au Canada, je vous adresse ma candidature pour rejoindre **{entreprise}** en tant que **{poste}**.

Passionné par la mise en production de solutions d'intelligence artificielle robustes et l'ingénierie des données à forte valeur ajoutée, j'ai développé une double compétence alliant rigueur mathématique et excellence logicielle. Mon parcours m'a permis de concevoir des architectures complètes, depuis la modélisation théorique jusqu'au déploiement :

{projects_block}

Rejoindre **{entreprise}** représente pour moi l'opportunité de mettre à profit mon autonomie, ma maîtrise des architectures IA/Data et ma rigueur analytique au service de vos projets stratégiques. Je serais ravi de contribuer activement aux défis techniques de vos équipes.

Je me tiens à votre entière disposition pour convenir d'un entretien afin d'échanger sur les synergies entre vos besoins et mon profil.

Dans cette attente, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées.

**Mohamed Nourou Dine CISSE**
"""
    return letter

def generate_cover_letter_en(candidate, entreprise, poste, selected_projects):
    date_str = datetime.now().strftime("%B %d, %Y")
    
    proj_paragraphs = []
    for p in selected_projects:
        bullets = "\n".join([f"    • {b}" for b in p["star_bullet_points_en"][:2]])
        proj_paragraphs.append(
            f"**{p['title_en']}** ({p['institution']}):\n"
            f"{p['pitch_en']}\n"
            f"{bullets}"
        )
    
    projects_block = "\n\n".join(proj_paragraphs)
    
    letter = f"""# Cover Letter — End-of-Studies Internship (6 Months)

**Mohamed Nourou Dine CISSE**  
Master's Student in Applied Mathematics & Artificial Intelligence  
ENSIIE (Paris-Saclay affiliate, France) | Exchange at McMaster University (Canada)  
Email: mouhamed.nouroudine.cisse@gmail.com | Phone: +33 7 65 60 09 97  
GitHub: [github.com/nourou-dine-mahy](https://github.com/nourou-dine-mahy)  

Hiring Team / Engineering Leadership  
**{entreprise}**  
Date: {date_str}  

**Subject: Application for {poste} (End-of-Studies Internship)**

Dear Hiring Team,

Currently completing my final year of engineering studies in Applied Mathematics and Artificial Intelligence at **ENSIIE** (France), alongside an academic exchange semester at **McMaster University** (Canada), I am writing to express my strong enthusiasm for joining **{entreprise}** as an intern in **{poste}**.

Throughout my academic journey and previous industry experiences, I have developed a solid foundation combining theoretical machine learning with production-grade software and data engineering:

{projects_block}

I am confident that my technical proficiency in modern AI frameworks, data pipelines, and analytical problem-solving would enable me to make an immediate impact on your strategic initiatives at **{entreprise}**.

I look forward to discussing how my experience and skills align with your team's goals. Thank you for your time and consideration.

Sincerely,

**Mohamed Nourou Dine CISSE**
"""
    return letter

def generate_pitch_email(candidate, entreprise, poste, selected_projects, lang="fr"):
    p_names = ", ".join([f"**{p['title_fr' if lang == 'fr' else 'title_en']}**" for p in selected_projects[:2]])
    if lang == "fr":
        return f"""### 📧 Message Court d'Accroche (Email / LinkedIn)

**Objet** : Candidature {poste} — Mohamed Nourou Dine CISSE (ENSIIE / McMaster)

Bonjour,

Étudiant-ingénieur en IA et Mathématiques Appliquées à l'ENSIIE et actuellement en échange à McMaster University, je suis activement à la recherche de mon stage de fin d'études (PFE, 6 mois) à partir de mai/juin 2026.

Suivant de près les avancées de **{entreprise}**, je souhaiterais vivement contribuer à vos projets en tant que **{poste}**.

Lors de mes précédentes expériences et projets, j'ai notamment conçu des solutions concrètes telles que :
- {selected_projects[0]['pitch_fr']}
- {selected_projects[1]['pitch_fr']}

Vous pouvez retrouver mon portfolio complet avec code source, rapports techniques et présentations de soutenance sur mon GitHub :
🔗 [https://github.com/nourou-dine-mahy](https://github.com/nourou-dine-mahy)

Seriez-vous disponible pour un court échange téléphonique de 10 minutes cette semaine ?

Bien cordialement,  
**Mohamed Nourou Dine CISSE**  
+33 7 65 60 09 97 | mouhamed.nouroudine.cisse@gmail.com
"""
    else:
        return f"""### 📧 Cold Email / LinkedIn Pitch (English)

**Subject**: Application for {poste} — Mohamed Nourou Dine CISSE (ENSIIE / McMaster)

Dear Hiring Manager,

I am a final-year graduate engineering student in Artificial Intelligence and Applied Mathematics at ENSIIE (France), currently completing an exchange semester at McMaster University (Canada). I am actively seeking my 6-month end-of-studies internship starting May/June 2026.

I have been following **{entreprise}**'s work with great interest and would love to contribute to your engineering efforts as a **{poste}**.

My previous engineering and applied research work includes:
- {selected_projects[0]['pitch_en']}
- {selected_projects[1]['pitch_en']}

You can explore my complete open portfolio with documented source code, technical reports, and defense decks on GitHub:
🔗 [https://github.com/nourou-dine-mahy](https://github.com/nourou-dine-mahy)

Would you be open to a brief 10-minute introductory call sometime this week?

Best regards,  
**Mohamed Nourou Dine CISSE**  
+33 7 65 60 09 97 | mouhamed.nouroudine.cisse@gmail.com
"""

def generate_cv_bullet_points(selected_projects, lang="fr"):
    res = "### 📄 Puces Projets Clés pour votre CV\n\n"
    for p in selected_projects:
        title = p["title_fr"] if lang == "fr" else p["title_en"]
        tech = ", ".join(p["technologies"][:6])
        bullets = p["star_bullet_points_fr"] if lang == "fr" else p["star_bullet_points_en"]
        res += f"**{title}** | *{tech}* ({p['institution']}, {p['year']})\n"
        for b in bullets:
            res += f"- {b}\n"
        res += "\n"
    return res

def generate_attachments_checklist(selected_projects):
    res = "### 📎 Fichiers Livrables & Justificatifs à Joindre (depuis `All projects/`)\n\n"
    for p in selected_projects:
        res += f"**{p['folder']}** :\n"
        if p["reports"]:
            for r in p["reports"]:
                res += f"  - [Rapport PDF] `{p['folder']}/{r}`\n"
        if p["presentations"]:
            for pr in p["presentations"]:
                res += f"  - [Présentation/Slides] `{p['folder']}/{pr}`\n"
        if not p["reports"] and not p["presentations"]:
            res += f"  - [Dépôt GitHub / Code] Voir dossier `{p['folder']}`\n"
    return res

def main():
    parser = argparse.ArgumentParser(description="Générateur de candidatures personnalisées pour PFE.")
    parser.add_argument("--profil", default="ai", help="Profil cible (ai, ml, de, quant, biostat, software)")
    parser.add_argument("--entreprise", default="Entreprise Cible", help="Nom de l'entreprise ciblée")
    parser.add_argument("--poste", default="Stagiaire Data Scientist / Machine Learning Engineer", help="Intitulé du poste")
    parser.add_argument("--offre", default=None, help="Chemin vers un fichier texte contenant l'offre d'emploi")
    parser.add_argument("--lang", default="fr", choices=["fr", "en"], help="Langue de génération (fr ou en)")
    parser.add_argument("--output", default=None, help="Fichier de sortie (par défaut : dossier All projects/candidature_<entreprise>.md)")
    args = parser.parse_args()

    catalog = load_catalog()
    
    job_text = None
    if args.offre and os.path.exists(args.offre):
        with open(args.offre, "r", encoding="utf-8") as f:
            job_text = f.read()

    selected = select_projects(catalog, profile=args.profil, job_text=job_text)
    
    if args.lang == "fr":
        letter = generate_cover_letter_fr(None, args.entreprise, args.poste, selected)
    else:
        letter = generate_cover_letter_en(None, args.entreprise, args.poste, selected)

    pitch = generate_pitch_email(None, args.entreprise, args.poste, selected, lang=args.lang)
    cv_bullets = generate_cv_bullet_points(selected, lang=args.lang)
    checklist = generate_attachments_checklist(selected)

    content = f"""{letter}

---

{pitch}

---

{cv_bullets}

---

{checklist}
"""

    out_name = args.output if args.output else os.path.join(CURRENT_DIR, f"candidature_{args.entreprise.replace(' ', '_')}.md")
    with open(out_name, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n[SUCCÈS] Dossier de candidature généré avec succès dans :\n-> {out_name}\n")
    print(f"Projets sélectionnés pour {args.entreprise} ({args.poste}) :")
    for i, p in enumerate(selected, 1):
        print(f"  {i}. {p['folder']} ({p['category']})")

if __name__ == "__main__":
    main()
