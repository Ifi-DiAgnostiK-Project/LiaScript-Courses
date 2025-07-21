<!--

author: Hilke Domsch; Volker Göhler

email:    hilke.domsch@gkz-ev.de

version: 0.0.2

language: de

narrator: Deutsch Female

edit: true
date: 2025-07-21
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/ISO_Exit_-_Right.svg/2880px-ISO_Exit_-_Right.svg.png

comment:  Rettungszeichen

attribute: Sicherheitszeichen von [Berufsgenossenschaft Holz und Metall](https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen)

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

title: Rettungszeichen

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

## Rettungszeichen

1. Welches dieser Zeichen ist ein Rettungszeichen?
===
<!-- --{{1}}--
Welches dieser Zeichen ist ein Rettungszeichen?
-->

<!-- data-randomize -->
- [[ @Rettungszeichen.Erste_Hilfe(10) ] ( @Warnzeichen.Automatischer_Anlauf(10) ) [ @Brandschutzzeichen.Brandmelder(10) ]]
- [    [X]           [ ]             [ ]     ]  Rettungszeichen



2. Füllen Sie den Lückentext aus.
===
<!-- --{{2}}--
Füllen Sie den Lückentext aus.
-->

<!-- data-randomize -->
Das Rettungszeichen für den [[ Sammelpunkt | (Notausgang) | Sani-Kasten]] ist grün und zeigt eine laufende Person mit einem Pfeil.
Rettungszeichen sind immer in der Farbe [[ rot |   blau   | (grün) ]] gehalten. 

Die Bedeutung der Rettungszeichen ist europaweit [[ unterschiedlich |   in den meisten Symbolen gleich   | (standardisiert) ]].
Die Rettungszeichen befinden sich in der Regel [[ in öffentlichen Gebäuden |   (in Fluren und Ausgängen)  | in Lagerräumen ]].



3. Ordnen Sie das jeweilige Symbol der richtigen Bedeutung zu.
===
<!-- --{{3}}--
Ordnen Sie das jeweilige Symbol im Bild 1, 2 und 3 der richtigen Bedeutung zu. 
-->

<!-- data-randomize -->
-   [[ @Rettungszeichen.Richtungspfeil_rechts(10) ]        ( @Rettungszeichen.Oeffentliche_Rettungsausruestung(10) )                 [ 	@Rettungszeichen.Arzt(10) ]]
- [    ( )              ( )                      ( )     ]  Fluchtweg links
- [    (X)              ( )                      ( )     ]  Fluchtweg rechts
- [    ( )              ( )                      ( )     ]  Rettungsring
- [    ( )              (X)                      ( )     ]  öffentliche Schutzausrüstung
- [    ( )              ( )                      (X)     ]  Arzt

---

Geschafft! 🙌
===
