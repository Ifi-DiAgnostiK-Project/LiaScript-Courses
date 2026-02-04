<!--
author: Volker Göhler
email: volker.goehler@informatik.tu-freiberg
version: 0.0.3
language: de
narrator: Deutsch Female
date: 2025-06-27
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

tags:
    - tischler
    - gefahrstoffe

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
@end

-->

# Gefahrstoffe im Tischlerhandwerk

Willkommen!

Der Umgang mit Gefahrstoffen ist im Tischlerhandwerk fester Bestandteil des Arbeitsalltags, zum Beispiel beim Arbeiten mit Lacken, Leimen oder Reinigungsmitteln. Um sich selbst und andere zu schützen, ist es entscheidend, die Kennzeichnungen und Symbole dieser Stoffe zu kennen und richtig zu deuten. Dieses Quiz unterstützt Sie dabei, Ihr Wissen zu überprüfen und zu festigen.

![Rein Sikk, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/c/c4/Aru_Grupp_02.jpg)

_Rein Sikk, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons_<!--style="font-size:x-small;"-->

## 1. Wie sehen Gefahrstoffzeichen typischerweise aus?

<section class="flex-container">
<div class="flex-child">
<!-- data-randomize -->
- [( )] Blaues Quadrat mit weißem Symbol
- [( )] Grünes Rechteck mit weißem Symbol
- [(X)] Weiße Raute, mit rotem Rand und schwarzem Symbol
- [( )] Gelbes Dreieck mit schwarzem Symbol
</div>
<!--class="flex-child"-->
![](https://upload.wikimedia.org/wikipedia/commons/3/32/Mathematrix_book_02.svg)

</section>

## 2. Dieses Symbol steht für:

<section class="flex-container">
<div class="flex-child">
@Gefahrstoffe.Giftig_Sehr_giftig(15)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Umweltgefährlich
- [(X)] Giftig oder sehr giftig
- [( )] Explosiv
</div>
</section>

---

## 3. Wofür steht dieses Symbol?

<section class="flex-container">
<div class="flex-child">
@Gefahrstoffe.Oxidierend(15)
</div>
<div class="flex-child">

<!-- data-randomize -->
- [( )] Entzündlich
- [( )] Ätzend / Reizend
- [(X)] Oxidierend
</div>
</section>

---

## 4. Lacke und Lösungsmittel sind häufig...

<!-- data-randomize -->
- [( )] Nicht kennzeichnungspflichtig
- [(X)] Brennbar / leicht entzündlich
- [( )] Explosiv

---

## 5. Welches Symbol warnt vor Krebsrisiko?

<!-- data-randomize -->
- [(X)] @Gefahrstoffe.Krebserregend_Gesundheitsschaedlich(10)
- [( )] @Gefahrstoffe.Umweltgefaehrlich(10)
- [( )] @Gefahrstoffe.Giftig_Sehr_giftig(10)

---

## 6. Welches Symbol bedeutet „brandfördernd“?

<!-- data-randomize -->
- [(X)] @Gefahrstoffe.Oxidierend(10)
- [( )] @Gefahrstoffe.Explosiv(10)
- [( )] @Gefahrstoffe.Entzuendlich(10)

---

## 7. Ordnen Sie das Symbol der richtigen Bedeutung zu?

<!-- data-randomize -->
- [[@Gefahrstoffe.Aetzend_Reizend(10)] (@Gefahrstoffe.Reizend_Gesundheitsschaedlich(10)) [@Gefahrstoffe.Komprimierte_Gase(10)]]
- [    [X]           [ ]             [ ]     ]  Kann schwere Haut- oder Augenschäden verursachen
- [    [ ]           [X]             [ ]     ]  Kann die Gesundheit bei längerem Kontakt beeinträchtigen
- [    [ ]           [ ]             [X]     ]  Enthält Gas unter hohem Druck
- [    [ ]           [ ]             [ ]     ]  Unterstützt die Verbrennung anderer Stoffe  <!-- absichtlich falsch -->
- [    [ ]           [ ]             [ ]     ]  Kann sich ohne Zündquelle selbst entzünden  <!-- absichtlich falsch -->

---

## 8. Welche Stoffe sind mit diesem Zeichen gekennzeichnet?

<section class="flex-container">
<div class="flex-child">
@Gefahrstoffe.Umweltgefaehrlich(20)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Holzstaub aus der Werkstatt
- [(X)] Chemikalien, die Pflanzen und Tiere im Wasser gefährden können
- [( )] Gasbehälter mit hohem Druck
- [( )] Materialien, die elektrischen Strom leiten
- [( )] Stoffe, die bei Hitze leicht explodieren
</div>
</section>


---

## 9. Welche Schutzmaßnahmen sind bei Stoffen mit folgendem Zeichen zu ergreifen?
<section class="flex-container">
<div class="flex-child">
@Gefahrstoffe.Krebserregend_Gesundheitsschaedlich(20)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [(X)] Tragen von Atem-, Haut- und Augenschutz sowie Arbeiten in gut belüfteten Bereichen
- [( )] Kontakt möglichst vermeiden und nur mit geeigneten Schutzhandschuhen arbeiten
- [( )] Stoffe in geschlossenen Systemen verwenden und Dämpfe absaugen
- [( )] Regelmäßige ärztliche Vorsorgeuntersuchungen einplanen
- [( )] Nur bei starkem Regen im Freien verwenden  <!-- weit weg von der richtigen Antwort -->
</div>
</section>

---

## Fülle den Lückentext aus.

<!-- data-randomize -->
Im Tischlerhandwerk kommen häufig Stoffe wie Lacke und [[ (Leime) | Schrauben | Holzarten ]] zum Einsatz, die Gefahrstoffe enthalten können.
Besonders wichtig ist es, beim Arbeiten mit Gefahrstoffen immer auf die [[ (Kennzeichnung) | Verpackungsgröße | Herkunft ]] zu achten.
Viele dieser Stoffe sind leicht [[ (entzündlich) | wasserlöslich | geruchsneutral ]] und erfordern besondere Vorsicht.
Zur sicheren Anwendung gehört auch das Tragen von [[ (Schutzhandschuhen) | Sandalen | Mützen ]] bei direktem Kontakt.

---

## Vielen Dank! 👐

Sie haben das Quiz erfolgreich absolviert. Sie können weiterführendes Materialien auf den Seiten der BGHM und der Berufsgenossenschaften einsehen.

