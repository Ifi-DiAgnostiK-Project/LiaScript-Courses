<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.1

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/c/cc/Bundesarchiv_Bild_183-41030-0002%2C_Sichtwerbung_f%C3%BCr_Arbeits-_und_Gesundheitsschutzes.jpg

attribute: title image Von Bundesarchiv, Bild 183-41030-0002 / Draum / CC-BY-SA 3.0, CC BY-SA 3.0 de, https://commons.wikimedia.org/w/index.php?curid=5428443

comment:  Arbeitssicherheit & Gesundheitsschutz

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

title: Arbeitssicherheit und Gesundheitsschutz -- Allgemeine Fragen

tags:
    - Arbeitssicherheit
    - Gesundheitsschutz

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

.image_matrix img {
    padding: 3px;
    margin: 5px;
    width: 100px;
    border: 1px black solid;
    display:inline-block;
}

@end

-->

# Arbeitssicherheit und Gesundheitsschutz

Arbeitsbedingte Gesundheitsgefahren, Unfälle und Erkrankungen sollen gar nicht erst entstehen. Dazu ist es wichtig, Gefahrenhinweise und Symbole richtig zu verstehen.
Vor allem junge Menschen sind am Arbeitsplatz besonders gefährdet, weil sie (noch) nicht über alle nötigen Kenntnisse verfügen.
Dieses Quiz zeigt Ihnen, wie gut Sie sich bereits auskennen!
Wir sind gespannt, wie Sie die Challenge meistern!

__Viel Erfolg!__

__In welcher Zeile befinden sich Warnschilder?__
===

<!-- --{{1}}--
In welcher Zeile befinden sich Warnschilder? Zeile 1, 2 oder 3?
-->

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 1:__
</div>
<div class="flex-child">
@Brandschutzzeichen.Feuerloescher(10)
</div>
<div class="flex-child">
@Brandschutzzeichen.Loeschschlauch(10)
</div>
<div class="flex-child">
@Brandschutzzeichen.Feuerleiter(10)
</div>
</section>

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 2:__
</div>
<div class="flex-child">
@Warnzeichen.Elektrische_Spannung(10)
</div>
<div class="flex-child">
@Warnzeichen.Flurfoerderzeugen(10)
</div>
<div class="flex-child">
@Warnzeichen.Schwebende_Last(10)
</div>
</section>

<section class="flex-container" style="padding: 1rem;">
<div style="padding-top:3rem;">
__Zeile 3:__
</div>
<div class="flex-child">
@Verbotszeichen.Zutritt_fuer_Unbefugte_verboten(10)
</div>
<div class="flex-child">
@Verbotszeichen.Besteigen_fuer_Unbefugte_verboten(10)
</div>
<div class="flex-child">
@Verbotszeichen.Allgemeines_Verbotszeichen(10)
</div>
</section>

[[ __Zeile 1__ | (__Zeile 2__) | __Zeile 3__]]


## 4. Aussagen rund um den Arbeits- und Gesundheitsschutz

<!-- --{{0}}--
Die nächsten Aussagen drehen sich rund um den Arbeits- und Gesundheitsschutz. 
Entscheiden Sie, ob die folgenden Aussagen wahr oder falsch sind. Es können mehrere Antworten richtig sein.
--> 

__Die nächsten Aussagen drehen sich rund um den Arbeits- und Gesundheitsschutz. Entscheiden Sie, ob die folgenden Aussagen wahr oder falsch sind! Es können mehrere Antworten richtig sein.__
===

>_Ich habe in der Vertonung die Fragennummern mit eingesprochen, möchte aber gern, dass zukünftig das Quiz in beliebiger Reihenfolge abgespielt wird. Bitte angeben, wie ich das ändern/verbessern kann._

>_Die Aussage "Es können mehrere Antworten richtig sein." hätte ich gern wieder auf einer neuen Zeile = Zeilenumbruch. Wie geht das?_

--- 

<!-- --{{0}}--
Erstens. Das Bild mit einer Person auf der Leiter und einer Zahl zeigt an, dass die Leiter von insgesamt drei Personen zu nutzen ist: Eine Person, die hinaufsteigt, und zwei Personen, welche die Leiter sichern. Wahr oder falsch? 
-->

![Die oberen 3 Sprossen nicht nutzen](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Leitern/Die_obersten_3_Sprossen_nicht_besteigen.jpg?raw=true) <!-- style="width: 130px" -->

__1. Das Bild mit einer Person auf der Leiter und einer Zahl zeigt an, dass die Leiter von insgesamt drei Personen zu nutzen ist: Eine Person, die hinaufsteigt, und zwei Personen, welche die Leiter sichern. __ 
===

[[ wahr | (falsch) ]]


>_Wie kann ich einen Absatz in der Textanleitung generieren?_

---

<!-- --{{}}--
Zweitens. Brandschutzzeichen sind immer orange-schwarz. Wahr oder falsch?
-->

__2. Brandschutzzeichen sind immer orange-schwarz. __
===

[[ wahr | (falsch) ]]

---

<!-- --{{}}--
Drittens. Das Bild bedeutet, dass Leitern nur bei entsprechenden Witterungsbedingungen genutzt werden dürfen. Wahr oder falsch?
-->

![Leitereinsatz](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Leitern/Witterungsbedingungen.jpg?raw=true) <!-- style="width: 130px" -->

__3. Das Bild bedeutet, dass Leitern nur bei entsprechenden Witterungsbedingungen genutzt werden dürfen. __
===

[[ (wahr) | falsch ]]

---


<!-- --{{}}--
Viertens. Diese Abbildung zeigt, dass bei der Arbeit kein Wasser aus dem Gartenschlauch entnommen werden darf. Wahr oder falsch?
-->

![Wasser spritzen verboben](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Verbotszeichen/Mit_Wasser_spritzen_verboten.jpg?raw=true) <!-- style="width: 130px" -->


__4. Diese Abbildung zeigt, dass kein Wasser versprüht werden darf.__
===

[[ wahr | (falsch) ]]

---

<!-- --{{}}--
Fünftens. Dieses Symbol meint: Achtung: Diebstahlgefahr! Wahr oder falsch?
-->

![Berühren verboten!](https://github.com/vgoehler/DiAgnostiK_Bilder_Test/blob/main/img/Verbotszeichen/Ber%C3%BChren_verboten.jpg?raw=true) <!-- style="width: 130px" -->

__5. Dieses Symbol meint: Achtung: Diebstahlgefahr!__
===

[[ wahr | (falsch) ]]

---


<!-- --{{}}--
Sechstens. Warum sind Brandschutzzeichen wichtig? Wahr oder falsch?
-->


__6. Warum sind Brandschutzzeichen wichtig?__
====

<section class="flex-container">

<div class="flex-child" style="min-width: 250px">

- [[ ]]  Sie dienen der Dekoration.
- [[X]]  Sie helfen, im Brandfall schnell die richtigen Hilfsmittel zu finden.
- [[ ]]  Sie zeigen Fluchtwege an.
- [[X]]  Sie sind gesetzlich vorgeschrieben.

</div>

<div class="flex-child" style="min-width: 500px">

<div class="image_matrix">
@Brandschutzzeichen.Feuerloescher(10)
@Brandschutzzeichen.Loeschschlauch(10)
@Brandschutzzeichen.Brandmeldetelefon(10)
@Brandschutzzeichen.Richtungspfeil_Rechts(10)
</div>
<div class="image_matrix">
@Brandschutzzeichen.Brandbekaempfung(10)
@Brandschutzzeichen.Brandmelder(10)
@Brandschutzzeichen.Feuerleiter(10)
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)
</div>

</div>

</section>

---


<!-- --{{}}--
Siebentens. Was bedeutet dieses Schild? Entweder: Klappbügel befindet sich hier. Oder: Fluchttür befindet sich hier. Oder: Wartung beziehungsweise Reparatur freischalten.
-->

__7. Was bedeutet dieses Schild?__
===

![Gebotszeichen. Wartung oder Reparatur](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Gebotszeichen/Wartung_oder_Reparatur_freischalten.jpg?raw=true) <!-- style="width: 130px" -->


<!-- data-randomize -->
[[ Klappbügel befindet sich hier. | __Fluchttür befindet sich hier.__ | (Wartung oder Reparatur freischalten.) ]]

---

<!-- --{{}}--
Achtens. Ordnen Sie die Schilder den richtigen Begriffen zu!
-->

__8. Ordnen Sie die Schilder den richtigen Begriffen zu!__
===

<!-- data-randomize -->
-   [[![Warnzeichen](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Warnzeichen/Hei%C3%9Fe_Oberfl%C3%A4che.jpg?raw=true) <!-- style="width: 100px" -->]        (![Warnweste](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Gebotszeichen/Warnweste.jpg?raw=true) <!-- style="width: 100px" -->)                 [![Rauchen verboten](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Verbotszeichen/Rauchen_verboten.jpg?raw=true) <!-- style="width: 100px" -->]       (![Brandbekämpfung](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Brandschutzzeichen/Brandbek%C3%A4mpfung.jpg?raw=true) <!-- style="width: 100px" -->)                 [![Notausgang](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Rettungszeichen/Notausgang_rechts.jpg?raw=true) <!-- style="width: 100px" -->]       (![Entzündlich](https://github.com/Ifi-DiAgnostiK-Project/Piktogramme/blob/main/img/Gefahrstoffe/Entz%C3%BCndlich.gif?raw=true) <!-- style="width: 100px" -->)]
- [    ( )              ( )                      ( )      (X)              ( )                      ( )     ]  Brandschutzzeichen
- [    ( )              (X)                      ( )      ( )              ( )                      ( )     ]  Gebotszeichen
- [    ( )              ( )                      ( )      ( )              ( )                      (X)     ]  Gefahrstoffe
- [    ( )              ( )                      (X)      ( )              ( )                      ( )     ]  Verbotszeichen
- [    (X)              ( )                      ( )      ( )              ( )                      ( )     ]  Warnzeichen
- [    ( )              ( )                      ( )      ( )              (X)                      ( )     ]  Rettungszeichen

---

<!-- --{{}}--
Neuntens. Wo müssen Brandschutzzeichen angebracht werden? Entweder: Nur im Büro. Oder: Überall, wo sich Brandschutzeinrichtungen befinden. Oder: Nur in der Werkstatt. Oder: Nur im Lager.
-->


__9. Wo müssen Brandschutzzeichen angebracht werden?__
===

- [( )] Nur im Büro.
- [(X)] Überall, wo sich Brandschutzeinrichtungen befinden.
- [( )] Nur in der Werkstatt.
- [( )] Nur im Lager.

---


<!-- --{{}}--
Zehntens. Füllen Sie den Lückentext richtig aus. 
-->


__10. Füllen Sie den Lückentext richtig aus:__
===


>_Kann der Lückentext sinnvoll vorgelesen werden, dass die Lücken offensichtlich werden?_

<!-- data-randomize -->
Arbeits- und Gesundheitsschutz ist ein wichtiger Bestandteil im Berufsleben. Ziel ist es, die [[ (Sicherheit) | __Gefährdung__ | Unfall | __Krankheit__  ]] und Gesundheit aller Beschäftigten am Arbeitsplatz zu gewährleisten. Zu den wichtigsten Maßnahmen gehören die [[ __Pausenregelung__ |  (Gefährdungsbeurteilung) | __Urlaubsplanung__ | Gehaltsabrechnung  ]] und das Ergreifen geeigneter Schutzmaßnahmen.

Eine wichtige Rolle spielt auch die [[ (__Unterweisung__) |  Entlassung | __Versetzung__ | Beförderung  ]] der Mitarbeiter und Mitarbeiterinnen. Sie müssen regelmäßig über Gefahren und Schutzmaßnahmen informiert werden. Das Tragen von persönlicher [[ __Freizeitkleidung__ |  Bürobedarf | __Werkzeug__ | (Schutzausrüstung)  ]] kann in bestimmten Bereichen vorgeschrieben sein.

Arbeitgeber sind verpflichtet, Arbeitsunfälle und [[ Feiertage |  __Überstunden__ | Fehlzeiten | (__Berufskrankheiten__)  ]] zu melden. Beschäftigte sollten bei Gefahr sofort ihren [[ Kollegen |  __Hausmeister__ | (Vorgesetzten) | __Kunden__  ]] informieren.

---


<!-- --{{}}--
Können Sie  diese Zuordnungsaufgabe lösen? - Ziehen Sie alle Gebotszeichen in das Antwortfeld.
-->

__11. Ziehen Sie alle Gebotszeichen in das Antwortfeld!__ 🤔
===


<!-- data-randomize -->
@dragdropmultipleimages(@uid,@Gebotszeichen.Uebergang.src,@Rettungszeichen.Arzt.src|@Leitern.Maximale_Belastung.src|@Warnzeichen.Absturzgefahr.src|@Brandschutzzeichen.Richtungspfeil_Rechts_unten.src|) 

----


<!-- --{{}}--
Wenn Sie noch mehr wissen wollen, finden Sie mehr Informationen und alle Sicherheitszeichen auf der BGHM-Website - siehe Link.
-->

__Tipp:__ 
Weitere Informationen und alle Sicherheitszeichen finden Sie auf der BGHM-Webseite: https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen 

---

Geschafft! 🙌
===
