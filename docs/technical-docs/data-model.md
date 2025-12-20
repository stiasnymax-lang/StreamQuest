# Datenmodell

Unsere Anwendung verwendet eine relationale SQLite-Datenbank, um Nutzer (Streamer), Gruppen und deren Challenges zu verwalten. Das Datenmodell ist bewusst kompakt gehalten und bildet nur die Teile ab, die für den aktuellen Funktionsumfang der Anwendung notwendig sind. Dadurch bleibt es übersichtlich und lässt sich später bei Bedarf leicht erweitern.

## Tabellen

### `users`

Speichert alle registrierten Nutzer, die sich in StreamQuest anmelden können.

| Feld         | Typ        | Beschreibung                               |
|--------------|------------|--------------------------------------------|
| `id`         | INTEGER PK | Eindeutige ID des Nutzers                  |
| `username`   | TEXT       | Anzeigename im System                      |
| `email`      | TEXT       | E-Mail-Adresse des Nutzers                 |
| `password`   | TEXT       | Passwort-Hash für den Login                |
| `created_at` | TEXT       | Zeitpunkt der Registrierung (ISO-String)   |


### `groups`

Repräsentiert eine StreamQuest-Gruppe, z. B. eine Community oder ein Team, für das Challenges erstellt werden.

| Feld         | Typ        | Beschreibung                               |
|--------------|------------|--------------------------------------------|
| `id`         | INTEGER PK | Eindeutige ID der Gruppe                   |
| `name`       | TEXT       | Name der Gruppe                            |
| `owner_id`   | INTEGER FK | Verweis auf `users.id` (Ersteller der Gruppe) |
| `created_at` | TEXT       | Erstellungszeitpunkt der Gruppe            |


### `challenges`

Speichert alle Challenges, die einer Gruppe zugeordnet sind und später im Overlay angezeigt werden können.

| Feld          | Typ        | Beschreibung                                        |
|---------------|------------|-----------------------------------------------------|
| `id`          | INTEGER PK | Eindeutige ID der Challenge                         |
| `group_id`    | INTEGER FK | Verweis auf `groups.id` (zugehörige Gruppe)         |
| `title`       | TEXT       | Kurzer Titel der Challenge                          |
| `description` | TEXT       | Optionale Detailbeschreibung                        |
| `category`    | TEXT       | Kategorie (z. B. Gaming, Chat, IRL)                 |
| `difficulty`  | TEXT       | Schwierigkeitsgrad (z. B. Easy, Medium, Hard)       |
| `status`      | TEXT       | Status der Challenge (z. B. `open`, `done`, `skip`) |


## Beziehungen

- Ein **User** kann mehrere **Groups** besitzen (`users 1:n groups`).
- Eine **Group** gehört genau einem **Owner** (dem User, der sie erstellt hat).
- Eine **Group** kann mehrere **Challenges** enthalten (`groups 1:n challenges`).
- Jede **Challenge** ist genau einer **Group** zugeordnet und kann im Overlay dieser Gruppe angezeigt werden.

Dieses Datenmodell zeigt den aktuellen Stand der Anwendung (Login, Gruppen, Challenges inkl. Overlay) und bietet eine Basis, auf der später zusätzliche Features hinzugefügt werden können.
