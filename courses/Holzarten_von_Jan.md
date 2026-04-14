<!--
author:   Jan Franke; Volker Göhler

email:    jan.franke@hwk-dresden.de

version:  0.0.12

language: de

narrator: Deutsch Female

edit: true
date: 2025-06-24
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Wood_of_a_Picea_abies_03.jpg/1920px-Wood_of_a_Picea_abies_03.jpg

attribute: Title Image By Kritzolina - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=128991156


comment:  Der ursprüngliche Kurs von Jan

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md

title: Holzarten - Alter Kurs

tags: Tischler

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

@Fichte: @Hoelzer1.Fichte.src
@Balsa:  @Hoelzer1.Balsa.src
@Ahorn: @Hoelzer1.Ahorn.src
@Pockholz: @Hoelzer1.Pockholz.src

-->

## Überprüfe hier dein Wissen zu den Holzarten

__Probier dich einfach mal aus__ 😊.

### Bevor wir mit dem Quiz beginnen, kannst du dich im Film informieren, wie aus einem Baumstamm ein Brett entsteht

!?[](https://youtu.be/veoFy8ty9Q8?si=p5xSav-HDr9Avk5n)

Welche Holzart erkennst du hier?
===

@Hoelzer.Ahorn(10)

- [[x]] Ahorn
- [[ ]] Fichte
- [[ ]] Kiefer
- [[ ]] Zeder

@Hoelzer.Birke(10)

- [[ ]] Ahorn
- [[x]] Birke
- [[ ]] Rüster
- [[ ]] Lärche

<section class="flex-container">
<div class="flex-child">

@Hoelzer.Pappel(10)

</div>
<div class="flex-child">

- [[x]] Pappel
- [[x]] Espe
- [[ ]] Ahorn
- [[x]] Aspe

</div>
</section>


__Fülle den Lückentext aus.__
===

<!-- data-randomize -->
Eiche ist ein sehr wiederstandsfähiges Holz und lässt sich daher sehr gut für [[ Schneidbretter | (Außenbereiche) | Brandschutzverkleidungen]] verwenden.

Lärche ist aufgrund seiner[[ groben Holzstruktur |   Astfreiheit   | (hohen Harzhaltigkeit) ]] für Außenverkleidungen sehr gut geeignet.

Ahorn ist wegen seiner [[ breiten wuchses |   hellen Färbung   | (Härte) ]] für beanspruchte Arbeitsflächen nutzbar.

Die Buche  wird sehr gerne aufgrund ihrer [[ wilden Wuchsform |   (gleichmäßigen Färbung)  | Langlebigkeit ]] für Furniere verwendet.

## Und weiter gehts mit dem Quiz

Schaue dir dazu den nächsten Film an.


!?[](https://youtu.be/QP7nOjA9si8?si=LXjAJXKKXkOx9Sim)

- [ [sehr hart] [hart] [weich] [sehr weich]  ]
- [  ( )  (x)  ( )   ( ) ] __Ahorn__ @Hoelzer.Ahorn(10)
- [  ( )  ( )  ( )  (x) ] __Balsa__ @Hoelzer.Balsa(10)
- [  ( )  ( )  (x)  ( ) ] __Fichte__ @Hoelzer.Fichte(10)
- [  (x)  ( )  ( )  ( ) ] __Pockholz__ @Hoelzer.Pockholz(10)


## Volkers Quiz - ich zeig hier mal die Bilder Quizes von Niklas:

Bilder Quiz
=======

> Hier das Bilder Auswahl Quiz von Niklas
> `@selectimages(@uid, grösse, richtig, falsch)`
> Beachtet dazu den import im Kopf `LiaScript_ImageQuiz`

- **@uid**: ist wichtig damit das Quiz funktioniert
- **grösse**: ist die Grösse der Bilder in Zeilenhöhe des Textes
- **richtig**: ist das Bild, das richtig ist
- **falsch**: sind die Bilder, die falsch sind

Alle Bilder sind die Pfadangaben zu Bildern, die aktuell im Ordner `img/` liegen. Bilder können mit `|` getrennt werden, um mehrere Bilder anzugeben.

Was ist der Ahorn?
=====

@selectimages(@uid, 10, @Ahorn, @Balsa|@Fichte)

Drag and Drop Quiz
=======

> Hier das Drag and Drop Quiz von Niklas
> `@dragdropmultiple(@uid, richtig, falsch)`
> Beachtet dazu den import im Kopf `LiaScript_DragAndDrop_Template`

- **@uid**: ist wichtig damit das Quiz funktioniert
- **richtig**: sind die Bilder, die richtig sind
- **falsch**: sind die Bilder, die falsch sind

Alle Bilder sind die Pfadangaben zu Bildern, die aktuell im Ordner `img/` liegen. Bilder können mit `|` getrennt werden, um mehrere Bilder anzugeben.

Ziehe alle Hardhölzer in die Box
===

> weiss nicht was hier die richtigen sind :) Hab jetzt Ahorn und Pockholz genommen aus dem matrix quiz

@dragdropmultiple(@uid, @Ahorn|@Pockholz, @Balsa|@Fichte)


