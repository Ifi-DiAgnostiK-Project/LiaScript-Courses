<!--
author: Volker Göhler
email:    volker.goehler@informatik.tu-freiberg.de
language: de
narrator: German Female
version: 0.0.3
comment: this is only a test for image sizes in conjunction with quizes

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md

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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/raw/refs/heads/main/courses/gefahrensymbole_gr%C3%B6%C3%9Fen_test_v2.md)

# Quiztest

## Bild über Quiz

@Brandschutzzeichen.Brandmelder(10)

Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

---------------------

## Layout daneben

Wir nutzen flex-container und flex-child, um die Bilder nebeneinander zu platzieren. Dies sind HTML Elemente, die bis zu ihrem Ende `<div></div>` interpretieren werden und dann geschlossen sind.

> An Markdown Images können wir den Container als Kommentar drüber schreiben.
> Die minimalen Breiten können mit dem `style: min-width` Attribut gesetzt werden, damit die Bilder nicht zu klein werden.
> Um das Bild selber in der Größe zu verändern können wir einen `style: width` tag anhängen, ebenfalls als html Kommentar.

```html
<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Bildbeschreibung](Bildadresse)<!--style="width: 200px;"-->

<div class="flex-child" style="min-width: 250px">

Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandleiter
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>
```

<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/img/Brandschutzzeichen/Feuerleiter.jpg)<!--style="width: 200px;"-->

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandleiter
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>

----------------------

Beim einbinden der Bilder als Makros `@Kategorie.Bild(Größe)` müssen wir das Bild auch mit einem div umschließen, damit es in der Flexbox funktioniert.

```html
<section class="flex-container">

<div class="flex-child" style="min-width: 250px">
@Brandschutzzeichen.Brandmeldetelefon(15)
</div>

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmeldetelefon
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>
```

<section class="flex-container">

<div class="flex-child" style="min-width: 250px">
@Brandschutzzeichen.Brandmeldetelefon(15)
</div>

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmeldetelefon
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>

-----------------------

# Vorlesen von Quizes

Zum Vorlesen der Aufgabe können wir einen Kommentar verwenden. Diesen unter das Quiz packen.
Die Zahl steuert die Reihenfolge der Vorlesung.

```markdown
-> Quiz <-

<!-- --{{0}}--
Hier steht unser Text, der vorgelesen werden soll.
-->

```


1. Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?
===

- [( )] Mutterschutz
- [(X)] Schutz vor Gefahren am Arbeitsplatz
- [( )] Sportunfälle

<!-- --{{0}}--
Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?
a. Mutterschutz b. Schutz vor Gefahren am Arbeitsplatz c. Sportunfälle
--> 

--{{1}}--
Dieser Text steht auf der Seite und wird vorgelesen.

<!-- --{{2}}--
Gratulation, Sie haben die Aufgabe erfolgreich gelöst.
--> 
