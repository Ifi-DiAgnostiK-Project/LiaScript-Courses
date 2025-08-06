<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.4

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/ISO_7010_W002.svg/2560px-ISO_7010_W002.svg.png

comment:  Arbeitssicherheit & Gesundheitsschutz

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

title: Sicherheitszeichen

tags:
    - Arbeitssicherheit
    - Sicherheitszeichen
    - Arbeits-_und_Gesundheitsschutz

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


<!--style="color:blue; font-weight: bolder"-->Viel Erfolg!
===

![Arbeitsschutz](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/schilder_an_zaun.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, planet-fox_

## Sicherheitszeichen 

>Im Handwerk sorgen Sicherheitszeichen und der richtige Umgang mit Gefahrstoffen dafür, dass alle gesund und unfallfrei durch den Arbeitsalltag kommen.  <br> Wer die wichtigsten Zeichen kennt und Gefahrstoffe richtig erkennt, schützt nicht nur sich selbst, sondern auch andere. <br> Die Symbole zeigen Ihnen auf einen Blick, was zu tun, zu lassen oder besonders zu beachten ist.  <br> Mit dem Quiz prüfen Sie, wie fit Sie sind beim Thema Sicherheit im Betrieb. wirklich bist!<br> 

![Sicher](img/sicher_aus_schildern.jpg)<!-- style="width: 700px" --> 

_Quelle: Pixabay, succo_



### 1. Warnzeichen

<!--style="color:blue; font-weight: bolder"-->In welcher Zeile befinden sich Warnschilder?

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 1:__
</div>
<div class="flex-child">
@Gefahrstoffe.Giftig_Sehr_giftig(10)
</div>
<div class="flex-child">
@Gefahrstoffe.Entzuendlich(10)
</div>
<div class="flex-child">
@Gefahrstoffe.Umweltgefaehrlich(10)
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


### 2. Sicherheitszeichen und ihre Bedeutungen I

<!--style="color:blue; font-weight: bolder"-->Ordnen Sie die Zeichen den passenden Beschreibungen zu.

<br>



<!-- data-randomize -->
-   [[ @Warnzeichen.Elektrische_Spannung(10) ]        ( @Gebotszeichen.Handschuh(10) )                 [ @Verbotszeichen.Keine_Offene_Flamme(10) ]]
- [    (X)                                     ( )                                      ( )     ]  Warnung vor elektrischer Spannung
- [    ( )                                     (X)                                      ( )     ]  Aufforderung, Handschuhe zu tragen
- [    ( )                                     ( )                                      (X)     ]  Verbot von offenem Feuer
- [    ( )                                     ( )                                      ( )     ]  Lagerfeuerverbot


### 3. Sicherheitszeichen und ihre Bedeutungen II

<!--style="color:blue; font-weight: bolder"-->Wahr oder falsch? -- Das Symbol "Schutzbrille tragen" ist ein blaues, rundes Gebotszeichen.

<!-- data-randomize -->
- [(X)] wahr
- [( )] falsch

----

<!--style="color:blue; font-weight: bolder"-->Was bedeutet das folgende Zeichen?


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Brandschutzzeichen.Feuerloescher(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Brandmelder
- [( )] Achtung - keine Brandtür!
- [(X)] Feuerlöscher

</div>
</section>

----

<!--style="color:blue; font-weight: bolder"-->Füllen Sie den Lückentext richtig aus.

Das Zeichen mit einer laufenden Person und einem Pfeil auf grünem Hintergrund kennzeichnet einen [[ Sammelpunkt | (Notausgang) | Sani-Kasten]]. 

### 4. Zuordnungsaufgabe Sicherheitszeichen

<!--style="color:blue; font-weight: bolder"-->Ordnen Sie die abgebildeten Sicherheitszeichen dem richtigen Begriff zu:

<!-- data-randomize -->
-   [[ @Rettungszeichen.Notruftelefon(10) ]        ( @Gebotszeichen.Kopfschutz(10) )                 [ @Gefahrstoffe.Aetzend_Reizend(10) ]]
- [    ( )              ( )                      ( )     ]  Warnung vor einer Gefahr
- [    (X)              ( )                      ( )     ]  Notruftelefon
- [    ( )              ( )                      (X)     ]  Warnung vor Gefahrstoffen - ätzend
- [    ( )              ( )                      ( )     ]  Brandmelder
- [    ( )              (X)                      ( )     ]  Schutzhelm tragen


### 5. Sicherheitszeichen und ihre Bedeutungen III

<!--style="color:blue; font-weight: bolder"-->Wofür steht dieses Zeichen?


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Explosiv(15)
</div>
<div class="flex-child">

<!-- data-randomize -->
- [( )] Achtung: Komprimierte Gase!
- [(X)] Achtung: Explosiv!
- [( )] Achtung: Entzündlich!

</div>
</section>

---

<!--style="color:blue; font-weight: bolder"-->Wofür steht dieses Zeichen?


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">
@Gefahrstoffe.Oxidierend(15)
</div>
<div class="flex-child">

<!-- data-randomize -->
- [( )] Entzündbar
- [(X)] Brandfördernd, oxidierend
- [( )] Umweltgefährlich

</div>
</section>

---

<!--style="color:blue; font-weight: bolder"-->Was ist beim Umgang mit gekennzeichneten Gefahrstoffen zu beachten?


<!-- data-randomize -->
- [[ ]] Nur Fachkräfte mit einer entsprechenden Zulassung dürfen mit Gefahrstoffen arbeiten.
- [[X]] Betriebsanweisung lesen.
- [[ ]] Handschuhe sind nur nach Anweisung nötig.
- [[X]] Schutzmaßnahmen einhalten.



### Geschafft! 🙌

<!--style="color:blue; font-size: large; font-weight: bolder"-->Tipp: <br>
Weitere Informationen und alle Sicherheitszeichen finden Sie auf der BGHM-Webseite: <br> <br> https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen 

---

![Jubel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/colorfull_jumping.jpg)<!-- style="width: 500px" --> 

_Quelle: Pixabay, geralt_
