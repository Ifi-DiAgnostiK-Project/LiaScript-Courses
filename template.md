<!--
author: <name hier - semikolon trennt mehrere Autoren>
email:    <email hier - semikolon trennt mehrere Emails>
language: de
narrator: German Female
version: 0.0.1
edit: true
date: <Datum hier>
comment: <Kommentar hier>
title: Templatefile <der Title für die Übersichtsseite>

tags:
  - Wissensspeicher
  - <Tag1>
  - <Tag2>

link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css

icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: <Pfad zum Logo hier>

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md
        https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Textilpflegesymbole/refs/heads/main/makros.md

-->

# LiaScript Makros

## Bilder

Bilder importiert aus dem ISO 7010 Repository

> `@Brandschutzzeichen.Richtungspfeil_Rechts(10)`

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

## Layouts

Wir nutzen die flex styles:

```html
<section class="flex-container">

<div class="flex-child" style="min-width: 250px">
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)

</div>

<div class="flex-child" style="min-width: 250px">

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

</div>

</section>
```

<section class="flex-container">

<div class="flex-child" style="min-width: 250px">
@Brandschutzzeichen.Richtungspfeil_Rechts_unten(10)

</div>

<div class="flex-child" style="min-width: 250px">

@Brandschutzzeichen.Richtungspfeil_Rechts(10)

</div>

</section>

