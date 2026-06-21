# BDE — Bureau des Élèves · ESAD Orléans

Site web du BDE de l'ESAD Orléans. Liste les événements à venir et les archives.

**Production :** https://bde-esad-orleans.github.io/bde/

---

## Structure du projet

```
bde/
├── index.html          # Page d'accueil (liste des événements)
├── viewer.html         # Affichage d'un événement (lit un fichier .md)
├── manage.html         # Interface de gestion no-code
├── style.css           # Styles globaux
├── script.js           # Chargement markdown pour viewer.html
├── server.py           # Serveur local (site + API pour manage.html)
│
├── _events/            # Événements à venir
│   └── YYYY-MM-DD-nom.md
├── _archive/           # Événements passés
│   └── YYYY-MM-DD-nom.md
│
├── data/
│   ├── events.json     # Index des événements à venir
│   └── archive.json    # Index des archives
│
├── assets/
│   └── images/
│       └── posters/    # Affiches des événements
│
└── .github/workflows/
    ├── deploy.yml          # Déploiement GitHub Pages (push sur main)
    └── archive-events.yml  # Archivage automatique (1er du mois)
```

---

## Format d'un événement

Chaque événement est un fichier Markdown avec un frontmatter :

```markdown
---
titre: "Gala de la Charbonnière"
date: 2026-04-18
heure: "20:30 - 03h00"
lieu: "108 rue de Bourgogne, Orléans"
poster: "assets/images/posters/charbo-04-2026.jpg"
---

Description de l'événement en Markdown…
```

Le fichier va dans `_events/` s'il est à venir, `_archive/` s'il est passé.  
Le nom de fichier suit le format `YYYY-MM-DD-slug.md`.

---

## Gestion du site

### Option 1 — Interface no-code (recommandé)

Lancer le serveur local :

```bash
python3 server.py
```

Puis ouvrir http://localhost:4242/manage.html dans Chrome ou Edge.

L'interface permet d'ajouter, modifier, archiver et supprimer des événements. Le bouton **"Publier sur le site"** crée un commit git — il reste à pousser depuis GitHub Desktop.

### Option 2 — Directement dans les fichiers

Créer/modifier les `.md` dans `_events/` ou `_archive/`, puis mettre à jour `data/events.json` et `data/archive.json` en conséquence.

---

## Déploiement

Chaque push sur `main` déclenche le workflow `deploy.yml` qui publie le site sur GitHub Pages.

L'archivage automatique tourne le 1er de chaque mois : les événements dont la date est passée sont déplacés de `_events/` vers `_archive/` et les JSON sont mis à jour.
