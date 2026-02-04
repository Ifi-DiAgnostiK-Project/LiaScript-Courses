# DiAgnostiK_LiaScript

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/learn_more.svg)](https://LiaScript.github.io/)

![GitHub contributors](https://img.shields.io/github/contributors/Ifi-DiAgnostiK-Project/LiaScript-Courses)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Ifi-DiAgnostiK-Project/LiaScript-Courses)
![GitHub repo size](https://img.shields.io/github/repo-size/Ifi-DiAgnostiK-Project/LiaScript-Courses)
[![GitHub issues](https://img.shields.io/github/issues/Ifi-DiAgnostiK-Project/LiaScript-Courses)](https://github.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/issues)

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

### Belehrung

Kategorie für Belehrungen.

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

### Change Detection and State Persistence

The deployment workflow uses a checksum-based state persistence mechanism to track changes across workflow runs. This ensures:
- Accurate detection of changed files across multiple commits
- Efficient processing of only modified courses
- Persistent state management via GitHub Actions artifacts

For detailed information, see [docs/checksum-state-persistence.md](docs/checksum-state-persistence.md).

### Tag and Release Management

The repository includes a cleanup script to manage course releases and tags. Each time a course is changed, a new SCORM course is built with a corresponding version tag. Use the cleanup script to keep only the most recent versions:

```bash
# See what would be deleted (dry run)
python3 scripts/cleanup_old_releases.py

# Delete old tags/releases, keeping last 2 versions
python3 scripts/cleanup_old_releases.py --execute

# Keep last 3 versions
python3 scripts/cleanup_old_releases.py --execute --keep 3
```

For detailed documentation, see [scripts/CLEANUP_SCRIPT_README.md](scripts/CLEANUP_SCRIPT_README.md).
