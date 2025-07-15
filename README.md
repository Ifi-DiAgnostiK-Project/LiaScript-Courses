# DiAgnostiK_LiaScript

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/learn_more.svg)](https://LiaScript.github.io/)

Generated LiaScript Courses for DiAgnostiK Project

![DiAgnostiK Projekt](https://raw.githubusercontent.com/vgoehler/DiAgnostiK_LiaScript/refs/heads/main/img/WortBildMarkeSlogan_variante2_cropped.png)

## Location

- all courses are on our docs site:
- [https://ifi-diagnostik-project.github.io/LiaScript-Courses/](https://ifi-diagnostik-project.github.io/LiaScript-Courses/)

## Categories

Die Website sortiert automatisch anhand der `tags`, die in den Kursen verwendet werden, die Kurse in Kategorien ein.

### Tischler

Alle Kurse, die sich mit dem Beruf Tischler beschäftigen.

### SHK

Kurse, die sich mit dem Beruf Sanitär-, Heizungs- und Klimatechnik beschäftigen.

### Zahntechniker

Kurse, die sich mit dem Beruf Zahntechniker beschäftigen.

### Maler

Kurse, die sich mit dem Beruf Maler beschäftigen.

### Raumausstatter

Kurse, die sich mit dem Beruf Raumausstatter beschäftigen.

### Experimente

Experimentelle Kurse, die zeigen wie LiaScript mit verschiedenen Elementen funtioniert.

### Wissensspeicher

LiaScript-Kurse, die zeigen wie LiaScript Elemente geschrieben und angewandt werden können.

### Sonstige

Kurse ohne obige `tags` werden hier eingeordnet.
Weitere Tags können als Filter auf der Webseite genutzt werden.

## Title

Üblicherweise wird der Titel der ersten Überschrift als Titel des Kurses verwendet. Um diese für die Webseite alternativ angeben zu können existiert das `title` Element im Header.

## Beispiel

```markdown
<!--
title: Alternativer Titel
tags: Tischler
-->
```
oder als Liste:

```markdown
<!--
tags: 
- Tischler
- Grundkurs
- Anlagenwissen
-->
```

## Developer Note

- Workflows push automatically to website if there is a change in `courses/`
- we need a PAT for this with contents and workflows r/w
