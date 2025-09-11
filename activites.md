---
layout: default
title: "Nos activités"
---


# Les Clubs
<p><img class="glitters" src="https://media.tenor.com/xQKnWkukw9YAAAAi/brilho-shine.gif"> <a href="https://docs.google.com/forms/d/e/1FAIpQLSfdvX5rUUFXTu2i3cXDn03kfKD2BA0PLlPZJr6gO7AaRMh9zA/viewform?usp=dialog">Lien vers le formulaire 2025/2026 de création de club</a></p>

### Clubs en cours d'activité
<ul id="clubs-existants">
    <li><img class="glitters" src="https://media.tenor.com/xQKnWkukw9YAAAAi/brilho-shine.gif"> <a href="https://www.instagram.com/fanzizine/">Le club fanzine</a><br>
    Tenu par Jade JARRY (3 DVG-VM) et Naya JEAN (3 DVG-DAD)</li>
    <li><img class="glitters" src="https://media.tenor.com/xQKnWkukw9YAAAAi/brilho-shine.gif"> <a href="https://www.instagram.com/orlinzoofc/">Le club de foot</a><br>
    Tenu par ... et Ali AZAROUAL (2 )</li>
    <li><img class="glitters" src="https://media.tenor.com/xQKnWkukw9YAAAAi/brilho-shine.gif"> <a href="https://www.instagram.com/esaderange_twitch/">Le club émission</a><br>
    Tenu par Mosa BRETON (3 DVG-DAD) et créé avec Harlow PROUST (ex - 3 DVG DAD)</li>
    <li><img class="glitters" src="https://media.tenor.com/xQKnWkukw9YAAAAi/brilho-shine.gif"> Le club d'animation<br>
    Par Martin MARTINOV (3DVG-VM) -> recherche volontaires pour le seconder</li>
</ul>

# Une idée d'évènement, de projet, ou d'amélioration ?

<div class="mailbox-container">
    <!-- bouton avec image -->
    <button type="button" id="boite-a-idees">
        <img src="boite-a-idees.jpg" alt="Boîte à idées">
    </button>

    <!-- formulaire Google -->
    <iframe id="boite-a-idees__form" 
            src="https://docs.google.com/forms/d/e/1FAIpQLSeZC4b_vnbj5EnmH5EZkU8m4ZFO-NQGuxjY5On60DOWZQRaXg/viewform?embedded=true">
    </iframe>

    <img id="enveloppe-img" src="enveloppe.webp" alt="Enveloppe">
</div>

<br>
<button type="button" id="fermer-form">Fermer</button>

<script>
    const bouton = document.getElementById("boite-a-idees");
    const form = document.getElementById("boite-a-idees__form");
    const fermer = document.getElementById("fermer-form");
    const enveloppe = document.getElementById("enveloppe-img");

    bouton.addEventListener("click", () => {
      form.classList.add("active");
      fermer.style.display = "inline-block";
    });

    fermer.addEventListener("click", () => {
      form.classList.remove("active");
      fermer.style.display = "none";

      // lancer animation enveloppe
      enveloppe.classList.add("active");

      // remettre à zéro après animation
      enveloppe.addEventListener("animationend", () => {
        enveloppe.classList.remove("active");
      }, { once: true });
    });
  </script>

