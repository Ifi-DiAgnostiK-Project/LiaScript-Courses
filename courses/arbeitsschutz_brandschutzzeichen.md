<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.4

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/ISO_7010_F001.svg/1920px-ISO_7010_F001.svg.png
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png

comment:  Brandschutzzeichen

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

tags:
    - Arbeitssicherheit
    - Brandschutzzeichen
    - Arbeits-_und_Gesundheitsschutz

title: Brandschutzzeichen

@style
.flex-container {
    display: flex;[](https://liascript.github.io/LiveEditor/liascript/index.html?#5)
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

.image_matrix img {
    padding: 3px;
    margin: 5px;
    width: 100px;
    border: 1px black solid;
    display:inline-block;
}

@end

-->

# Arbeitssicherheit und Gesundheitsschutz

Arbeitsbedingte Gesundheitsgefahren, Unfälle und Erkrankungen sollen gar nicht erst entstehen. Dazu ist es wichtig, Gefahrenhinweise und Symbole richtig zu verstehen. <br>
Vor allem junge Menschen sind am Arbeitsplatz besonders gefährdet, weil sie (noch) nicht über alle nötigen Kenntnisse verfügen.
<br>
<br>
Dieses Quiz zeigt Ihnen, wie gut Sie sich bereits auskennen!

<!--style="color:red"-->Hinweis: Es können mehrere Antworten richtig sein.

-----



![Arbeitsschutz](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/schilder_an_zaun.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, planet-fox_


<!--style="color:blue; font-weight: bolder"-->Viel Erfolg!
===

## Brandschutzzeichen

>Brandschutz geht uns alle an! <br> Im Betrieb ist es besonders wichtig, Gefahren durch Brände zu kennen und richtig auf sie zu reagieren. <br> <br> Damit Sie sich und andere schützen können, sollten Sie die wichtigsten Brandschutzzeichen kennen und wissen, wie Sie sich im Ernstfall richtig verhalten.  <br> Mit ein wenig Aufmerksamkeit können Sie helfen, Gefahren zu vermeiden und im Notfall schnell zu handeln.

![sicher](img/sicher_aus_schildern.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, succo_

### 1. Signalfarbe von Brandschutzzeichen

Wie sehen Brandschutzzeichen typischerweise aus?


<!-- data-randomize -->
- [( )] Blaues Quadrat mit weißem Symbol
- [( )] Grünes Rechteck mit weißem Symbol
- [(X)] Rotes Quadrat oder Rechteck mit weißem Symbol
- [( )] Gelbes Dreieck mit schwarzem Symbol 



### 2. Die Bedeutung einzelner Brandschutz-Piktogramme


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Brandschutzzeichen.Brandbekaempfung(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Bei Feuer sofort Helm aufsetzen.
- [(X)] Brandbekämpfung.
- [( )] Bei Brand sofort fliehen - alle beschwerenden Kleidungsstücke zurücklassen.
</div>
</section>

------------

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Brandschutzzeichen.Feuerleiter(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Achtung - Haus steht in Flammen!
- [(X)] Hier befindet sich eine Feuerleiter.
- [( )] Fluchtweg erfolgt über Leitern.
</div>
</section>

----

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Brandschutzzeichen.Brandmelder(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Bei Feuer sofort Fahrstuhl rufen.
- [(X)] Bei Feuer über Signalknopf Brand melden.
- [( )] Bei Feuer Licht ausschalten. 
</div>
</section>

### 3. Zuordnungsaufgabe Brandschutzzeichen


Ordnen Sie das jeweilige Symbol der richtigen Bedeutung zu.


<!-- data-randomize -->
[[![Brandschutzpfeil rechts](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Brandschutzzeichen/Richtungspfeil_Rechts.jpg?raw=true) <!-- style="width: 100px" -->]        (![Brandmeldetelefon](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Brandschutzzeichen/Brandmeldetelefon.jpg?raw=true) <!-- style="width: 100px" -->)                 [![Brandmelder](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Brandschutzzeichen/Brandmelder.jpg?raw=true) <!-- style="width: 100px" -->]]
- [    ( )              ( )                      ( )     ]  Fluchtweg
- [    (X)              ( )                      ( )     ]  Richtungspfeils rechts
- [    ( )              ( )                      (X)     ]  Brandmelder
- [    ( )              ( )                      ( )     ]  Notruftelefon
- [    ( )              (X)                      ( )     ]  Brandmeldetelefon


### 4. Verhalten im Brandfall

<!--style="color:red; font-size: large; font-weight: bolder"-->Was ist im Brandfall am wichtigsten?

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

<!-- data-randomize -->
- [[X]] Ruhe bewahren.
- [[X]] Andere warnen.
- [[X]] Feuerwehr rufen.
- [[ ]] Fenster öffnen, damit der Rauch entweichen kann.
- [[X]] Ausgeschilderte Fluchtwege benutzen.
- [[ ]] Sofort mit Löschen beginnen, um das Feuer im Keim zu ersticken.
- [[X]] Keine Aufzüge verwenden.
</div>
<div class="flex-child">
![Feuerloescher](img/fuenf_feuerloescher.jpg)<!-- style="width: 300px" -->
<br>
_Quelle: Pixabay, Foto-Rabe_
</div>
</section>

------

Welche Bedeutung hat dieses Piktogramm?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Rettungszeichen.Rettungsweg_Notausgang_rechts(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Brandschutzzeichen sind immer rot. Daher ist es hier bedeutungslos.
- [(X)] Fluchtweg / Notausgang.
- [( )] Brandschutztür benutzen.
</div>
</section>



### Geschafft! 🙌


<!--style="color:blue; font-size: large; font-weight: bolder"-->Tipp: <br>
Weitere Informationen und alle Sicherheitszeichen finden Sie auf der BGHM-Webseite: <br> <br> https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen 

---

![Jubel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/colorfull_jumping.jpg)<!-- style="width: 500px" --> 

_Quelle: Pixabay, geralt_

