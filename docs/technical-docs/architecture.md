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
Diese Anwendung ist eine Flask-basierte Plattform für gemeinsame bestreiten von Herausforderungen, die es Nutzern ermöglicht, sich in Gruppen zu organisieren, Challenges zuzuweisen und den Fortschritt gemeinsam in Echtzeit zu verfolgen. Sie ist als serverseitig gerenderte Webanwendung mit seld reloading DOM-Elementen konzipiert, um es auch als OBS-Quelle Overlay zu generieren und nutzbar zu gestalten.

## Technology stack
- Backend: Python (Flask)
- Frontend: HTML, CSS, Jinja, JSON
- Database: SQLite-Datenbank


## Codemap

### Überblick über die App-Struktur
Die App ist eine Flask-Webanwendung, bei der sich alles um Gruppen dreht, die gemeinsam Challenges verwalten und absolvieren. Die Struktur orientiert sich an einem einfachen MVC-Ansatz: Routen steuern die Logik, die Daten liegen in einer SQLite-Datenbank, und die Darstellung erfolgt über Jinja-Templates.

### Zentrale Bestandteile

**Applikation & Routing**
- Die gesamte App wird in einer zentralen Flask-Datei initialisiert.
- Dort sind alle Routen definiert und nach Themen gegliedert (Login, Gruppen, Challenges, Profil, statische Seiten).
- Geschützte Bereiche verwenden einen login_required-Decorator zur Zugriffskontrolle.

**Datenbank-Schicht**
- Es wird eine SQLite-Datenbank verwendet, angebunden über ein eigenes db-Modul. 
- SQL-Abfragen werden direkt in den Routen ausgeführt, ohne ORM.
- Zentrale Entitäten sind User, Groups, Challenges sowie Zuordnungstabellen für Mitgliedschaften und Challenge-Status.

**Authentifizierung & Sessions**
- Die Anmeldung erfolgt über Sessions.
- Nach dem Login wird die User-ID in der Session gespeichert und in geschützten Routen verwendet.
- Formulare (Login, Registrierung, Gruppen) werden über Flask-WTF umgesetzt.

**Gruppen & Challenges (Kernfunktionalität)**
- Gruppen bilden den Kern der Anwendung.
- User können Gruppen erstellen, ihnen beitreten und Challenges verwalten.
- Challenges durchlaufen verschiedene Zustände (queued, active, done).
- Die Gruppen-Seite dient als zentrale Arbeitsoberfläche für alle gruppenbezogenen Aktionen.

**Views & Templates**
- Die Benutzeroberfläche basiert auf Jinja-Templates.
- Dynamische Seiten (Gruppen, Challenges, Profil) sind klar von statischen Seiten (Guide, Support) getrennt.
- Eine Overlay-Route kann wahlweise HTML oder JSON ausgeben, um Inhalte flexibel wiederzuverwenden.

**Views & Templates**
- Fokus auf Einfachheit und Verständlichkeit statt komplexer Abstraktionen.
- Klare Trennung von Logik, Daten und Darstellung.
- Die App ist bewusst modular aufgebaut und lässt sich gut erweitern (z. B. Sessions, Rollen, bessere Suche).

## Cross-cutting concerns

Die größte schwierigkeit ist es Daten, welche im routing "/group/<int:group_id>/", verändert werden, auch in einem anderen Route (hier Overlay) in echt Zeit angepasst wird. Schwierig wird es auch werden alle Features, die am Anfang gebrainstormed wurde und in design decision abgebildet sind, eins zu eins umzusetzen oder generell zu implementieren. 

