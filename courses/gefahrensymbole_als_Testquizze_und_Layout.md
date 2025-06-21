<!--
author: Hilke Domsch
title: Gefahrensymbole als Testquizze und Layout
comment: Hilkes Fragen am 20.05.25, mit Volkers Antworten
version: 0.0.3
import: https://raw.githubusercontent.com/wenik35/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/wenik35/LiaScript_ImageQuiz/refs/heads/main/README.md
-->


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
@end
-->
# LiaScript Badges


[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/main/gefahrensymbole_als_Testquizze_und_Layout.md)

[![GitHub](https://img.shields.io/badge/Ansehen%20auf-GitHub-181717?logo=github)](https://github.com/vgoehler/DiAgnostiK_LiaScript/blob/main/gefahrensymbole_als_Testquizze_und_Layout.md)

[![Raw](https://img.shields.io/badge/Raw-Inhalt-blue)](https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/main/gefahrensymbole_als_Testquizze_und_Layout.md)

# Testquizzes und Layout

__Welches dieser Zeichen ist ein Rettungszeichen?__
===

 

> ❓_Bilder sind nicht automatisch verkleinert. Ich hätte gern 3 Bilder nebeneinander._  
 ✔


> ❓_Wie kann ich Fragen und ihre Antworten zufällig mischen?_
✔

> nutze `<!-- data-randomize -->` direkt über den Fragen (Single oder Multichoice)


Wieviel Apostel hatte Jesus
====

<!-- data-randomize -->
- [( )] 0
- [( )] 5
- [(X)] 12
- [( )] 666
- [( )] 48

---

#️⃣ nebeneinander Beispiel
===

> Hierzu brauchen wir die Style Angaben in der Preamble. Alles muss in einen section container (der / vor dem element beendet es wieder) und jedes element muss in ein div. Das Bild kann den Kommentar direkt drüber bekommen

 <section class="flex-container">

<!-- class="flex-child" style="min-width: 250px; " -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandmelder.jpg?raw=true)<!-- style="width: 150px;"-->

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>

1️⃣ nebeneinander Beispiel -- version 2
===

> Aber! wenn ein Text vor dem bild steht braucht es auch so ein div!

 <section class="flex-container">

<div class="flex-child" style="min-width: 250px">
mein toller Text!
===
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandmelder.jpg?raw=true)<!-- style="width: 150px;"-->
</div>

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich?
===
- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>

---

> Wenn du dich jetzt fragst woher die icons herkommen. dann drück im Live Editor mal :  
🤖⚒

---

## einige Aufgaben Beispiele

> ich nutze hier die floats (also die schwebenden Container) um die Bilder mit Text nebeneinander zu positionieren. Das ist sehr breiten Abhängig.

Frage: Welches der Bilder ist ein Gefahrenzeichen?
=======

<section class="flex-container">
<div class="flex-child" style="min-width: 100px">
Bild a) @Rettungszeichen.Erste_Hilfe(10)
</div>
<div class="flex-child" style="min-width: 100px">
Bild b) @Warnzeichen.Automatischer_Anlauf(10)
</div>
<div class="flex-child" style="min-width: 100px">
Bild c) @Brandschutzzeichen.Brandbekaempfung(10)
</div>
</section>

- [[ ]] Bild a
- [[x]] Bild b
- [[x]] Bild c


--- 

Frage: Welches der Bilder ist ein Erste Hilfe Zeichen?
====

> Üblicherweise nutzt man Tabellen nicht zum Formatieren von Inhalten. Da gucken die Webdesigner böse. :)

| Bild 1 | Bild 2 | Bild 3 |
| -------- | :------: | -------: |
| @Rettungszeichen.Erste_Hilfe(10)| @Warnzeichen.Automatischer_Anlauf(10) | @Brandschutzzeichen.Brandbekaempfung(10)|

- [(X)] Bild 1
- [( )] Bild 2
- [( )] Bild 3

---

Frage: Welches der Bilder ist ein Erste Hilfe Zeichen?
====

> Hier mal mit der Matrix Komponente! Man könnte auch den Text weglassen.

[[@Rettungszeichen.Erste_Hilfe(10)] [@Warnzeichen.Automatischer_Anlauf(10)] [@Brandschutzzeichen.Brandbekaempfung(10)]]
[    [X]           [ ]             [ ]     ]  Erste Hilfe Zeichen



---

Aufgabe: Wähle die Warnzeichen!
====

> Drag&Drop ist auch möglich

@dragdropmultipleimages(@uid,@Warnzeichen.Laserstrahl.src|@Warnzeichen.Automatischer_Anlauf.src,@Leitern.Nur_eine_Person.src|@Brandschutzzeichen.Brandbekaempfung.src|@Rettungszeichen.Erste_Hilfe.src)


---

Aufgabe: Wähle die Warnzeichen!
====

> Oder direkt anklicken

@selectimages(@uid,10,@Warnzeichen.Laserstrahl.src|@Warnzeichen.Automatischer_Anlauf.src,@Leitern.Nur_eine_Person.src|@Brandschutzzeichen.Brandbekaempfung.src|@Rettungszeichen.Erste_Hilfe.src)
