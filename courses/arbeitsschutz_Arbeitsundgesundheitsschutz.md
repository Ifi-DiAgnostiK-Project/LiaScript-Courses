<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.6

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/c/cc/Bundesarchiv_Bild_183-41030-0002%2C_Sichtwerbung_f%C3%BCr_Arbeits-_und_Gesundheitsschutzes.jpg

attribute: title image Von Bundesarchiv, Bild 183-41030-0002 / Draum / CC-BY-SA 3.0, CC BY-SA 3.0 de, https://commons.wikimedia.org/w/index.php?curid=5428443

comment:  Arbeitssicherheit & Gesundheitsschutz

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md

title: Arbeitssicherheit und Gesundheitsschutz -- Allgemeine Fragen

tags:
    - Arbeitssicherheit
    - Gesundheitsschutz
    - Arbeits-_und_Gesundheitsschutz

@style
.flex-container {
    display: flex;
    flex-wrap: wrap; /* Allows the items to wrap as needed */
    align-items: stretch;
    gap: 20px; /* Adds both horizontal and vertical spacing between items */
}

.flex-child { 
    flex: 1;
    margin-right: 20px; /* Adds space between the columns */
}

@media (max-width: 600px) {
    .flex-child {
        flex: 100%; /* Makes the child divs take up the full width on slim devices */
        margin-right: 0; /* Removes the right margin */
    }
}

.image-container {
  width: 200px;
  height: 200px;
  border: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background-color: #f8f8f8;
}

.image-container img {
  width: fit-content;
  height: fit-content;
  object-fit: cover;
  display: block;
}

@end

-->

# Arbeitssicherheit und Gesundheitsschutz

Arbeitsbedingte Gesundheitsgefahren, Unfälle und Erkrankungen sollen gar nicht erst entstehen. Dazu ist es wichtig, Gefahrenhinweise und Symbole richtig zu verstehen. <br>
Vor allem junge Menschen sind am Arbeitsplatz besonders gefährdet, weil sie (noch) nicht über alle nötigen Kenntnisse verfügen.
<br>
<br>
Dieses Quiz zeigt Ihnen, wie gut Sie sich bereits auskennen!


<!--style="color:blue; font-weight: bolder"-->Viel Erfolg!
===

![Arbeitsschutz](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/schilder_an_zaun.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, planet-fox_


# In welcher Zeile befinden sich Warnschilder?

_Quelle aller Piktogramme: BGHM_

---------------------

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 1:__
</div>
<div class="flex-child">
@Brandschutzzeichen.Feuerloescher(10)
</div>
<div class="flex-child">
@Brandschutzzeichen.Loeschschlauch(10)
</div>
<div class="flex-child">
@Brandschutzzeichen.Feuerleiter(10)
</div>
</section>

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 2:__
</div>
<div class="flex-child">
@Warnzeichen.Elektrische_Spannung(10)
</div>
<div class="flex-child">
@Warnzeichen.Flurfoerderzeugen(10)
</div>
<div class="flex-child">
@Warnzeichen.Schwebende_Last(10)
</div>
</section>

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 3:__
</div>
<div class="flex-child">
@Verbotszeichen.Zutritt_fuer_Unbefugte_verboten(10)
</div>
<div class="flex-child">
@Verbotszeichen.Besteigen_fuer_Unbefugte_verboten(10)
</div>
<div class="flex-child">
@Verbotszeichen.Allgemeines_Verbotszeichen(10)
</div>
</section>

---------------------------

<br>

- [( )] Zeile 1
- [(X)] Zeile 2
- [( )] Zeile 3


## Aussagen rund um den Arbeits- und Gesundheitsschutz

<!--style="color:blue; font-weight: bolder"-->Die nächsten Aussagen drehen sich rund um den Arbeits- und Gesundheitsschutz. <br> Entscheiden Sie, ob die folgenden Aussagen wahr oder falsch sind. <br> <br> 

<!--style="color:red"-->Hinweis: Es können mehrere Antworten richtig sein.

![Fragezeichen](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/fragezeichen.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, Peggy+Marco_


### 1. Umgang mit Leitern


<!--style="color:blue; font-weight: bolder"-->Dieses Piktogramm zeigt an, dass die Leiter von insgesamt drei Personen zu nutzen ist: <br>   Eine Person, die hinaufsteigt, und zwei Personen, welche die Leiter sichern.

<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Leitern.Die_obersten_3_Sprossen_nicht_besteigen(15)
</div>
<div class="flex-child">
- [( )] wahr
- [(X)] falsch
</div>
</section>

------------------

<!--style="color:blue; font-weight: bolder"-->Dieses Piktogramm bedeutet, dass Leitern nur bei entsprechenden Witterungsbedingungen genutzt werden dürfen.

<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Leitern.Witterungsbedingungen(15)
</div>
<div class="flex-child">
- [(X)] wahr
- [( )] falsch
</div>
</section>

### 2. Brandschutzzeichen


<!--style="color:blue; font-weight: bolder"-->Brandschutzzeichen sind immer orange-schwarz.

- [( )] wahr
- [(x)] falsch

----------------

<!--style="color:blue; font-weight: bolder"-->Warum sind Brandschutzzeichen wichtig?


<section class="flex-container">

<div class="flex-child" style="min-width: 250px">

- [[ ]]  Sie dienen der Dekoration.
- [[X]]  Sie helfen, im Brandfall schnell die richtigen Hilfsmittel zu finden.
- [[ ]]  Sie zeigen Fluchtwege an.
- [[X]]  Sie sind gesetzlich vorgeschrieben.

</div>

<div class="flex-child" style="min-width: 500px">

<div class="image_matrix">
@Brandschutzzeichen.Feuerloescher(10)
@Brandschutzzeichen.Loeschschlauch(10)
@Brandschutzzeichen.Brandmeldetelefon(10)
@Brandschutzzeichen.Richtungspfeil_Rechts(10)
</div>
<div class="image_matrix">
@Brandschutzzeichen.Brandbekaempfung(10)
@Brandschutzzeichen.Brandmelder(10)
@Brandschutzzeichen.Feuerleiter(10)
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)
</div>

</div>

</section>

--------------

<!--style="color:blue; font-weight: bolder"-->Wo müssen Brandschutzzeichen angebracht werden?

- [( )] Nur im Büro.
- [(X)] Überall, wo sich Brandschutzeinrichtungen befinden.
- [( )] Nur in der Werkstatt.
- [( )] Nur im Lager.


### Verbotszeichen

<!--style="color:blue; font-weight: bolder"-->Dieses Piktogramm zeigt, dass kein Wasser versprüht werden darf.

<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Verbotszeichen.Mit_Wasser_spritzen_verboten(15)

</div>
<div class="flex-child">
- [( )] wahr
- [(X)] falsch
</div>
</section>

---


<!--style="color:blue; font-weight: bolder"-->Dieses Symbol meint: Achtung: Diebstahlgefahr!

<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Verbotszeichen.Beruehren_verboten(15)

</div>
<div class="flex-child">
- [( )] wahr
- [(X)] falsch
</div>
</section>

----

<!--style="color:blue; font-weight: bolder"-->Was bedeutet dieses Piktogramm?

<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Verbotszeichen.Rauchen_verboten(15)

</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Kippen wegwerfen verboten!
- [(X)] Rauchen verboten.
- [( )] Besondere Vorsicht beim Rauchen - allgemeine Brandgefahr!
</div>
</section>


### Gebotszeichen

<!--style="color:blue; font-weight: bolder"-->Was bedeutet dieses Schild?


<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gebotszeichen.Wartung_oder_Reparatur_freischalten(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Klappbügel befindet sich hier.
- [(X)] Wartung oder Reparatur freischalten.
- [( )] Fluchttür befindet sich hier. 

</div>
</section>

---------------

<!--style="color:blue; font-weight: bolder"-->Welche Piktogramme sind Gebotsschilder? <br> Ziehe die richtigen Symbole ins Antwortfeld.

<!-- data-randomize -->
@dragdropmultiple(@uid,@Gebotszeichen.Handlauf.src|@Gebotszeichen.Rettungsweste_benutzen.src|@Gebotszeichen.Hautschutzmittel.src,@Rettungszeichen.Erste_Hilfe.src|@Rettungszeichen.Notdusche.src|@Rettungszeichen.Notausstieg.src)



### Zuordnungsaufgabe Piktogramme

<!--style="color:blue; font-weight: bolder"-->Ordnen Sie die Schilder den richtigen Begriffen zu!



<!-- data-randomize -->
-   [[ @Warnzeichen.Heisse_Oberflaeche(10)]        [ @Gebotszeichen.Warnweste(10) ]                 [ @Verbotszeichen.Rauchen_verboten(10) ]       [ @Brandschutzzeichen.Brandbekaempfung(10) ]                 [ 	@Rettungszeichen.Rettungsweg_Notausgang_rechts(10) ]       [ @Gefahrstoffe.Entzuendlich(10) ]]
- [    ( )              ( )                      ( )      (X)              ( )                      ( )     ]  Brandschutzzeichen
- [    ( )              (X)                      ( )      ( )              ( )                      ( )     ]  Gebotszeichen
- [    ( )              ( )                      ( )      ( )              ( )                      (X)     ]  Gefahrstoffe
- [    ( )              ( )                      (X)      ( )              ( )                      ( )     ]  Verbotszeichen
- [    (X)              ( )                      ( )      ( )              ( )                      ( )     ]  Warnzeichen
- [    ( )              ( )                      ( )      ( )              (X)                      ( )     ]  Rettungszeichen



### Lückentext zum Arbeits- und Gesundheitsschutz

<!--style="color:blue; font-weight: bolder"-->Füllen Sie den Lückentext richtig aus:


<!-- data-randomize -->
Arbeits- und Gesundheitsschutz ist ein wichtiger Bestandteil im Berufsleben. <br> <br> 
Ziel ist es, die [[ (Sicherheit) | __Gefährdung__ | Unfall | __Krankheit__  ]] und Gesundheit aller Beschäftigten am Arbeitsplatz zu gewährleisten. <br> <br> 
Zu den wichtigsten Maßnahmen gehören die [[ __Pausenregelung__ |  (Gefährdungsbeurteilung) | __Urlaubsplanung__ | Gehaltsabrechnung  ]] und das Ergreifen geeigneter Schutzmaßnahmen.
<br> <br>
Eine wichtige Rolle spielt auch die [[ (__Unterweisung__) |  Entlassung | __Versetzung__ | Beförderung  ]] der Mitarbeiter und Mitarbeiterinnen. 
<br> <br>
Sie müssen regelmäßig über Gefahren und Schutzmaßnahmen informiert werden. 
<br> <br>
Das Tragen von persönlicher [[ __Freizeitkleidung__ |  Bürobedarf | __Werkzeug__ | (Schutzausrüstung)  ]] kann in bestimmten Bereichen vorgeschrieben sein.
<br> <br>
Arbeitgeber sind verpflichtet, Arbeitsunfälle und [[ Feiertage |  __Überstunden__ | Fehlzeiten | (__Berufskrankheiten__)  ]] zu melden. 
<br> <br>
Beschäftigte sollten bei Gefahr sofort ihren [[ Kollegen |  __Hausmeister__ | (Vorgesetzten) | __Kunden__  ]] informieren.

---

### Warnzeichen 

<!--style="color:blue; font-weight: bolder"-->Ziehen Sie alle Piktogramme, welche Warnzeichen abbilden, in das Antwortfeld!

<!-- data-randomize -->
@dragdropmultiple(@uid,@Warnzeichen.Absturzgefahr.src|@Warnzeichen.Flurfoerderzeugen.src|@Warnzeichen.Magnetische_Felder.src,@Verbotszeichen.Zutritt_fuer_Unbefugte_verboten.src|@Verbotszeichen.Rauchen_verboten.src|@Verbotszeichen.Mit_Wasser_loeschen_verboten.src) 

### Gefahrstoffe


<br>

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Komprimierte_Gase(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Achtung - herumliegende Gasflaschen!
- [(X)] Achtung - komprimierte Gase!
- [( )] Achtung - Stolperfallen!

</div>
</section>

---------------


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Giftig_Sehr_giftig(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Todeszone
- [(X)] Giftig. Sehr giftig.
- [( )] Zutritt verboten!

</div>
</section>

---------------


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Reizend_Gesundheitsschaedlich(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Achtung - Gefahr droht!
- [(X)] Reizend. Gesundheitsschädlich.
- [( )] Achtung - Vorfahrt beachten!

</div>
</section>

---------------


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Aetzend_Reizend(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Achtung - Tropfende Reagenzen!
- [(X)] Ätzend. Reizend.
- [( )] Wasser zum Händewaschen steht nur dosiert zur Verfügung.

</div>
</section>



### Geschafft! 🙌





<!--style="color:blue; font-size: large; font-weight: bolder"-->Tipp: <br>
Weitere Informationen und alle Sicherheitszeichen finden Sie auf der BGHM-Webseite: <br> <br> https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen 

---

![Jubel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/colorfull_jumping.jpg)<!-- style="width: 500px" --> 

_Quelle: Pixabay, geralt_
