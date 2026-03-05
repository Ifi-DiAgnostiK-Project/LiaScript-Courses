<!--

author:   Hilke Domsch
email:    hilke.domsch@gkz-ev.de
version:  0.0.7
language: de
narrator: Deutsch Female

edit: true
date: 2025-09-08

icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/Textilpflegesymbole.png
comment:  Kurs mit den Piktogrammen zur Textilpflege für Raumausstatter.

title: Raumausstatter - Textilpflegesymbole

link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Textilpflegesymbole/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md


tags: [ Textilpflege, Bügeln, Waschen, Bleichen, Trocknen, Raumausstatter]

-->

# Textilpflege - Symbole 

![Waschschüssel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/wash.png)<!-- style="max-width: 100px; width: 100%;" -->

Jede Textilfaser und Stoffart benötigt eine besondere Behandlung. Pflegeetiketten sind die "Geheimschrift" der Textilien-Hersteller. Sie enthalten wichtige Hinweise für die Reinigung und Bearbeitung. Die Textilpflegesymbole sind international standardisiert. Sie geben nicht nur Empfehlungen, sondern auch Einschränkungen wie "nicht bleichen" an. 

Im Alltag eines Raumausstatters ist es unerlässlich, die kleinen Symbole zu entschlüsseln bzw. richtig an gefertigte Arbeiten anzubringen.

Testen Sie, ob Sie sich bereits gut in den Textilpflegesymbolen auskennen!

<!--class="highlight"-->
Viel Erfolg!
------------

<center>
![Pflegesymbole](https://upload.wikimedia.org/wikipedia/commons/3/33/Textilpflegesymbole.svg "Quelle: https://commons.wikimedia.org/wiki/File:Textilpflegesymbole.svg")<!-- style="max-width: 500px; width: 100%" -->
</center>


## 1. Textilpflegesymbole verstehen 🏷

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was versteht man unter textilen Artikeln?\
Setzen Sie den jeweils richtigen Begriff an die passende Stelle.

[->[ (Garn) ]], Stückware und konfektionierte Produkte mit einem Gewichtsanteil an [->[ (Textilfasern) ]] von mindestens [->[  55% | (80%)  ]], einschließlich nichttextiler Bestandteile.  

</div>
</section>


<!-- class="highlight" -->
Welche ~~fünf~~ Kategorien bilden die grundlegenden Pflegesymbole auf Textilien?\
Ziehen Sie die richtigen Begriffe ins Antwortfeld.

<!-- data-randomize -->
@dragdropmultiple(@uid,Waschen|Bleichen|Trocknen|Bügeln|Professionelle Textilpflege,Nähen|Färben|Schleudern|Verpacken)



## 2. Bügeln und Pressen 🔳 

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Hier geht es um eine Definition.\
Setzen Sie den jeweils richtigen Begriff an die passende Stelle.

Bügeln und [->[  (Pressen) | Bleichen ]] ist ein Vorgang, der am textilen Artikel mit einem geeigneten Gerät unter Einsatz von [->[  chemischen Substanzen | (Wärme)  ]], Druck und ggf.  [->[ (Dampf) | Aktivsauerstoff ]] zur Wiederherstellung seiner Form und seines Erscheinungsbildes durchgeführt wird.

</div>
</section>


<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 160 Grad
- [(X)] Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 210 Grad
- [( )] Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 210 Grad - ohne Dampf
- [( )] Bügeln mit Pressstärke 3

</div>
<div class="flex-child-2 center">
@Buegelsymbole.Buegeln_hohe_temperatur(15)
</div>
</section>

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Bügeln nicht erlaubt
- [(X)] Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 120 Grad - Dampf kann irreparable Schäden verursachen
- [( )] Bügeln mit einer Presstärke 1 - ohne Dampf
- [( )] Bügeln mit Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 180 Grad - ohne Dampf

</div>
<div class="flex-child-2 center">
@Buegelsymbole.Buegeln_geringe_Temperatur_ohne_Dampf(15)
</div>
</section>

## 3. Waschen 🥼

<!-- class="highlight" -->
Welches Symbol steht für Waschen?\
Ziehen Sie das richtige Piktrogramm ins Antwortfeld.

<!-- data-randomize -->
@dragdropmultiple(@uid,@Waschsymbole.Waschen_Grundsymbol.src, @Reinigungssymbole.Professionelle_Reinigung_Grundsymbol.src|@Bleichsymbole.Chlor_oder_Sauerstoffbleichen.src|@Reinigungssymbole.Professionelle_Nassreinigung_schonend.src|@Trocknersymbole.Trocknen_Grundsymbol.src)

<section class="flex-container border">
<div class="flex-child">


<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Handwäsche - Umgebungstemperatur
- [(X)] Handwäsche - max. 40 Grad
- [( )] Handwäsche - max. 30 Grad
- [( )] Maschinenwäsche - Schonprogramm

</div>
<div class="flex-child-2 center">
@Waschsymbole.Handwaesche_max_40_grad(15)
</div>
</section>


<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Waschtemperatur mindestens 60 Grad
- [(X)] max. Waschtemperatur 60 Grad - schonender Prozess
- [( )] max. Waschtemperatur 60 Grad - nur 1x Schleudern
- [( )] 2x Waschen bei 60 Grad

</div>
<div class="flex-child-2 center">
@Waschsymbole.waschen_bei_max_60_grad_schonend(15)
</div>
</section>

## 4. Bleichen ☀

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Welche Aussagen zum Bleichen sind richtig?

<!-- data-randomize -->
- [[X]] Bleichen kann vor, während oder nach dem Waschen durchgeführt werden.
- [[ ]] Die Bleichsymbole sind entweder dreieckig oder viereckig.
- [[ ]] Wenn Bleichen erlaubt ist, ist es immer durchzuführen, damit der Stoff weiß bleibt.
- [[X]] Ein Bleichaktivator ist ein Mittel, das Bleichen bei niedrigen Temperaturen ermöglicht.
- [[X]] Bleichen wird eingesetzt, um Schmutz und Flecken besser zu entfernen.


</div>
</section>

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Es ist nur Chlorbleiche zulässig.
- [(X)] Es ist nur Sauerstoffbleiche zulässig.
- [( )] Bleichen ist max. aller 3 Monate zulässig.
- [( )] Bleichen ist vorab an einer unauffälligen Stelle zu probieren.

</div>
<div class="flex-child-2 center">
@Bleichsymbole.Nur_Sauerstoffbleichen(15)
</div>
</section>

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Bleichen ist nur in der Waschmaschine möglich.
- [(X)] Symbol für "haushaltsüblicher Wäschetrockner".
- [( )] Chlor- oder Sauerstoffbleiche ist zulässig.
- [( )] Bleichen ist im Wäschetrockner möglich.

</div>
<div class="flex-child-2 center">
@Trocknersymbole.Trommeltrocknen_Grundsymbol(15)
</div>
</section>

## 5. Trocknen 👗

<!-- class="highlight" -->
Welche Symbole stehen für das Trocknen im Wäschetrockner?\
Ziehen Sie die richtigen Piktrogramme ins Antwortfeld.

<!-- data-randomize -->
@dragdropmultiple(@uid,@Trocknersymbole.Trommeltrocknen_normale_Temperatur.src|@Trocknersymbole.Trommeltrocknen_niedrige_Temperatur.src, @Trocknersymbole.Trocknen_Waescheleine_im_Schatten.src|@Trocknersymbole.Trocknen_Liegend_Tropfnass.src|@Reinigungssymbole.Professionelle_Nassreinigung.src)


<section class="flex-container border">
<div class="flex-child">


<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Die Wäsche darf nur bei niedrigen Temperaturen getrocknet werden.
- [(X)] Die Wäsche ist auf der Leine zu trocknen.
- [( )] Es darf nur Wäsche einer Stoffart zusammen im Trockner getrocknet werden. 
- [( )] Die Wäsche ist im tropfnassen Zustand zu trocknen.

</div>
<div class="flex-child-2 center">
@Trocknersymbole.Trocknen_Waescheleine(15)
</div>
</section>

## 6. Professionelle Textilpflege 🩳

<!-- class="highlight" -->
Welches Symbol steht für die Professionelle Nassreinigung?\
Ziehen Sie das richtige Piktrogramm ins Antwortfeld.

<!-- data-randomize -->
@dragdropmultiple(@uid,@Reinigungssymbole.Professionelle_Nassreinigung_schonend.src, @Reinigungssymbole.Nicht_Trockenreinigen.src|@Reinigungssymbole.Trockenreinigung_mit_Kohlenwasserstoffloesungsmittel_schonend.src|@Reinigungssymbole.Trockenreinigung_mit_Perchlorethylen.src)


<section class="flex-container border">
<div class="flex-child">


<!-- class="highlight" -->
Was bedeutet dieses Symbol?

<!-- data-randomize -->
- [( )] Professionelle Nassreinigung 
- [(X)] Professionelle Trockenreinigung mit Perchlorethylen, Dibutoxymethan und Kohlenwasserstoffen - schonend
- [( )] Professionelle Trockenreinigung nur mit Kohlenwasserstoffen
- [( )] Trocknen im Wäschetrockner

</div>
<div class="flex-child-2 center">
@Reinigungssymbole.Trockenreinigung_mit_Perchlorethylen_schonend(15)
</div>
</section>



## Zusatz

<section class="flex-container border">
<div class="flex-child">

<!-- class="highlight" -->
In welcher standardisierten Reihenfolge sind die Pflegesymbole auf einem Etikett anzubringen?\
Ziehen Sie die Wörter in die richtige Reihenfolge.

@dragdroporder(@uid,Waschen|Bleichen|Trocknen|Bügeln|Professionelle Textilpflege,3)

Ziehen Sie die Zeichen in die richtige Reihenfolge.

@dragdroporder(@uid, @Waschsymbole.Waschen_Grundsymbol(10).src | @Bleichsymbole.Chlor_oder_Sauerstoffbleichen(10).src | @Trocknersymbole.Trocknen_Grundsymbol(10).src | @Buegelsymbole.Buegeln_Grundsymbol(10).src | @Reinigungssymbole.Professionelle_Reinigung_Grundsymbol(10), 3)

</div>
</section>

## Geschafft! 🙌


<center>
![Jubel](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/colorfull_jumping.jpg "_Quelle: Pixabay, geralt_")
</center>













