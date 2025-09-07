---
layout: default
title: "Accueil"
---

# Bienvenue sur le site du BDE

Découvrez tous les événements organisés par le Bureau des Élèves !

## Événements à Venir

{% assign upcoming_events = site.events | sort: "date" %}
{% for event in upcoming_events limit:3 %}
<div class="event-card">
  <h3>{{ event.titre }}</h3>
  <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
  <p><strong>Heure :</strong> {{ event.heure }}</p>
  <p><strong>Lieu :</strong> {{ event.lieu }}</p>
  <a href="{{ event.url | relative_url }}">Voir les détails</a>
</div>
{% endfor %}

## Derniers Événements

{% assign recent_events = site.archive | sort: "date" | reverse %}
{% for event in recent_events limit:3 %}
<div class="event-card">
  <h3>{{ event.titre }}</h3>
  <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
  <p><strong>Lieu :</strong> {{ event.lieu }}</p>
  <a href="{{ event.url | relative_url }}">Voir l'archive</a>
</div>
{% endfor %}
