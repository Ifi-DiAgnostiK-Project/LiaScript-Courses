<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.2

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/ISO_7010_W002.svg/2560px-ISO_7010_W002.svg.png

comment:  Arbeitssicherheit & Gesundheitsschutz

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

title: Sicherheitszeichen

tags:
    - Arbeitssicherheit
    - Sicherheitszeichen

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

## Kennen Sie die Sicherheitszeichen?

1. Ordnen Sie die Zeichen den passenden Beschreibungen zu.
===
<!-- --{{1}}--
Ordnen Sie die Zeichen den passenden Beschreibungen zu.
Warnung vor elektrischer Spannung
Aufforderung, Handschuhe zu tragen
Verbot von offenem Feuer
-->

<!-- data-randomize -->
-   [[ @Warnzeichen.Elektrische_Spannung(10) ]        ( @Gebotszeichen.Handschuh(10) )                 [ @Verbotszeichen.Keine_Offene_Flamme(10) ]]
- [    (X)                                     ( )                                      ( )     ]  Warnung vor elektrischer Spannung
- [    ( )                                     (X)                                      ( )     ]  Aufforderung, Handschuhe zu tragen
- [    ( )                                     ( )                                      (X)     ]  Verbot von offenem Feuer




2. Wahr oder falsch? -- Das Symbol "Schutzbrille tragen" ist ein blaues, rundes Gebotszeichen.
===
<!-- --{{2}}--
Wahr oder falsch?
Das Symbol "Schutzbrille tragen" ist ein blaues, rundes Gebotszeichen.
-->

- [(X)] wahr
- [( )] falsch



3. Was bedeutet das folgende Zeichen?
===
<!-- --{{3}}--
Was bedeutet das folgende Zeichen?
a) Brandmelder
b) Erste-Hilfe-Kasten
c) Feuerlöscher
-->

<section class="flex-container">
<div class="flex-child">
@Brandschutzzeichen.Feuerloescher(10)
</div>
<div class="flex-child">
<!-- data-randomize -->
- [( )] Brandmelder
- [( )] Erste-Hilfe-Kasten
- [(X)] Feuerlöscher

</div>
</section>

4. Lückentext:
===
<!-- --{{4}}--
Lückentext:
Das Zeichen mit einer laufenden Person und einem Pfeil auf grünem Hintergrund kennzeichnet einen Rettungsweg, Notausstieg oder Notausgang. Wählen Sie das richtige Wort aus.
-->

Das Zeichen mit einer laufenden Person und einem Pfeil auf grünem Hintergrund kennzeichnet einen [[ Sammelpunkt | (Notausgang) | Sani-Kasten]]. 

5. Ordnen Sie die abgebildeten Sicherheitszeichen dem richtigen Begriff zu:
===
<!-- --{{5}}--
Ordnen Sie die abgebildeten Sicherheitszeichen dem richtigen Begriff zu:
-->

<!-- data-randomize -->
-   [[ @Rettungszeichen.Notruftelefon(10) ]        ( @Gebotszeichen.Kopfschutz(10) )                 [ @Gefahrstoffe.Aetzend_Reizend(10) ]]
- [    ( )              ( )                      ( )     ]  Warnung vor einer Gefahr
- [    (X)              ( )                      ( )     ]  Notruftelefon
- [    ( )              ( )                      (X)     ]  Warnung vor Gefahrstoffen - ätzend
- [    ( )              ( )                      ( )     ]  Brandmelder
- [    ( )              (X)                      ( )     ]  Schutzhelm tragen




6. Wofür steht dieses Zeichen?
===
<!-- --{{6}}--
Wofür steht dieses Zeichen?
-->

<section class="flex-container">
<div class="flex-child">
@Gefahrstoffe.Explosiv(15)
</div>
<div class="flex-child">

<!-- data-randomize -->
- [( )] Achtung: Komprimierte Gase!
- [(X)] Achtung: Explosiv!
- [( )] Achtung: Entzündlich!

</div>
</section>

---

Geschafft! 🙌
===
