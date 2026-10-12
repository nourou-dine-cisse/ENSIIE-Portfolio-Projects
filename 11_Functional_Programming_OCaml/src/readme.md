# Éditeur de Texte en OCaml – Projet INPF12 2024–2025

## Objectif

Ce projet a pour but de développer un éditeur de texte simple en OCaml, en utilisant une structure de données fonctionnelle appelée **zipper** pour représenter les lignes et le buffer. Il permet :

- Les deplacements dans le texte (haut, bas, gauche, droite)
- L’insertion et la suppression de caractères
- L’ajout de nouvelles lignes

## Structure du projet

- `projet.ml` : le code source OCaml principal, contenant la logique du buffer et l’interface graphique.
- `rapport.pdf` : rapport expliquant les choix techniques, les fonctions implémentées, les limites, etc.
- `Makefile` : pour compiler le projet facilement.
- `tests.ml`: les testes des fonctions implementer dans projet.ml
- `README.md` : ce fichier.

## Compilation

Sur une machine avec OCaml et Graphics installés :

```bash
make
```

puis

```bash
./projet
```

## Compilation des tests

- commenter la derniere ligne de projet.ml a savoir le main puis lancer

```bash
make tests
```
