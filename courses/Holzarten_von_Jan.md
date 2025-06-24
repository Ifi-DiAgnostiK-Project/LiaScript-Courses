<!--
author:   Jan Franke; Volker Göhler

email:    jan.franke@hwk-dresden.de
 
version:  0.0.1
 
language: de
 
narrator: Deutsch Female

edit: true
date: 2025-06-24
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png

comment:  Quiz zu Eigenschaften Holz

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

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
 

# Probier dich einfach mal aus :-)



## Überprüfe hier dein Wissen zu den Holzarten

### Bevor wir mit dem Quiz beginnen, kannst du dich im Film informieren, wie aus einem Baumstamm ein Brett entsteht

!?[](https://youtu.be/veoFy8ty9Q8?si=p5xSav-HDr9Avk5n)

Welche Holzart erkennst du hier?

![](img/78c4079dabd58afc91d0be6ebd3e3f389c8af08a.jpeg)

- [[x]] Ahorn
- [[ ]] Fichte
- [[ ]] Kiefer
- [[ ]] Zeder

![](img/5e520f8694d34696f83bf568388b0dfd1e300b84.jpeg)

- [[ ]] Ahorn
- [[x]] Birke
- [[ ]] Rüster
- [[ ]] Lärche

<section class="flex-container">
<div class="flex-child">
![](img/834543b7e8b5418443110258628f76915d6eae70.jpeg)<!-- style="width: 250px" -->
</div>
<div class="flex-child">
![](img/71b1d7fab8e7554438c16292c49261894df41bff.jpeg)<!-- style="width: 250px" -->
</div>
</section>

- [[x]] Pappel
- [[x]] Espe
- [[ ]] Ahorn
- [[x]] Aspe

__Fülle den Lückentext aus.__
===

<!-- data-randomize -->
Eiche ist ein sehr wiederstandsfähiges Holz und lässt sich daher sehr gut für [[ Schneidbretter | (Außenbereiche) | Brandschutzverkleidungen]] verwenden.

Lärche ist aufgrund seiner[[ groben Holzstruktur |   Astfreiheit   | (hohen Harzhaltigkeit) ]] für Außenverkleidungen sehr gut geeignet.

Ahorn ist wegen seiner [[ breiten wuchses |   hellen Färbung   | (Härte) ]] für beanspruchte Arbeitsflächen nutzbar.

Die Buche  wird sehr gerne aufgrund ihrer [[ wilden Wuchsform |   (gleichmäßigen Färbung)  | Langlebigkeit ]] für Furniere verwendet.

## Und weiter gehts mit dem Quiz

Schaue dir dazu den nächsten Film an<F6>
====

!?[](https://youtu.be/QP7nOjA9si8?si=LXjAJXKKXkOx9Sim)


-   [[![Ahorn](https://)![](img/78c4079dabd58afc91d0be6ebd3e3f389c8af08a.jpeg) <!-- style="width: 100px" -->]        (![Balsa](https://)![](img/1c4945f4d6de59e7f52b79bdece3db8579d5bf11.jpeg) <!-- style="width: 100px" -->)                 [![Fichte](https://)![](img/b9fb21a6efb67e30927e96685605779ed132bd86.jpeg) <!-- style="width: 100px" -->]               [![Pockholz](https://)![](img/751501db64601f0f609856c7df3aa7f2ce1388c9.jpeg) <!-- style="width: 100px" -->]]
- [    ( )              ( )                      (x)     ]  sehr hart
- [    ( )              (X)                      ( )     ]  Sehr weich
- [    ( )              ( )                      (x)     ]  hart
- [    ( )              ( )                      ( )     ]  weich


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

@selectimages(@uid, 10, img/78c4079dabd58afc91d0be6ebd3e3f389c8af08a.jpeg, img/1c4945f4d6de59e7f52b79bdece3db8579d5bf11.jpeg|img/b9fb21a6efb67e30927e96685605779ed132bd86.jpeg)

Drag and Drop Quiz
=======

> Hier das Drag and Drop Quiz von Niklas
> `@dragdropmultipleimages(@uid, richtig, falsch)`
> Beachtet dazu den import im Kopf `LiaScript_DragAndDrop_Template`

- **@uid**: ist wichtig damit das Quiz funktioniert
- **richtig**: sind die Bilder, die richtig sind
- **falsch**: sind die Bilder, die falsch sind

Alle Bilder sind die Pfadangaben zu Bildern, die aktuell im Ordner `img/` liegen. Bilder können mit `|` getrennt werden, um mehrere Bilder anzugeben.

Ziehe alle Hardhölzer in die Box
===

> weiss nicht was hier die richtigen sind :) Hab jetzt Ahorn und Fichte genommen aus dem matrix quiz

@dragdropmultipleimages(@uid, img/78c4079dabd58afc91d0be6ebd3e3f389c8af08a.jpeg|img/b9fb21a6efb67e30927e96685605779ed132bd86.jpeg, img/1c4945f4d6de59e7f52b79bdece3db8579d5bf11.jpeg|img/751501db64601f0f609856c7df3aa7f2ce1388c9.jpeg)


