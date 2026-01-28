---
title:  Datenmodell
parent: Technical Docs
nav_order: 2
---

# Datenmodell

Unsere Anwendung verwendet eine relationale SQLite-Datenbank, um Nutzer (Streamer), Gruppen und deren Challenges zu verwalten. Das Datenmodell ist bewusst kompakt gehalten und bildet nur die Teile ab, die für den aktuellen Funktionsumfang der Anwendung notwendig sind. Dadurch bleibt es übersichtlich und lässt sich später bei Bedarf leicht erweitern.

## Tabellen

### `users`

Speichert alle registrierten Nutzer, die sich in StreamQuest anmelden können.

| Feld         | Typ        | Beschreibung                               |
|--------------|------------|--------------------------------------------|
| `id`         | INTEGER PK | Eindeutige ID des Nutzers                  |
| `username`   | TEXT       | Anzeigename im System                      |
| `password`   | TEXT       | Passwort-Hash für den Login                |
| `email`      | TEXT       | E-Mail-Adresse des Nutzers                 |
| `abonoment`  | INTEGER    | Welche Stufe das Abo vom User ist          |


### `challenges`

Speichert alle Challenges, die einer Gruppe zugeordnet sind und später im Overlay angezeigt werden können.

| Feld          | Typ        | Beschreibung                                        |
|---------------|------------|-----------------------------------------------------|
| `id`          | INTEGER PK | Eindeutige ID der Challenge                         |
| `title`       | TEXT       | Kurzer Titel der Challenge                          |
| `description` | TEXT       | Optionale Detailbeschreibung                        |
| `difficulty`  | TEXT       | Schwierigkeitsgrad (z. B. Easy, Medium, Hard)       |
| `game_name`   | TEXT       | In Welchen Game Genre oder expliziten               |
| `time_needed` | INTEGER    | Wert für wie lange die Aufgabe dauert durchschn.    |


### `groups`

Repräsentiert eine StreamQuest-Gruppe, z. B. eine Community oder ein Team, für das Challenges erstellt werden.

| Feld         | Typ        | Beschreibung                                   |
|--------------|------------|------------------------------------------------|
| `id`         | INTEGER PK | Eindeutige ID der Gruppe                       |
| `name`       | TEXT       | Name der Gruppe                                |
| `password`   | TEXT       | Password des Users für Login u. Register       |
| `owner_id`   | INTEGER FK | Verweis auf `user.id` (Ersteller der Gruppe)   |
| `session_start` | TEXT    | Zeitpunkt wo Session gestartet wird            |


### `group_members`

Speichert alle User, die einer Gruppe zugeordnet sind und wer Owner ist.

| Feld          | Typ        | Beschreibung                                        |
|---------------|------------|-----------------------------------------------------|
| `owner_id`    | INTEGER FK | Verweis auf `user.id` (Ersteller der Gruppe)        |
| `user_id`     | INTEGER FK | Verweis auf `user.id` (zugehörige Gruppe)           |
| `group_id`    | INTEGER FK | Verweis auf `groups.id` (zugehörige Gruppe)         |

Primary keys sind `user_id` und `group_id`


### `group_challenges`

Speichert alle Challenges, die einer Gruppe zugeordnet sind und später im Overlay angezeigt werden können.

| Feld          | Typ        | Beschreibung                                            |
|---------------|------------|---------------------------------------------------------|
| `group_id`    | INTEGER FK | Verweis auf `groups.id` (zugehörige Gruppe)             |
| `challenge_id`| INTEGER FK | Verweis auf `challenger.id` (zugehörige Gruppe)         |
| `status`      | TEXT       | Status der Challenge (z. B. `active`, `done`, `queued`) |
| `assigned_at` | DATETIME   | Wann die challenge zugeordnet wurde                     |
| `startet_at`  | DATETIME   | Wann die challenge gestartet wurdet                     |
| `finished_at` | DATETIME   | Wann die challenge beendet wurde                        |

Primary keys sind `group_id` und `challenge_id`
`startet_at` und `finished_at` wichtig um eventuell später Zeit pro Challenge zu berechnen

## Beziehungen

- Ein **User** kann mehrere **Groups** besitzen (`users 1:n groups`).
- Eine **Group** gehört genau einem **Owner** (dem User, der sie erstellt hat).
- Eine **Group** kann mehrere **Challenges** enthalten (`groups 1:n challenges`).
- Jede **Challenge** ist genau einer **Group** zugeordnet und kann im Overlay dieser Gruppe angezeigt werden.

Dieses Datenmodell zeigt den aktuellen Stand der Anwendung und bietet eine Basis, auf der später zusätzliche Features hinzugefügt werden können.
