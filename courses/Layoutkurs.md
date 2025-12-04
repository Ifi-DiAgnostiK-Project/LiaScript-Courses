<!--
author: Volker Göhler
email: volker.goehler@informatik.tu-freiberg.de
language: de
narrator: German Female
version: 0.0.1
edit: true
date: 2025-12-04
comment: Kurs zum Sammeln von Layout Elementen
title: Layout Elemente Sammlung

tags:
  - Wissensspeicher
  
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css

icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/e/ef/Programming_code.jpg
attribute: title image -- Martin Vorel, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Textilpflegesymbole/refs/heads/main/makros.md

-->

# LiaScript Layout Elemente

Generell werden LiaScript Elemente nur in eine Box gerendert.
Alle weiteren Layouts können mit inklusion unserer css datei und den dort definierten Klassen realisiert werden.
Diese müssen in der preamble eingebunden werden mit:

```yaml
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css
```

## Bilder

Markdown Bilder können mit `![Alt Text/Beschreibung](bildadresse)` eingefügt werden. 

> ![Brandenburger Tor, Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/b/b1/Brandenburger_Tor_morgens.jpg)
> 
> Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons

Der Untertitle ist in diesem Fall händisch unter das Bild geschrieben.

besser!<!--style="font-size:20pt; font-weight:bold;"-->

LiaScript hat die Möglichkeit noch Bilduntertext einzufügen.`![Alt Text](bildadresse "subtitle")`

> ![Brandenburger Tor, Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/b/b1/Brandenburger_Tor_morgens.jpg "Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons")

### Größenanpassungen

Weiterhin kann die Größe des Bildes angepaßt werden. (Und weitere Aspekte die man mit CSS manipulieren kann.) `![Alt Text](URL "subtitle")<!-- style="styleelement" -->`
Dies nutzt einen html Kommentar um das `style` tag dem Bild zuzuweisen. `class` geht ebenso.
Bei Angabe von css styles ist zu beachten die einzelnen elemente mit `;` zu trennen. `style="max-width: 400px;"` Prozentangaben sind auch möglich.

> ![Brandenburger Tor, Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/b/b1/Brandenburger_Tor_morgens.jpg "Thomas Wolf, www.foto-tw.de, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons")<!-- style="width: 50%;" -->

Wenn nur eines der Attribute `width` oder `height` angegeben wird, skaliert das Bild im Verhältnis. Diese Attribute setzen die Größe auf den angegebenen Wert, was in kleineren Anzeigen (zB Handy) seltsam wirken kann. Um eine maximale Größe anzugeben kann man `max-width` bzw. `max-height` nutzen. Diese skaliert das Bild automatisch kleiner, wenn weniger Platz zur Verfügung steht. Aber es braucht dazu eine entsprechende Relationale Größenangabe `width: 100%;` zB.

<section class="flex-container" style="background-color: lightblue;">
<div class="flex-child" style="background-color: orange; width:250px;">
![Space X Dragon](https://upload.wikimedia.org/wikipedia/commons/3/33/SpaceX_Crew_Dragon_%28More_cropped%29.jpg "NASA/SpaceX Dragon Capsule")<!-- style="width:250px;"-->

`<!-- style="width:250px;"-->`
</div>
<div class="flex-child" style="background-color: lightgreen; width:250px;">
![Soyuz TMA-7](https://upload.wikimedia.org/wikipedia/commons/b/bc/Soyuz_TMA-7_spacecraft2edit1.jpg "Soyuz TMA-7")<!-- style="max-width:500px; width:100%;"-->

`<!-- style="max-width:500px; width:100%;"-->`
</div>
</section>

### Position des Bildes auf der Seite

Eine Zentrierung ist über prozent semantik ebenso möglich. Die Prozente beziehen sich auf die Breite des Containers in dem das Bild aktuell existiert. `<!-- style="width: 50%; margin-left: 25%;" -->` z.B. schiebt dies das Bild um 25% nach rechts.

Der `margin` kontrolliert einen Bereich um einen Block (div) in dem keine anderen Objekte sein dürfen, also wie das weiße auf einer Buchseite bis zum textblock. Man kann mit `margin: 0 0 0 0;` das anpassen (dieser Fall löscht alle margins). Jedes dieser Zahlen steuert einen der Bereiche. In Reihenfolge “oben”, “rechts”, “unten”, “link”.
Angaben sind zB in `px`, `%` oder auch `cm` möglich.  
Z.B. 
- `margin: 1cm 100px 0 20px;`
- `margin: 2% 3% 10% 2%;`
Ebenso ist es möglich nur die speziellen Werte anzugeben:
- `margin-bottom: 10px;`
- `margin-top: 50cm;`
- `margin-left: -5em;`
- `margin-right: -20cm;`

Um das Bild also "runterzuschieben" muss der top margin angepasst werden.

`<!-- style="margin-left:20px; margin-top:10px;" -->`

```ascii
    +-------------------+
    |           10 px   |
    |      +------------|
    |      |            |
    |      |            |
    |  20px|    Bild    |
    |      |            |
    |      |            |
    +-------------------+

```

### LiaScript Makros für Bilder

Das DiAgnostiK Projekt hat eine Reihe von Makrobibliotheken um Bilder einzubinden. 
Um Bilder zum Beispiel aus  unserem ISO 7010 Repository zu importieren:

> `@Brandschutzzeichen.Richtungspfeil_Rechts(10)`

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

Eine komplette Liste aller Symbole findet man in den entsprechenden Repos.

- [Textilpflegesymbole](https://liascript.github.io/course/?https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Textilpflegesymbole/refs/heads/main/makros.md)
- [Bildersammlung](https://liascript.github.io/course/?https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md)
- [Piktogramme](https://liascript.github.io/course/?https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md)
- [Holzarten](https://liascript.github.io/course/?https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md)

Mit `.src` hinter dem Befehl, anstelle der runden Klammern, kann der Pfad zu der Datei ausgegeben werden.

> `@Brandschutzzeichen.Richtungspfeil_Rechts.src`

@Brandschutzzeichen.Richtungspfeil_Rechts.src

## Layouts

Neben der möglichkeit MarkdownElemente mit HTML Kommentaren style informationen zu übergeben`<!--style="something"-->`, können wir auch direkt HTML Elemente und deren Attribute spezifizieren.
`<div class="a class" style="style infos">inhalt</div>`
Dabei ist zu beachten die Elemnte (`<div>` zB) wieder zu schließen (`</div>`).

Die Style Informationen in den Kommentaren können über einem Markdownelement stehen und gelten dann für alles unten drunter, oder hinter einem Markdownelement und gelten dann nur für dieses.

<!-- style="background-color: white; color:orange;"-->
> oranger Kommentar

```
<!-- style="background-color: white; color:orange;"-->
> oranger Kommentar
```

><!-- style="background-color: white; color:orange;"--> oranger Kommentar

```
><!-- style="background-color: white; color:orange;"--> oranger Kommentar
```

> oranger Kommentar<!-- style="background-color: white; color:orange;"-->

```
> oranger Kommentar<!-- style="background-color: white; color:orange;"-->
```

### Text Nebeneinander (Flex)

Wir nutzen die flex styles:

```html
<section class="flex-container">
<div class="flex-child" style="min-width: 200px; width: 50%;">
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)

</div>
<div class="flex-child" style="min-width: 200px; width: 50%;">

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

</div>
</section>
```

<section class="flex-container">
<div class="flex-child" style="min-width: 200px; width: 50%;">
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)

</div>
<div class="flex-child" style="min-width: 200px; width: 50%;">

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

</div>
</section>

Aber Achtung wenn horizontal nicht genug Platz ist werden die Container umgebrochen! Wenn ich 3 Container a 300px breite reserviere, aber nur 750 px horizontaler Platz bereits steht sind nur die Container 1 und 2 in der selben Zeile und der dritte wird umgebrochen.

### Umbrüche

Das HTML Elemente `<br>` sorgt für einen Zeilenumbruch, aber Achtung dass kann für Probleme bei anderen Bildschirmauflösungen sorgen. Lieber die style margin semantic nutzen wenn es um blosse Abstände geht.

### Farben (Hinter- und Vordergrund)

Mit `style="background-color: farbe;"` kann die Hintergrundfarbe eines Elements eingestellt werden. Farbnamen und html Farbcodes werden dabei akzeptiert. Die Farbcodes sind Rot Grün BLau kodiert und in Hexadecimal.

<div style="background-color: #FF0000; width:100px;">
Red, #FF0000
</div>
<div style="background-color: #00FF00; width:100px;">
Green, #00FF00
</div>
<div style="background-color: #0000FF; width:100px; color: white;">
Blue, #0000FF
</div>
<div style="background-color: #A090FF; width:100px; color: white;">
#A090FF
</div>
Vordergrundfarben können auf die selbe Art mit `style="color: farbe;"` eingestellt werden.

Dies zum Beispiel für einen Markdown Kommentar `> text`

<!--style="background-color:cyan;"-->
> text

```
<!--style="background-color:cyan;"-->
> text
```
also direkt darüber schreiben. Falls viele Änderungen notwendig sind, lieber eine Klasse im css file schreiben.

Dies funktioniert auch direkt für Texte.

<!-- style="font-weight: bolder; font-size: 20pt; color: #A00000;"-->
Text der rot ist

```
<!-- style="font-weight: bolder; font-size: 20pt; color: #A00000;"-->
Text der rot ist
```

Oder nur ein rotes<!-- style="font-weight: bolder; font-size: 20pt; color: #A00000;"--> Wort.

```
Oder nur ein rotes<!-- style="font-weight: bolder; font-size: 20pt; color: #A00000;"--> Wort.
```

