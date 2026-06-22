# BDE — Bureau des Élèves · ESAD Orléans

Site web du BDE de l'ESAD Orléans.

**Production :** https://bde-esad-orleans.github.io/bde/

---

## Structure du projet

```
bde/
├── index.html          # Accueil : planning + événements à venir + archives
├── activites.html      # Clubs et boîte à idées
├── association.html    # L'équipe BDE + présentation de l'association
├── viewer.html         # Affichage d'un événement (lit un fichier .md)
├── manage.html         # Interface de gestion (protégée par mot de passe)
├── style.css           # Styles globaux
├── script.js           # Chargement markdown pour viewer.html
├── server.py           # Serveur local + API pour manage.html
│
├── _events/            # Événements à venir (fichiers .md)
├── _archive/           # Événements passés (fichiers .md)
│
├── data/
│   ├── events.json     # Index des événements à venir
│   ├── archive.json    # Index des archives
│   ├── clubs.json      # Liste des clubs étudiants
│   └── equipe.json     # Membres du BDE
│
├── assets/
│   └── images/
│       ├── posters/                  # Affiches des événements
│       └── equipe-et-planning/       # Photo d'équipe, planning, boîte à idées
│
└── .github/workflows/
    ├── deploy.yml          # Déploiement GitHub Pages (push sur main)
    └── archive-events.yml  # Archivage automatique (1er du mois)
```

---

## Format d'un événement

Chaque événement est un fichier Markdown dans `_events/` ou `_archive/` :

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

Le nom de fichier suit le format `YYYY-MM-DD-slug.md`.

---

## Gestion du site

### Option 1 — Interface no-code (recommandé)

1. Créer un fichier `.env` à la racine du projet (une seule fois) :
   ```
   BDE_PASSWORD=votre_mot_de_passe
   ```

2. Lancer le serveur local :
   ```bash
   python3 server.py
   ```
   Le serveur écoute sur toutes les interfaces — accessible depuis le téléphone sur le même Wi-Fi via `http://<IP-locale>:4242`.

3. Ouvrir http://localhost:4242/manage.html

L'interface permet de gérer :
- **Événements** — ajouter, modifier, archiver, supprimer
- **Planning** — remplacer l'image du planning affiché sur l'accueil
- **Clubs** — ajouter, modifier, supprimer des clubs (nom, catégorie, membres, Instagram)
- **Équipe** — modifier les noms des membres et la photo d'équipe

Les modifications dans les onglets Clubs, Équipe et Planning sont gardées en mémoire jusqu'au clic sur **"Publier"**, qui sauvegarde tout sur le disque et crée un commit git. Il reste ensuite à pousser le commit depuis GitHub Desktop (ou `git push`).

La session expire automatiquement après **20 minutes d'inactivité**.

### Option 2 — Directement dans les fichiers

Modifier les `.md` dans `_events/` ou `_archive/`, mettre à jour les JSON dans `data/`, puis committer.

---

## Déploiement

Chaque push sur `main` déclenche `deploy.yml` qui publie sur GitHub Pages.

L'archivage automatique tourne le 1er de chaque mois : les événements dont la date est passée sont déplacés de `_events/` vers `_archive/` et les JSON sont mis à jour.
