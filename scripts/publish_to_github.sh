#!/usr/bin/env bash
# Script d'aide pour initialiser et publier vos projets sur GitHub (nourou-dine-mahy)

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=========================================================="
echo "  ASSISTANT DE PUBLICATION GITHUB (Mohamed Nourou Dine CISSE)"
echo "  Compte cible : nourou-dine-mahy"
echo "=========================================================="
echo ""
echo "Vous avez 16 projets prêts à être publiés ou partagés dans :"
echo "$DIR"
echo ""
echo "Options disponibles :"
echo "1) Publier le Portfolio global (Master Repo Portfolio)"
echo "2) Publier un projet spécifique en tant que nouveau dépôt GitHub"
echo "3) Quitter"
echo ""
read -p "Votre choix (1/2/3) : " choix

if [ "$choix" = "1" ]; then
    echo ""
    echo "Initialisation du dépôt pour l'ensemble du portfolio..."
    git init
    git add README.md PORTFOLIO.md projects_catalog.json automate_candidatures.py
    git commit -m "feat: initial commit of AI & Data Engineering Portfolio"
    echo ""
    echo "Pour le relier à GitHub, créez le dépôt 'portfolio' sur github.com puis lancez :"
    echo "  git remote add origin git@github.com:nourou-dine-mahy/portfolio.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"

elif [ "$choix" = "2" ]; then
    echo ""
    echo "Liste des projets disponibles :"
    i=1
    for d in $(ls -d */ | grep -v scripts); do
        echo "  $i) $d"
        i=$((i+1))
    done
    echo ""
    read -p "Entrez le nom du dossier à publier (ex: 01_Spielberg_AI_Data_Platform) : " target
    if [ -d "$target" ]; then
        cd "$target"
        if [ ! -d ".git" ]; then
            git init
            git add .
            git commit -m "feat: initial commit for $target"
            echo "Dépôt local initialisé dans $target."
            echo "Pour le publier sur GitHub :"
            echo "  gh repo create \"$target\" --public --source=. --remote=origin --push"
            echo "  (ou créez le repo sur github.com puis 'git remote add origin ...' et 'git push -u origin main')"
        else
            echo "Le dossier contient déjà un dépôt git."
        fi
    else
        echo "Dossier introuvable."
    fi
else
    echo "Terminé."
fi
