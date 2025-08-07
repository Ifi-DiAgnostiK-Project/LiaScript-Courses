<!--

author:   Hilke Domsch

email:    hilke.domsch@gkz-ev.de

version:  0.0.4

language: de

narrator: Deutsch Male

edit: true
date: 2025-08-01

title:  Grundkurs Maler/Lackierer G-ML-24
comment:  Grundkurs Maler/Lackierer

tags: 
  - Maler
  - Grundkurs

icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: img/farben.jpg

attribute: Title Image by Pixabay, Darkmoon Art

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md

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

# Grundstufe Maler- und Lackiererhandwerk G-ML-24  🧑‍🎨

![Pinsel+Farben](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/farben.jpg)<!-- style="width: 800px" -->

_Quelle: Pixabay, Darkmoon Art_

## Überprüfungsaufgaben

<!--style="color:grey; font-size: large; font-weight: bolder"-->Sie haben in den letzten Tagen Werkzeuge und Grundhandgriffe im Maler- und Lackiererhandwerk kennengelernt und eingeübt. <br> <br> Überprüfen Sie Ihr Wissen - viel Erfolg!


<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

@Maler_Planung.Uebung3_Ergebnis(70) 

</div>
<div class="flex-child">
_Quelle aller Bilder: HWK Dresden, Florian Riefling_

</div>
</section>

### Typische Werkzeuge im Maler- und Lackiererhandwerk I

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

<!--style="color:grey; font-size: large; font-weight: bolder"-->Wie nennt man dieses Werkzeug?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

![Abreißblech](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/spachtel.jpg)<!-- style="width: 300px" -->

</div>
<div class="flex-child">
<!-- data-randomize -->
- [[ ]] Kamm
- [[X]] Abreißblech
- [[X]] Rakel
- [[X]] Schwedenblech
- [[ ]] Blockschiene
- [[X]] Flächenrakel

</div>
</section>

### Typische Werkzeuge im Maler- und Lackiererhandwerk II


<!--style="color:grey; font-size: large; font-weight: bolder"-->Wie nennt man dieses Werkzeug?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

![Tapezierbürste](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/buerste.jpg)<!-- style="width: 300px" -->

</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Kehrbesen
- [( )] Wandbürste
- [(X)] Tapezierbürste

</div>
</section>

### Typische Werkzeuge im Maler- und Lackiererhandwerk III


<!--style="color:grey; font-size: large; font-weight: bolder"-->Wie nennt man dieses Werkzeug?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

![Schraegstrichzieher](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/kleiner_pinsel.jpg)<!-- style="width: 300px" -->

</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Ringpinsel
- [( )] Heizkörperpinsel
- [(X)] Schrägstrichzieher

</div>
</section>



### Wichtige Arbeitsabläufe für allgemeine Decken- und Wandgestaltungen

<!--style="color:grey; font-weight: bolder"-->In welcher Reihenfolge führen Sie den Auftrag aus? <br> Ziehen Sie die einzelnen Arbeitsschritte in die richtige Reihenfolge. <br> An oberster Stelle steht der erste Arbeitsschritt.

------------------


<!-- data-randomize -->
@dragdroporder(@uid,Makulatur/Glattvlies kleben.|Decken- und Wandanschlüsse beschneiden und Schlussbeschichtung applizieren.|Wand- und Deckenflächen nachwaschen.|Wand- und Deckenflächen schleifen/entstauben.|Wand- und Deckenflächen mit unpigmentierter sowie wasserverdünnter Grundbeschichtung grundieren.|Nicht tragfähige Beschichtung und Beläge von den Wand- und Deckenflächen entfernen.|Decken- und Wandanschlüsse beschneiden und Zwischenbeschichtung applizieren.|Wand- und Deckenflächen abkleben/abdecken.|Wand- und Deckenflächen spachteln.|Tapezieren von Raufaser an der Deckenfläche.,Nicht tragfähige Beschichtung und Beläge von den Wand- und Deckenflächen entfernen.|Wand- und Deckenflächen nachwaschen.|Wand- und Deckenflächen spachteln.|Wand- und Deckenflächen schleifen/entstauben.|Wand- und Deckenflächen mit unpigmentierter sowie wasserverdünnter Grundbeschichtung grundieren.|Makulatur/Glattvlies kleben.|Tapezieren von Raufaser an der Deckenfläche.|Wand- und Deckenflächen abkleben/abdecken.|Decken- und Wandanschlüsse beschneiden und Zwischenbeschichtung applizieren.|Decken- und Wandanschlüsse beschneiden und Schlussbeschichtung applizieren.)



### Wichtige Arbeitsabläufe für Gestaltungsflächen: Wände und Sockel

<!--style="color:grey; font-weight: bolder"-->In welcher Reihenfolge führen Sie den Auftrag aus? <br> Ziehen Sie die einzelnen Arbeitsschritte in die richtige Reihenfolge. <br> An oberster Stelle steht der erste Arbeitsschritt.

------------------

<!-- data-randomize -->
@dragdroporder(@uid,Gestaltungswand: Flächengliederung abmessen und anzeichnen.|Farbflächen mit Pinsel deckend farbig auslegen.|Fläche der Wickeltechnik mit Strichzieher und Lineal einrahmen.|Radius auf der rechten Seite anzeichnen und deckend farbig auslegen.|Abklebung und Abdeckung entfernen. Abfälle sachgerecht entsorgen und Werkzeuge und Arbeitsmittel reinigen.|Farbflächen mit Strichzieher und Lineal beschneiden.|Wickeltechnik über die gesamte Gestaltung mit Latexbindemittel -glänzend- ausführen.|Sockelfläche einmessen und abkleben/abdecken.|Wickeltechnik zweifarbig im Sockelbereich ausführen.|Kontrastlinien mit Lineal und Strichzieher ziehen.,Sockelfläche einmessen und abkleben/abdecken.|Gestaltungswand: Flächengliederung abmessen und anzeichnen.|Farbflächen mit Strichzieher und Lineal beschneiden.|Farbflächen mit Pinsel deckend farbig auslegen.|Kontrastlinien mit Lineal und Strichzieher ziehen.|Radius auf der rechten Seite anzeichnen und deckend farbig auslegen.|Wickeltechnik über die gesamte Gestaltung mit Latexbindemittel -glänzend- ausführen.|Wickeltechnik zweifarbig im Sockelbereich ausführen.|Fläche der Wickeltechnik mit Strichzieher und Lineal einrahmen.|Abklebung und Abdeckung entfernen. Abfälle sachgerecht entsorgen und Werkzeuge und Arbeitsmittel reinigen.)

### Beschaffenheit von Untergründen

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

-------------------

<!--style="color:grey; font-size: large; font-weight: bolder"-->Wie sollte ein Untergrund beschaffen sein, damit dieser beschichtet oder tapeziert werden kann?
===



<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

<!-- data-randomize -->
- [[X]] sauber
- [[X]] trocken
- [[X]] fest
- [[X]] tragfähig
- [[X]] frei von trennenden Substanzen
- [[X]] gleichmäßig saugfähig
- [[ ]] Haarrisse sind unerheblich
- [[ ]] leicht angeraute Unterfläche, damit es besser haftet
- [[ ]] leicht angefeuchtet, damit das Auftragen leichter geht

</div>
<div class="flex-child">
@Maler_Taetigkeiten.Koje_Vorbereitung(25)

</div>
</section>


### Haftfestigkeit alter Anstriche

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

-------------------

<!--style="color:grey; font-size: large; font-weight: bolder"-->Mit welchen Methoden kann die Haftfestigkeit alter Anstriche geprüft werden?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

<!-- data-randomize -->
- [[X]] Abriebprobe/Wischprobe mit der Hand oder einem Tuch
- [[ ]] Abkärchern
- [[X]] Kratzprobe mit dem Spachtel
- [[X]] Tragfähigkeitsprüfung mit Klebebandtest
- [[ ]] Besprühen der Wand mit Parfüm oder Duftstoffen
- [[ ]] Abklopfen mit dem Finger
- [[ ]] Farbauftragstest

</div>
<div class="flex-child">
![Maler](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/knetfigur_anstreicher.jpg)<!-- style="width: 300px" --> 
<br>
 _Quelle: Pixabay, Ralphs-Fotos_

</div>
</section>


### Saugfähigkeit eines Untergrundes



<!--style="color:grey; font-size: large; font-weight: bolder"-->Wie prüft man am besten die Saugfähigkeit eines Untergrunds?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

<!-- data-randomize -->
- [(X)] Benetzungsprobe mit Wasser
- [( )] Farbauftragstest
- [( )] Kratzprobe mit Messer
- [( )] Wischprobe mit trockenem Tuch

</div>
<div class="flex-child">
![Untergrund](img/putz.jpg)<!-- style="width: 300px" --> 
<br>
 _Quelle: Pixabay, geralt_

</div>
</section>

### Feuchtigkeitsmessung 

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

-------------------

<!--style="color:grey; font-size: large; font-weight: bolder"-->Wann ist eine Feuchtigkeitsprüfung sinnvoll?
===

<section class="flex-container" style="padding: 1rem;">
<div class="flex-child" style="min-width:200px;">

<!-- data-randomize -->
- [[X]] bei sichtbarem oder vermuteten Schimmelbefall
- [[X]] bei sichtbaren oder vermuteten Wasserschäden
- [[X]] wenn dunkle Flecken an den Wänden sichtbar sind
- [[X]] bei einem muffigen Geruch
- [[ ]] immer - auch wenn die Umgebung trocken ist
- [[ ]] Eine Feuchtigkeitsprüfung ist zugleich eine Temperaturmessung und daher immer sinnvoll.
- [[ ]] Eine Feuchtigkeitsprüfung geht jedem Farbanstrich voraus, um die Haftfestigkeit zu prüfen. 

</div>
<div class="flex-child">
![Wand streichen](img/malerrolle.jpg)<!-- style="width: 200px" --> 
<br>
 _Quelle: Pixabay, Giordano_

</div>
</section>



### Prüfgeräte für Untergrundprüfungen I

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

-------------------

<!--style="color:grey; font-size: large; font-weight: bolder"-->Welche Prüfgeräte oder Hilfsmittel werden häufig bei Untergrundprüfungen im Malerhandwerk eingesetzt?
===

<!-- data-randomize -->
- [[ ]] Rückprallbolzen
- [[ ]] Haftmessgerät
- [[ ]] CO2-Messgerät
- [[X]] Hydrometer
- [[X]] Gitterschnitt
- [[X]] Profometer (Betonüberdeckung)
- [[X]] Schichtdickenmessgerät (Lack)
- [[X]] Lupe


### Prüfgeräte für Untergrundprüfungen II

<!--style="color:red; font-size: huge"-->Hinweis: Es können mehrere Antworten richtig sein!

-------------------

<!--style="color:grey; font-size: large; font-weight: bolder"-->Welche der folgenden Geräte oder Werkzeuge gehören typischerweise zu einem Untergrundprüfkoffer?
===

<!-- data-randomize -->
- [[X]] Meißel
- [[X]] Taschenmesser
- [[X]] Hammer
- [[ ]] Föhn
- [[X]] Spritzflasche
- [[ ]] mobiler Gasbrenner


### Geschafft 🎉

![Jubel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/colorfull_jumping.jpg)<!-- style="width: 500px" --> 

_Quelle: Pixabay, geralt_
