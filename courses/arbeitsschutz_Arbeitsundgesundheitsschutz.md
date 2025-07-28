<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.3

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
    - Arbeits-_und_Gesundheitsschutz

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


## Aussagen rund um den Arbeits- und Gesundheitsschutz

__Die nächsten Aussagen drehen sich rund um den Arbeits- und Gesundheitsschutz. Entscheiden Sie, ob die folgenden Aussagen wahr oder falsch sind! Es können mehrere Antworten richtig sein.__

--- 

1. Das Bild mit einer Person auf der Leiter und einer Zahl zeigt an, dass die Leiter von insgesamt drei Personen zu nutzen ist: Eine Person, die hinaufsteigt, und zwei Personen, welche die Leiter sichern.
===
<!-- --{{1}}--
Erstens. Das Bild mit einer Person auf der Leiter und einer Zahl zeigt an, dass die Leiter von insgesamt drei Personen zu nutzen ist: Eine Person, die hinaufsteigt, und zwei Personen, welche die Leiter sichern. Wahr oder falsch? 
-->
<section class="flex-container" >
<div class="flex-child">
@Leitern.Die_obersten_3_Sprossen_nicht_besteigen(10)
</div>
<div class="flex-child">
[[ wahr | (falsch) ]]
</div>
</section>


---


2. Brandschutzzeichen sind immer orange-schwarz.
===
<!-- --{{2}}--
Zweitens. Brandschutzzeichen sind immer orange-schwarz. Wahr oder falsch?
-->

[[ wahr | (falsch) ]]

---

3. Das Bild bedeutet, dass Leitern nur bei entsprechenden Witterungsbedingungen genutzt werden dürfen.
===
<!-- --{{3}}--
Drittens. Das Bild bedeutet, dass Leitern nur bei entsprechenden Witterungsbedingungen genutzt werden dürfen. Wahr oder falsch?
-->

<section class="flex-container" >
<div class="flex-child">
@Leitern.Witterungsbedingungen(10)

</div>
<div class="flex-child">
[[ (wahr) | falsch ]]
</div>
</section>

---



4. Diese Abbildung zeigt, dass kein Wasser versprüht werden darf.
===
<!-- --{{4}}--
Viertens. Diese Abbildung zeigt, dass bei der Arbeit kein Wasser aus dem Gartenschlauch entnommen werden darf. Wahr oder falsch?
-->

<section class="flex-container" >
<div class="flex-child">
@Verbotszeichen.Mit_Wasser_spritzen_verboten(10)

</div>
<div class="flex-child">
[[ wahr | (falsch) ]]
</div>
</section>

---


5. Dieses Symbol meint: Achtung: Diebstahlgefahr!
===
<!-- --{{5}}--
Fünftens. Dieses Symbol meint: Achtung: Diebstahlgefahr! Wahr oder falsch?
-->

<section class="flex-container" >
<div class="flex-child">
@Verbotszeichen.Beruehren_verboten(10)

</div>
<div class="flex-child">
[[ wahr | (falsch) ]]
</div>
</section>

---


6. Warum sind Brandschutzzeichen wichtig?
====
<!-- --{{6}}--
Sechstens. Warum sind Brandschutzzeichen wichtig? Wahr oder falsch?
-->

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

7. Was bedeutet dieses Schild?
===
<!-- --{{7}}--
Siebentens. Was bedeutet dieses Schild? Entweder: Klappbügel befindet sich hier. Oder: Fluchttür befindet sich hier. Oder: Wartung beziehungsweise Reparatur freischalten.
-->
<section class="flex-container">

<div class="flex-child" style="min-width: 250px">
@Gebotszeichen.Wartung_oder_Reparatur_freischalten(10)
</div>

<div class="flex-child" style="min-width: 500px">
<!-- data-randomize -->
[[ Klappbügel befindet sich hier. | __Fluchttür befindet sich hier.__ | (Wartung oder Reparatur freischalten.) ]]
</div>
</section>

---

8. Ordnen Sie die Schilder den richtigen Begriffen zu!
===
<!-- --{{8}}--
Achtens. Ordnen Sie die Schilder den richtigen Begriffen zu!
-->

<!-- data-randomize -->
-   [[ @Warnzeichen.Heisse_Oberflaeche(10)]        [ @Gebotszeichen.Warnweste(10) ]                 [ @Verbotszeichen.Rauchen_verboten(10) ]       [ @Brandschutzzeichen.Brandbekaempfung(10) ]                 [ 	@Rettungszeichen.Rettungsweg_Notausgang_rechts(10) ]       [ @Gefahrstoffe.Entzuendlich(10) ]]
- [    ( )              ( )                      ( )      (X)              ( )                      ( )     ]  Brandschutzzeichen
- [    ( )              (X)                      ( )      ( )              ( )                      ( )     ]  Gebotszeichen
- [    ( )              ( )                      ( )      ( )              ( )                      (X)     ]  Gefahrstoffe
- [    ( )              ( )                      (X)      ( )              ( )                      ( )     ]  Verbotszeichen
- [    (X)              ( )                      ( )      ( )              ( )                      ( )     ]  Warnzeichen
- [    ( )              ( )                      ( )      ( )              (X)                      ( )     ]  Rettungszeichen

---




9. Wo müssen Brandschutzzeichen angebracht werden?
===
<!-- --{{9}}--
Neuntens. Wo müssen Brandschutzzeichen angebracht werden? Entweder: Nur im Büro. Oder: Überall, wo sich Brandschutzeinrichtungen befinden. Oder: Nur in der Werkstatt. Oder: Nur im Lager.
-->

- [( )] Nur im Büro.
- [(X)] Überall, wo sich Brandschutzeinrichtungen befinden.
- [( )] Nur in der Werkstatt.
- [( )] Nur im Lager.

---

10. Füllen Sie den Lückentext richtig aus:
===
<!-- --{{10}}--
Zehntens. Füllen Sie den Lückentext richtig aus. 
-->

<!-- data-randomize -->
Arbeits- und Gesundheitsschutz ist ein wichtiger Bestandteil im Berufsleben. Ziel ist es, die [[ (Sicherheit) | __Gefährdung__ | Unfall | __Krankheit__  ]] und Gesundheit aller Beschäftigten am Arbeitsplatz zu gewährleisten. Zu den wichtigsten Maßnahmen gehören die [[ __Pausenregelung__ |  (Gefährdungsbeurteilung) | __Urlaubsplanung__ | Gehaltsabrechnung  ]] und das Ergreifen geeigneter Schutzmaßnahmen.

Eine wichtige Rolle spielt auch die [[ (__Unterweisung__) |  Entlassung | __Versetzung__ | Beförderung  ]] der Mitarbeiter und Mitarbeiterinnen. Sie müssen regelmäßig über Gefahren und Schutzmaßnahmen informiert werden. Das Tragen von persönlicher [[ __Freizeitkleidung__ |  Bürobedarf | __Werkzeug__ | (Schutzausrüstung)  ]] kann in bestimmten Bereichen vorgeschrieben sein.

Arbeitgeber sind verpflichtet, Arbeitsunfälle und [[ Feiertage |  __Überstunden__ | Fehlzeiten | (__Berufskrankheiten__)  ]] zu melden. Beschäftigte sollten bei Gefahr sofort ihren [[ Kollegen |  __Hausmeister__ | (Vorgesetzten) | __Kunden__  ]] informieren.

---

11. Ziehen Sie alle Gebotszeichen in das Antwortfeld! 🤔
===
<!-- --{{11}}--
Können Sie  diese Zuordnungsaufgabe lösen? - Ziehen Sie alle Gebotszeichen in das Antwortfeld.
-->

<!-- data-randomize -->
@dragdropmultipleimages(@uid,@Gebotszeichen.Uebergang.src,@Rettungszeichen.Arzt.src|@Leitern.Maximale_Belastung.src|@Warnzeichen.Absturzgefahr.src|@Brandschutzzeichen.Richtungspfeil_Rechts_unten.src|) 

----

<!-- --{{12}}--
Wenn Sie noch mehr wissen wollen, finden Sie mehr Informationen und alle Sicherheitszeichen auf der BGHM-Website - siehe Link.
-->

__Tipp:__ 
Weitere Informationen und alle Sicherheitszeichen finden Sie auf der BGHM-Webseite: https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen 

---

Geschafft! 🙌
===
