<!--
author: Niklas Werner
version: 0.0.2
script: https://cdn.jsdelivr.net/npm/konva@latest/konva.min.js
comment: This is a test for the Konva library in LiaScript, demonstrating how to create shapes and measure their dimensions using arrows and labels.
edit: true

title: Flächenberechnungs Quiz

tags:
    - experimente
    - konva

@Konva
<div id='container-@0'></div>

<script>
    void setTimeout(() => {
        (function(){
        // Stage- und Layer-Einstellungen
            const stage = new Konva.Stage({
            container: "container-@0",
            width: 400,
            height: 250, // Höhe kann angepasst werden
            });

            @1

            stage.draw();
            
        })();
    }, 100);
</script>
@end


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

# Konva Quiz

LiaScript Badges
========

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/main/konva-quiz.md)

[![GitHub](https://img.shields.io/badge/Ansehen%20auf-GitHub-181717?logo=github)](https://github.com/vgoehler/DiAgnostiK_LiaScript/blob/main/konva-quiz.md)

[![Raw](https://img.shields.io/badge/Raw-Inhalt-blue)](https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/main/konva-quiz.md)


# Konva

Welchen Flächeninhalt haben die Formen?


<section class="flex-container">

<div class="flex-child" style="min-width: 250px">

``` js @Konva(@uid)

const layer = new Konva.Layer();
stage.add(layer);

// Rechteck-Parameter
const rectWidth = 300; // Breite (2:1-Verhältnis)
const rectHeight = 150; // Höhe

// Positionierung des Rechtecks im Stage
const rectX = (stage.width() - rectWidth) / 2;
const rectY = (stage.height() - rectHeight) / 2;

// Pfad für das abgeschnittene Rechteck
const pathData = `
  M ${rectX} ${rectY}
  L ${rectX + rectWidth} ${rectY}
  L ${rectX + rectWidth} ${rectY + rectHeight} 
  L ${rectX} ${rectY + rectHeight}
  Z
`;

// Erstelle das Rechteck
const rect = new Konva.Path({
  data: pathData,
  fill: 'lightblue',
  stroke: 'black',
  strokeWidth: 2
});
layer.add(rect);

// Messpfeile und Beschriftungen
// 1. Breite-Messung (200px)
const widthArrow = new Konva.Arrow({
  points: [
    rectX, rectY - 20, // Startpunkt oben
    rectX + rectWidth, rectY - 20 // Endpunkt rechts
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(widthArrow);

const widthLabel = new Konva.Text({
  x: rectX + rectWidth / 2,
  y: rectY - 40,
  text: '4',
  fill: 'black',
  fontSize: 12,
  align: 'center'
});
layer.add(widthLabel);

// 2. Höhe-Messung (100px)
const heightArrow = new Konva.Arrow({
  points: [
    rectX - 20, rectY, // Startpunkt rechts
    rectX - 20, rectY + rectHeight // Endpunkt unten
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(heightArrow);

const heightLabel = new Konva.Text({
  x: rectX - 40,
  y: rectY + rectHeight / 2,
  text: '2',
  fill: 'black',
  fontSize: 12,
  rotation: -90 // Text rotieren
});
layer.add(heightLabel);

```
</div>

<div class="flex-child" style="min-width: 100px">

<!-- data-randomize -->
- [(X)] 8
- [( )] 11
- [( )] 42

</div>

</section>


<section class="flex-container">

<div class="flex-child" style="min-width: 250px">

``` js @Konva(@uid)

const layer = new Konva.Layer();
stage.add(layer);

// Oval-Parameter
const ellipseWidth = 200; // Breite des Ovals
const ellipseHeight = 100; // Höhe des Ovals
const ellipseX = (stage.width()) / 2; // Zentriert horizontal
const ellipseY = (stage.height()) / 2; // Zentriert vertikal

// Erstelle das Oval
const ellipse = new Konva.Ellipse({
  x: ellipseX,
  y: ellipseY,
  width: ellipseWidth,
  height: ellipseHeight,
  fill: 'lightblue',
  stroke: 'black',
  strokeWidth: 2
});
layer.add(ellipse);

// Messpfeile und Beschriftungen
// 1. Horizontale Messung (Breite)
const widthArrow = new Konva.Arrow({
  points: [
    ellipseX - (ellipseWidth / 2), ellipseY, // Startpunkt oben
    ellipseX + (ellipseWidth / 2), ellipseY // Endpunkt rechts
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2,
});
layer.add(widthArrow);

const widthLabel = new Konva.Text({
  x: ellipseX + 20,
  y: ellipseY - 20,
  text: '20',
  fill: 'black',
  fontSize: 12,
  align: 'center'
});
layer.add(widthLabel);

// 2. Vertikale Messung (Höhe)
const heightArrow = new Konva.Arrow({
  points: [
    ellipseX, ellipseY - (ellipseHeight / 2), // Startpunkt rechts
    ellipseX, ellipseY + (ellipseHeight / 2) // Endpunkt unten
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2,
  lineJoin: 'round'
});
layer.add(heightArrow);

const heightLabel = new Konva.Text({
  x: ellipseX - 10,
  y: ellipseY - 10,
  text: '10',
  fill: 'black',
  fontSize: 12,
  rotation: -90 // Text rotieren
});
layer.add(heightLabel);
```
</div>

<div class="flex-child" style="min-width: 100px">

<!-- data-randomize -->
- [( )] 1
- [( )] 42
- [(X)] 628

</div>

</section>


<section class="flex-container">

<div class="flex-child" style="min-width: 250px">

``` js @Konva(@uid)

const layer = new Konva.Layer();
stage.add(layer);

// Rechteck-Parameter
const rectWidth = 300; // Breite (2:1-Verhältnis)
const rectHeight = 150; // Höhe
const cutOffX = rectWidth * 0.25; // 25% der Breite
const cutOffY = rectHeight * 0.75; // 75% der Höhe

// Positionierung des Rechtecks im Stage
const rectX = (stage.width() - rectWidth) / 2;
const rectY = (stage.height() - rectHeight) / 2;

// Pfad für das abgeschnittene Rechteck
const pathData = `
  M ${rectX} ${rectY}
  L ${rectX + rectWidth} ${rectY}
  L ${rectX + rectWidth} ${rectY + cutOffY} 
  L ${rectX + cutOffX} ${rectY + cutOffY}
  L ${rectX + cutOffX} ${rectY + rectHeight}
  L ${rectX} ${rectY + rectHeight}
  Z
`;

// Erstelle das Rechteck
const rect = new Konva.Path({
  data: pathData,
  fill: 'lightblue',
  stroke: 'black',
  strokeWidth: 2
});
layer.add(rect);

// Messpfeile und Beschriftungen
// 1. Breite-Messung (200px)
const widthArrow = new Konva.Arrow({
  points: [
    rectX, rectY - 20, // Startpunkt oben
    rectX + rectWidth, rectY - 20 // Endpunkt rechts
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(widthArrow);

const widthLabel = new Konva.Text({
  x: rectX + rectWidth / 2,
  y: rectY - 40,
  text: '200',
  fill: 'black',
  fontSize: 12,
  align: 'center'
});
layer.add(widthLabel);

// 2. Höhe-Messung (100px)
const heightArrow = new Konva.Arrow({
  points: [
    rectX - 20, rectY, // Startpunkt rechts
    rectX - 20, rectY + rectHeight // Endpunkt unten
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(heightArrow);

const heightLabel = new Konva.Text({
  x: rectX - 40,
  y: rectY + rectHeight / 2,
  text: '100',
  fill: 'black',
  fontSize: 12,
  rotation: -90 // Text rotieren
});
layer.add(heightLabel);

// 3. Abgeschnittenes Viertel (50x25px)
// Horizontale Messung (50px)
const cutWidthArrow = new Konva.Arrow({
  points: [
    rectX + cutOffX, rectY + rectHeight, // Startpunkt unten
    rectX + rectWidth, rectY + rectHeight // Endpunkt rechts
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(cutWidthArrow);

const cutWidthLabel = new Konva.Text({
  x: rectX + (cutOffX + rectWidth) / 2,
  y: rectY + cutOffY + 40,
  text: '150',
  fill: 'black',
  fontSize: 12,
  align: 'center'
});
layer.add(cutWidthLabel);

// Vertikale Messung (25px)
const cutHeightArrow = new Konva.Arrow({
  points: [
    rectX + rectWidth, rectY + cutOffY, // Startpunkt oben
    rectX + rectWidth, rectY + rectHeight // Endpunkt unten
  ],
  pointerLength: 5,
  pointerWidth: 3,
  pointerAtBeginning: true,
  stroke: 'black',
  strokeWidth: 2
});
layer.add(cutHeightArrow);

const cutHeightLabel = new Konva.Text({
  x: rectX + rectWidth + 10,
  y: rectY + (cutOffY + rectHeight) / 2 + 10,
  text: '25',
  fill: 'black',
  fontSize: 12,
  rotation: -90
});
layer.add(cutHeightLabel);

```
</div>

<div class="flex-child" style="min-width: 100px">

<!-- data-randomize -->
- [( )] 1
- [( )] 182.761
- [(X)] 16.250
- [( )] 666
- [( )] 42

</div>

</section>
