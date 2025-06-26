<!--
author: Volker Göhler
email:    volker.goehler@informatik.tu-freiberg.de
language: de
narrator: German Female
version: 0.0.1
edit: true
comment: This is a template for a LiaScript course. We define the header here and handle the imports!

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

import: https://raw.githubusercontent.com/vgoehler/DiAgnostiK_Bilder_Test/refs/heads/main/makros.md

-->

# LiaScript Template

[![LiaScript Course](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/vgoehler/DiAgnostiK_LiaScript/blob/main/template.md?raw=true)
[![GitHub](https://img.shields.io/badge/Ansehen%20auf-GitHub-181717?logo=github)](https://liascript.github.io/LiveEditor/?/show/file/https://github.com/vgoehler/DiAgnostiK_LiaScript/blob/main/template.md)
[![Rohinhalt](https://img.shields.io/badge/Raw-Inhalt-blue)](https://liascript.github.io/LiveEditor/?/show/file/https://github.com/vgoehler/DiAgnostiK_LiaScript/blob/main/template.md?raw=true)

# LiaScript Makros

## Bilder

Bilder importiert aus dem DiagnostiK_Bilder Repository

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

