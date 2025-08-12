<!--
author: <name hier - semikolon trennt mehrere Autoren>
email:    <email hier - semikolon trennt mehrere Emails>
language: de
narrator: German Female
version: 0.0.1
edit: true
comment: <Kommentar hier>
title: <der Title für die Übersichtsseite>

tags:
  - <Tag1>
  - <Tag2>

icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/img/Logo_234px.png
logo: <Pfad zum Logo hier>

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_DragAndDrop_Template/refs/heads/main/README.md

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript_ImageQuiz/refs/heads/main/README.md

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Piktogramme/refs/heads/main/makros.md

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Holzarten/refs/heads/main/makros.md

import: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/Bildersammlung/refs/heads/main/makros.md

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

.image-container {
  width: 200px;
  height: 200px;
  border: 1px solid #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background-color: #f8f8f8;
}

.image-container img {
  width: fit-content;
  height: fit-content;
  object-fit: cover;
  display: block;
}

@end

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

