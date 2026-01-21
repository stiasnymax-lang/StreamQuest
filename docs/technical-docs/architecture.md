---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Max Stiasny]
[Lukas Hoppart]

{: .no_toc }
# Architecture

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview
Diese Anwendung ist eine Flask-basierte Plattform für gemeinsame bestreiten von Herausforderungen, die es Nutzern ermöglicht, sich in Gruppen zu organisieren, Challenges zuzuweisen und den Fortschritt gemeinsam in Echtzeit zu verfolgen. Sie ist als serverseitig gerenderte Webanwendung mit dynamischen Erweiterungen (JSON-Endpunkte, Overlays) konzipiert, um es auch als OBS-Quelle Overlay zu generieren.

## Technology stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, Jinja, JSON
- Database: CURRENTLY SQLite3 BUT SQAlchemy Models have been built an could be implimented. Can be found under Main-Branch models.py
- 

## Codemap

## Home Screen
![Code Map](assets/images/CodeMap.png) 

## Cross-cutting concerns

Die größte schwierigkeit ist es Daten, welche im routing "/group/<int:group_id>/", verändert werden, auch in einem anderen Route (hier Overlay) in echt Zeit angepasst wird. Schwierig wird es auch werden alle Features, die am Anfang gebrainstormed wurde und in design decision abgebildet sind, eins zu eins umzusetzen oder generell zu implementieren. 

