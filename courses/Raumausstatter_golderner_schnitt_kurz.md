<!--

author:   Hilke Domsch, Volker Göhler

email:    hilke.domsch@gkz-ev.de

version:  0.0.1

language: de

narrator: Deutsch Male

comment:  Goldener Schnitt -- Kurzversion

edit: true
date: 2025-07-08
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/da_vinci.png
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

import: https://raw.githubusercontent.com/liaTemplates/algebrite/master/README.md

tags:
    - Raumausstatter

title: Goldener Schnitt -- Kurzversion

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

# Der Goldene Schnitt 

![Da Vinci](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/da_vinci.png)

_Quelle:_ Da Vinci Vitruve Luc Viatour 2.svg; Wikipedia; 


![Illustration Goldener Schnitt](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/goldener_schnitt_illustration.png)<!-- style="width: 400px;" -->

_Quelle:_ Generiert von Dall-E 3, An OpenAI Model, 2025


## Einführung

<!--style="font-size: large;"-->Der __Goldene Schnitt__ ist ein besonderes Verhältnis, das häufig in der Kunst, Architektur und Natur vorkommt. 

<!--style="font-size: large;"-->Es beträgt   1 <!--style="color:green;"-->  :   1,618 <!--style="color:green;"--> zwischen zwei verschiedenen Größen bzw. 38,2% <!--style="color:green;"--> zu 61,8% <!--style="color:green;"-->. 

<!--style="font-size: large;"-->In der Praxis wird oft das angenäherte Verhältnis **3:5** <!--style="color:red;"--> bzw. **5:8** <!--style="color:red;"--> verwendet. 

<!--style="font-size: large;"-->Dieses ungleiche Verhältnis zwischen zwei Größen wird als besonders schön und harmonisch empfunden. 



<!-- style="width: 800px" -->


![golden ratio examples](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/golden_ratio_collage.png)

_Quelle:_ Generiert von Dall-E 3, An OpenAI Model, 2025

## 🧠 Quiz: Verstehst du den Goldenen Schnitt?


Welche der folgenden Zahlenpaare stehen im ungefähren Verhältnis des Goldenen Schnitts?
===

- [[ ]] 2 : 3
- [[x]] 3 : 5
- [[x]] 5 : 8
- [[ ]] 4 : 6


### Was beschreibt der Goldene Schnitt?


- [( )] Eine Methode zur Berechnung von Kreisflächen
- [(x)] Ein Verhältnis, bei dem sich der kleinere Teil zum größeren Teil so verhält wie der größere zum Ganzen
- [( )] Eine Technik zum Messen von Winkeln
- [( )] Eine Methode zur Berechnung von Volumen


### Welche Aussagen über den Goldenen Schnitt sind richtig?

- [[x]] Der Wert des Goldenen Schnittes beträgt ungefähr 1,618.
- [[x]] Er kommt in der Natur vor.
- [[ ]] Er ist immer größer als 3.
- [[x]] Er wird oft in der Kunst verwendet.


### Wo kommt der Goldene Schnitt vor?  


- [[x]] In Blumen und Pflanzen
- [[x]] In Kunst und Architektur
- [[ ]] In der Zahl Pi
- [[x]] In Schneckenhäusern


## ✏️ Praxisaufgabe: Dekorationsschleife

Sie haben während Ihrer überbetrieblichen Ausbildung eine Dekorationsschleife gefertigt. 



Diese besteht aus zwei Teilen, dem oberen  Schleifen- [[  (körper)|band | stoff]]   und dem unteren Schleifen- [[  körper|(band)|stoff  ]].

Diese beiden Teile stehen im Verhältnis   __3:5__   zueinander. 

---

Schauen Sie sich die folgende Skizze an.
------------------

![Deko-Schleife](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/deko_schleife.jpg)

_Quelle: HWK Dresden, Frau Schmidt_

---


Lesen Sie die Breite der Gesamtschleife (Minor) ab:
---------------------

 [[  30  ]] cm


### Berechnen Sie die Gesamtlänge der Schleife unter Beachtung des Verhältnisses 3 : 5.

![Deko-Schleife_Major](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/schleife_major_laenge.jpg)

<!--style="font-size: medium;"-->__Berechnung:__

$3$ Teile (**Minor**) = [[ 30 ]] $\text{cm}$ = Schleifenbreite

$1$ Teil = [[ 10 ]] $\text{cm}$

$5$ Teile (**Major**) = [[ 50 ]] $\text{cm}$ = Gesamtlänge der Schleife
*****
Rechenweg
=========

- **Minor-Strecke** (3 Teile): $30\,\text{cm}$
- Verhältnis: $3 : 5$
- Gesucht: **Major-Strecke** (5 Teile)

---

Berechnung:  
===========

Ein Teil entspricht:  
$$
\frac{30\,\text{cm}}{3} = 10\,\text{cm}
$$

Major-Strecke (5 Teile):  
$$
5 \cdot 10\,\text{cm} = 50\,\text{cm}
$$

---

Ergebnis:  
=========

- **Minor-Strecke:** $30\,\text{cm}$  
- **Major-Strecke:** $50\,\text{cm}$  

*****


### Berechnen Sie die Höhe des Schleifenkörpers unter Beachtung des Verhältnisses 3 : 5.


_Tipp: In der vorherigen Aufgabe entsprach die Breite des Schleifenkörpers der Minor-Strecke, um daraus die Gesamtlänge des Schleifenbands (Major) zu berechnen. Jetzt ist die Höhe des Schleifenkörpers gesucht und die Breite des Schleifenkörpers stellt die Major-Strecke dar._

---

![Deko-Schleife_Höhe_Schleifenkörper](https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/schleife_minor_breite.jpg)


<!--style="font-size: medium;"-->__Berechnung:__

$5$ Teile (**Major**) = [[ 30 ]] $\text{cm}$ = Schleifenbreite

$1$ Teil = [[ 6 ]] $\text{cm}$

$3$ Teile (**Minor**) = [[ 18 ]] $\text{cm}$ = Höhe des Schleifenkörpers
*****
Rechenweg 
--------

- **Major-Strecke** (5 Teile): $30\,\text{cm}$
- Verhältnis: $3 : 5$
- Gesucht: **Minor-Strecke** (3 Teile)

---

Berechnung:  
===========

Ein Teil entspricht:  
$$
\frac{30\,\text{cm}}{5} = 6\,\text{cm}
$$

Minor-Strecke (3 Teile):  
$$
3 \cdot 6\,\text{cm} = 18\,\text{cm}
$$

---

Ergebnis:  
=========

- **Major-Strecke:** $30\,\text{cm}$  
- **Minor-Strecke:** $18\,\text{cm}$  

*****
