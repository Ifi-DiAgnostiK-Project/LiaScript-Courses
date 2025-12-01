<!--

author: Niklas Werner
version: 0.0.3
comment: This is a JSCAD example
language: de
edit: true
import:  https://raw.githubusercontent.com/LiaTemplates/jscad/0.0.1/README.md

tags:
  - experimente

-->

# JSCAD Example

``` js @JSCAD
"use strict"
/**
 * JSCAD Demonstration
 * Shows the basics of primitives, booleans and transforms
 */

const jscad = require('@jscad/modeling')
const { cuboid } = jscad.primitives
const { translate, mirrorX, mirrorY } = jscad.transforms
const { union } = jscad.booleans
const { colorize, colorNameToRgb } = jscad.colors

const pattern = (object, axis, number, distance) => {
  let result = object;
  for (let i = 0; i < number; i++) {
    const x_t = axis == 1 ? distance * i : 0
    const y_t = axis == 2 ? distance * i : 0
    const z_t = axis == 3 ? distance * i : 0
    const copy = translate([x_t, y_t, z_t], object)
    result = union(result, copy)
  }
  return result
}

const main = () => {
  const leg = translate([2,4,0], cuboid({ size: [1, 1, 5] }))
  const legs = union(leg, mirrorX(leg))
  const legss = union(legs, mirrorY(legs))
  const plate = translate([0,0,3], cuboid({ size: [8, 12, 1] }))
  const table = colorize(colorNameToRgb('burlywood'), union(legss, plate))

  const fliese = translate([2.75,4.9,3.5], cuboid({ size: [1, 1, 0.1] }))
  const fliesen = pattern(pattern(fliese, 1, 6, -1.1), 2, 10, -1.1)
  const fliesen_color = colorize(colorNameToRgb('white'), fliesen)

  return [table, fliesen_color]
}

module.exports = { main }

```

