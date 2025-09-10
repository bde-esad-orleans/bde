---
layout: default
title: "Accueil"
---

# Bureau des étudiants de l'ESAD Orléans
<!-- ATTENTION : le fichier planning doit être nommé    planning.png   et placé dans le dossier assets > images > planning -->
<!--ATTENTION : Il ne peut y avoir QU'UN SEUL fichier dans planning.png-->
<img id="photo-centree" src="assets/images/planning/planning.png">

<div class="section-title">
  <div class="section-title__item line"></div>
  <h2 class="section-title__item">Évènements à venir</h2>
  <div class="section-title__item line"></div>
</div>

{% assign upcoming_events = site.events | sort: "date" %}
{% for event in upcoming_events limit:3 %}
<div class="event-card" style="diplay: flex;">
  <img src="{{ event.poster }}">
  <div>
    <h3>{{ event.titre }}</h3>
    <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
    <p><strong>Heure :</strong> {{ event.heure }}</p>
    <p><strong>Lieu :</strong> {{ event.lieu }}</p>
    <a href="{{ event.url | relative_url }}">Voir les détails</a>
  </div>
</div>
{% endfor %}

<div class="section-title">
  <div class="section-title__item line"></div>
  <h2 class="section-title__item">Évènements passés</h2>
  <div class="section-title__item line"></div>
</div>

{% assign recent_events = site.archive | sort: "date" | reverse %}
{% for event in recent_events limit:3 %}
<div class="event-card">
  <h3>{{ event.titre }}</h3>
  <p><strong>Date :</strong> {{ event.date | date: "%d/%m/%Y" }}</p>
  <p><strong>Lieu :</strong> {{ event.lieu }}</p>
  <a href="{{ event.url | relative_url }}">Voir l'archive</a>
</div>
{% endfor %}
