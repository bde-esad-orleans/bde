---
layout: default
title: "Archives des Événements"
---

# Archives des Événements

Retrouvez tous les événements passés du BDE avec les retours des étudiants et les photos.

{% assign archived_events = site.archive | sort: "date" | reverse %}
{% for event in archived_events %}
  <div class="event-card">
    <h3>{{ event.titre }}</h3>
    <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
    <p><strong>Lieu :</strong> {{ event.lieu }}</p>
    <p>{{ event.content | truncate: 150 }}</p>
    <a href="{{ event.url }}">Voir l'archive complète</a>
  </div>
{% endfor %}

{% if archived_events.size == 0 %}
<p>Aucun événement archivé pour le moment.</p>
{% endif %}
