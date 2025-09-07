# BDE - Site Web du Bureau des Élèves

Bienvenue sur le projet de site web officiel du Bureau des Élèves (BDE). Cette plateforme sert de centre d'information pour les étudiants afin de rester informés des événements à venir, accéder aux archives des événements passés et s'engager avec la communauté BDE.

## 🎯 Aperçu du Projet

Le site web BDE vise à :
- Afficher les événements à venir organisés par le BDE dans l'ordre chronologique
- Fournir une archive des événements passés avec les retours des étudiants, témoignages, évaluations et albums photo
- Offrir un système de gestion de contenu facile pour les non-développeurs
- Utiliser des outils et hébergement gratuits

## ✨ Fonctionnalités

### Événements à Venir
- **Affichage Chronologique** : Les événements sont organisés par date, montrant ce qui arrive ensuite
- **Détails des Événements** : Date, heure, lieu, description et informations d'inscription
- **Affiches d'Événements** : Affichage des mêmes affiches utilisées pour les annonces dans le bâtiment
- **Appel Visuel** : Interface moderne et claire mettant en évidence le prochain événement

### Archives d'Événements
- **Dépôt d'Événements Passés** : Historique complet des événements BDE
- **Affiches d'Événements** : Archive de toutes les affiches d'événements pour référence historique
- **Retours des Étudiants** : Témoignages et évaluations des participants aux événements
- **Albums Photo** : Galeries de souvenirs pour chaque événement
- **Recherche et Filtrage** : Navigation facile dans les événements passés

### Gestion de Contenu
- **Basé sur Markdown** : Fichiers Markdown simples pour chaque événement
- **Téléchargement d'Images Direct** : Glisser-déposer les images directement dans l'éditeur GitHub
- **Reconstruction Automatique** : Le site se met à jour automatiquement lors des changements de contenu
- **Contrôle de Version** : Historique complet de tous les changements de contenu
- **Convivial pour les Non-Développeurs** : Édition visuelle avec l'interface web de GitHub

## 🛠️ Stack Technologique

### Solutions Gratuites Recommandées

#### Hébergement et Développement de Site Web
- **GitHub Pages + Jekyll** (Solution complète)
  - Hébergement de site statique gratuit
  - Support Jekyll intégré pour les fichiers Markdown
  - Génération automatique de site à partir de Markdown
  - Support de domaine personnalisé
  - Intégration du contrôle de version
  - Aucun hébergement externe nécessaire

#### Gestion de Contenu
- **Fichiers Markdown GitHub**
  - Fichiers Markdown simples pour chaque événement
  - Téléchargement d'images direct via l'éditeur web GitHub
  - Reconstruction automatique du site lors des commits
  - Contrôle de version pour tous les changements de contenu
  - Gratuit et intégré à l'hébergement
  - Très convivial pour les non-développeurs

#### Framework de Site Web
- **Jekyll** (Intégré à GitHub Pages)
  - Support Markdown natif
  - Génération automatique de site
  - Intégration GitHub Pages intégrée
  - Aucune configuration supplémentaire requise
  - Hébergement gratuit inclus

## 📋 Feuille de Route d'Implémentation

### Phase 1 : Fondation (Semaine 1-2)
- [ ] Configurer le dépôt GitHub
- [ ] Activer GitHub Pages avec Jekyll
- [ ] Créer la structure de base du site Jekyll
- [ ] Configurer l'organisation des fichiers Markdown (`_events/` et `_archive/`)

### Phase 2 : Fonctionnalités Principales (Semaine 3-4)
- [ ] Implémenter l'affichage des événements à venir
- [ ] Créer le système d'archive d'événements
- [ ] Concevoir la mise en page responsive
- [ ] Ajouter le style de base et l'identité visuelle

### Phase 3 : Gestion de Contenu (Semaine 5-6)
- [ ] Créer la structure de fichiers Markdown pour les événements (`_events/` et `_archive/`)
- [ ] Configurer la reconstruction automatique du site lors des changements de fichiers
- [ ] Créer un workflow d'édition Markdown simple pour les non-développeurs
- [ ] Tester le workflow de gestion de contenu avec les téléchargements d'images

### Phase 4 : Fonctionnalités Avancées (Semaine 7-8)
- [ ] Ajouter la fonctionnalité de galerie photo
- [ ] Implémenter le système de retours/évaluations
- [ ] Créer les capacités de recherche et filtrage
- [ ] Optimiser les performances et le SEO

### Phase 5 : Lancement et Maintenance (Semaine 9+)
- [ ] Déployer en production
- [ ] Former les membres BDE sur la gestion de contenu
- [ ] Surveiller et recueillir les retours
- [ ] Planifier les améliorations futures

## 🎨 Considérations de Design

### Expérience Utilisateur
- **Mobile-First** : Design responsive pour tous les appareils
- **Chargement Rapide** : Images optimisées et dépendances minimales
- **Navigation Intuitive** : Structure de menu claire et fonctionnalité de recherche
- **Accessibilité** : Conformité WCAG pour un design inclusif

### Identité Visuelle
- **Marque BDE** : Utilisation cohérente des couleurs, polices et logo
- **Centré sur les Événements** : Hiérarchie visuelle mettant l'accent sur les événements à venir
- **Intégration d'Affiches** : Affichage transparent des affiches d'événements physiques
- **Riche en Photos** : Mettre en valeur les souvenirs d'événements et l'esprit communautaire

## 📊 Structure des Données

### Modèle de Données d'Événement (Format Markdown)
```markdown
---
# _events/2024-01-15-soiree-bienvenue-bde.md (événements à venir)
# _archive/2024-01-15-soiree-bienvenue-bde.md (événements passés)
titre: "Soirée de Bienvenue BDE"
date: 2024-01-15
heure: "19:00"
lieu: "Centre Étudiant"
url_inscription: "https://..."
---

# Soirée de Bienvenue BDE

Rejoignez-nous pour la soirée de bienvenue pour commencer le nouveau semestre !

## Détails de l'Événement
- **Date** : 15 janvier 2024
- **Heure** : 19h00
- **Lieu** : Centre Étudiant
- **Inscription** : [Inscrivez-vous ici](https://...)

## Affiche de l'Événement
![Affiche de l'Événement](images/posters/soiree-bienvenue-2024.jpg)

## Photos
![Photo de l'Événement 1](images/events/soiree-bienvenue-1.jpg)
![Photo de l'Événement 2](images/events/soiree-bienvenue-2.jpg)

## Retours des Étudiants
- **Marie** : "Événement incroyable ! ⭐⭐⭐⭐⭐"
- **Pierre** : "Super ambiance et activités amusantes ! ⭐⭐⭐⭐⭐"
```

## 🔧 Configuration de Développement

### Prérequis
- Git
- Compte GitHub
- Compréhension de base de Markdown (optionnel - GitHub a un éditeur visuel)

### Développement Local (Optionnel)
```bash
# Cloner le dépôt
git clone https://github.com/votre-nom-utilisateur/bde-website.git
cd bde-website

# Installer Jekyll (si vous voulez prévisualiser localement)
gem install jekyll bundler
bundle install

# Démarrer le serveur de développement local
bundle exec jekyll serve
```

**Note** : Le développement local est optionnel. Vous pouvez tout éditer directement sur GitHub et voir les changements en direct sur le site web.

## 📝 Guide de Gestion de Contenu

### Pour les Membres BDE (Non-Développeurs)

1. **Ajouter de Nouveaux Événements**
   - Créer un nouveau fichier Markdown dans le dossier `_events/`
   - Utiliser le format de nom de fichier : `YYYY-MM-DD-nom-evenement.md`
   - Remplir les métadonnées (front matter) en haut :
     ```markdown
     ---
     titre: "Soirée de Bienvenue BDE"
     date: 2024-01-15
     heure: "19:00"
     lieu: "Centre Étudiant"
     statut: "upcoming"
     url_inscription: "https://..."
     ---
     ```
   - Écrire la description de l'événement en Markdown
   - **Télécharger les images directement** : Glisser-déposer l'affiche dans l'éditeur
   - GitHub télécharge automatiquement les images et crée le bon chemin
   - Commiter les changements - le site se reconstruit automatiquement

2. **Archiver les Événements Passés**
   - Déplacer le fichier de l'événement du dossier `_events/` vers le dossier `_archive/`
   - Ajouter une section "Retours des Étudiants" avec les témoignages
   - Télécharger les photos de l'événement en les glissant dans l'éditeur
   - Commiter les changements pour mettre à jour l'archive

3. **Gérer le Contenu**
   - Utiliser l'interface web de GitHub avec l'éditeur Markdown visuel
   - Glisser-déposer les images directement dans l'éditeur
   - Utiliser le formatage Markdown pour le texte enrichi (gras, liens, listes)
   - Collaborer grâce aux fonctionnalités intégrées de GitHub
   - Prévisualiser les changements avant de commiter

## 🚀 Déploiement

### Déploiement GitHub Pages
1. Pousser le code vers la branche principale
2. Activer GitHub Pages dans les paramètres du dépôt
3. Configurer le domaine personnalisé (optionnel)
4. Configurer les déploiements automatiques


## 🤝 Contribution

### Pour les Développeurs
1. Forker le dépôt
2. Créer une branche de fonctionnalité
3. Apporter vos modifications
4. Tester soigneusement
5. Soumettre une pull request

### Pour les Membres BDE
1. Utiliser GitHub pour la gestion de contenu
2. Signaler les problèmes via les issues GitHub
3. Fournir des retours sur l'expérience utilisateur
4. Suggérer de nouvelles fonctionnalités

## 📞 Support

### Problèmes Techniques
- Créer des issues GitHub pour les bugs ou problèmes techniques
- Consulter la documentation pour les solutions communes
- Contacter l'équipe de développement pour les problèmes complexes

### Gestion de Contenu
- Se référer au guide de gestion de contenu
- Contacter la direction BDE pour les problèmes d'accès
- Utiliser la documentation d'aide de GitHub

## 📄 Licence

Ce projet est open source et disponible sous la [Licence MIT](LICENSE).

## 🙏 Remerciements

- Équipe BDE pour la vision du projet
- Communauté étudiante pour les retours et suggestions
- Communauté open source pour les outils et ressources

---

**Dernière Mise à Jour** : Septembre 2025  
**Version** : 1.0.0  
**Statut** : Phase de Planification