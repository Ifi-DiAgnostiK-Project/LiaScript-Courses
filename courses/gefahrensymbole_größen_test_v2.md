<!--
author: Volker Göhler
email:    volker.goehler@informatik.tu-freiberg.de
language: de
narrator: German Female
version: 0.0.1
comment: this is only a test for image sizes in conjunction with quizes

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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/master/gefahrensymbole_größen_test_v2.md)

# Quiztest

> Wenn ich nur ein Bild setze dann nimmt das den gesamten Space ein. Ich würde nun das Ding als html einbinden und die größe Händisch festlegen, aber das kann ich den User nicht erklären. Im Pandoc gibt es die möglichkeit die Größe als Option in `{height=5cm}` z.B. mitzugeben, aber der rendered dann auch (bei mir ) latex.

![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandmelder.jpg?raw=true)<!-- style="width: 50%" -->

Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

---------------------

<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandmelder.jpg?raw=true)

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>




---

> Wenn 2 nebeneinander liegen ist die individuelle Größe gut, aber hab dann eben 2 Bilder. ;)

![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)

- [( )] nicht hier klickern
- [( )] falsch
- [(X)] Sicherheitszeichen Brandschutz Brandbekämpfung

----

<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)

<div class="flex-child" style="min-width: 250px">
Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

</div>
</section>

-----------


<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)

<!-- class="flex-child" style="min-width: 250px;" -->
![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Brandbek%C3%A4mpfung.jpg?raw=true)

</section>

Um was für ein Zeichen handelt es sich:

- [(X)] Sicherheitszeichen Brandmelder
- [( )] falsche Antwort
- [( )] auch falsch ;)

---

> Hier ist mein Hack dafür. ;) not ideal.

![Brandschutzzeichen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/Brandschutzzeichen/Sicherheitszeichen_Brandschutz_Feuerl%C3%B6scher.jpg?raw=true)
![weißes Bild](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/blank.jpg?raw=true)


- [( )] falsch
- [(X)] Feuerlöscher
- [( )] ganz falsch


## 1. __Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?__

<!-- --{{0}}--
Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?
a. Mutterschutz b. Schutz vor Gefahren am Arbeitsplatz c. Sportunfälle
--> 

- [( )] Mutterschutz
- [(X)] Schutz vor Gefahren am Arbeitsplatz
- [( )] Sportunfälle


## 1. __Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?__

So tut es ...

- [( )] Mutterschutz
- [(X)] Schutz vor Gefahren am Arbeitsplatz
- [( )] Sportunfälle

<!-- --{{0}}--
Für welches Aufgabengebiet ist die Berufsgenossenschaft zuständig?
a. Mutterschutz b. Schutz vor Gefahren am Arbeitsplatz c. Sportunfälle
--> 

--{{1}}--
more talkingpoints
