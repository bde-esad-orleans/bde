---
layout: default
title: "Événements à Venir"
---

# Événements à Venir

Découvrez tous les événements organisés par le BDE.

{% assign upcoming_events = site.events | sort: "date" %}
{% for event in upcoming_events %}
<div class="event-card">
  <h3>{{ event.titre }}</h3>
  <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
  <p><strong>Heure :</strong> {{ event.heure }}</p>
  <p><strong>Lieu :</strong> {{ event.lieu }}</p>
  <p>{{ event.content | strip_html | truncate: 150 }}</p>
  <a href="{{ event.url }}">Voir les détails</a>
</div>
{% endfor %}

{% if upcoming_events.size == 0 %}
<p>Aucun événement à venir pour le moment. Revenez bientôt !</p>
{% endif %}
