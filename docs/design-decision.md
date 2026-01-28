---
title: Design Decisions
nav_order: 3
---

{: .label }
[Max Stiasny]
[Lukas Hoppart]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: How to access the database - SQL or SQLAlchemy 

### Meta

Status
: Work in progress - **Decided** - Obsolete

### Problem statement

Sollen wir CRUD-Operationen (Create, Read, Update, Delete) auf der Datenbank durch reines SQL oder durch SQLAlchemy als Object-Relational Mapper (ORM) durchführen?

Unsere Webanwendung ist in Python mit Flask geschrieben und greift auf eine SQLite-Datenbank zu. Für den aktuellen Projektumfang ist dieses Setup ausreichend.

### Decision

Wir bleiben bei reinem SQL.

Unser Team muss sich derzeit noch in mehrere für uns neue Technologien einarbeiten, unter anderem Python und CSS. Ein weiteres Element im Technologie-Stack würde uns aktuell verlangsamen.

Außerdem ist es wahrscheinlich, dass wir die Anwendung nach der MVP-Validierung komplett neu schreiben. Das eröffnet uns in etwa 4–6 Monaten die Möglichkeit, technologische Entscheidungen erneut zu überprüfen.
*Decision was taken by:* Max Stiasny

### Regarded options

Wir haben zwei Alternativen in Betracht gezogen:

+ Plain SQL
+ SQLAlchemy

| Kriterium | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Know-how** | ✔️ Wir wissen, wie man SQL schreibt | ❌ Einarbeitung in ORM-Konzepte und SQLAlchemy notwendig |
| **Change DB schema** | ❌ SQL ist über den Code verteilt | ❔ Vorteil: Klassenstruktur, Nachteil: zusätzlich Alembic nötig |
| **Switch DB engine** | ❌ Unterschiedliche SQL-Dialekte | ✔️ Abstrahiert die Datenbank-Engine |


---

## 02: Aktualisierung der DOM-Elemente ohne JavaScript

### Meta

Status
: Work in progress - **Decided** - Obsolete

### Problem statement

Wir standen vor der Frage, wie die DOM-Elemente der overlay.html aktualisiert werden sollen, wenn sich die zugrunde liegenden Daten auf einem anderen HTTP-Pfad ändern.

Da JavaScript nicht erlaubt ist, konnten übliche clientseitige Lösungen wie DOM-Manipulation, Polling mit fetch oder WebSockets nicht eingesetzt werden. Es mussten daher rein HTML-basierte Alternativen betrachtet werden.

### Decision

Wir verwenden einen Meta-Refresh zur regelmäßigen Aktualisierung der Seite: 

```markdown
<meta http-equiv="refresh" content="0.5">
```
### Cause

Auch wenn diese Lösung ressourcenintensiv ist, erfüllt sie die funktionalen Anforderungen unter den gegebenen Einschränkungen und lässt sich einfach und schnell umsetzen.

- JavaScript ist explizit nicht erlaubt
- Die Lösung funktioniert unabhängig vom Server-Pfad der Daten
- Geringe Komplexität und schneller Implementierungsaufwand
- Akzeptabel für den aktuellen Projektumfang (MVP)

Eine effizientere Lösung kann zu einem späteren Zeitpunkt evaluiert werden, sofern die Einschränkungen entfallen oder sich die Anforderungen ändern.

*Decision was taken by:* Max Stiasny

### Regarded options

Wir haben drei Alternativen in Betracht gezogen:

+ Meta-Refresh (<meta http-equiv="refresh">)
+ Server-seitiges Rendering mit vollständigem Reload
+ JavaScript-basierte DOM-Updates (nicht erlaubt)

| Kriterium | Meta-Refresh | Server-seitiges Rendering | JavaScript | 
| --- | --- | --- | --- |
| **JavaScript-frei** | ✔️  | ✔️ | ❌ |
| **Implementierungsaufwand** | ✔️ Sehr gering | ❔ Mittel | ✔️ Gering |
| **Performance / Ressourcen** | ❌ Hocher Ressourcenverbrauch | ❔ Abhängig vom Server | ✔️ Effizient |
| **Echtzeit-Aktualität** | ✔️ Quasei-Echtzeit  | ❌ Nur Bei Reload | ✔️ Echtzeit |


---

## 03: Entfernung des Pricing- und Abonnement-Systems

### Meta

Status
: Work in progress - **Decided** - Obsolete

### Problem statement

Es stellte sich die Frage, ob ein Pricing-Modell mit angebundenem Abonnement-System Teil des Projekts sein soll.

Während der Umsetzung wurde deutlich, dass das Pricing- und Abo-System zusätzliche technische und konzeptionelle Komplexität einführt, ohne ein zentrales (Key-)Element des Projekts darzustellen oder zur Erreichung der Projektziele wesentlich beizutragen.

### Decision

Wir entfernen das Pricing-Modell inklusive des zugehörigen Abonnement-Systems vollständig aus dem Projekt.

### Cause

Wir entfernen das Pricing-Modell inklusive des zugehörigen Abonnement-Systems vollständig aus dem Projekt.

- Das Abo-System ist kein Kernelement der Anwendung
- Es erhöht die Komplexität von Backend, Datenmodell und UI unnötig
- ein Mehrwert für den aktuellen Projektfokus (MVP)

Durch den Verzicht auf Pricing können wir uns auf die wesentlichen Funktionen konzentrieren und die Entwicklungszeit effizienter nutzen.

*Decision was taken by:* Max Stiasny

### Regarded options

Wir haben zwei Alternativen in Betracht gezogen:

+ Beibehaltung des Pricing- und Abonnement-Systems
+ Entfernung des Pricing- und Abonnement-Systems
+ JavaScript-basierte DOM-Updates (nicht erlaubt)

| Kriterium | Mit Pricing & Abo | Ohne Pricing & Abo |
| --- | --- | --- |
| **Projektfokus** | ❌ Ablenkung vom Kernziel | ✔️ Fokus auf Kernfunktionen |
| **Technische Komplexität** | ❌ Hoch | ✔️ Gering |
| **Implementierungsaufwand** | ❌ Hoch | ✔️ Niedrig |
| **Mehrwert für MVP** | ❌ Gering | ✔️ Hoch |


---

## 04: Gruppenbeitritt und Zugriffsschutz über Redirect-Flow

### Meta

Status
: Work in progress - **Decided** - Obsolete

### Problem statement

Wir mussten entscheiden, wie der Beitritt zu Gruppen sowie der Zugriffsschutz auf die Gruppenseite umgesetzt werden soll.

Anforderungen dabei:
- Nur eingeloggte Nutzer dürfen Gruppen beitreten und Gruppenseiten sehen.
- Gruppen können passwortgeschützt sein.
- Nutzer sollen nicht mehrfach derselben Gruppe beitreten können.
- Die Lösung soll einfach bleiben und ohne zusätzliche Komplexität (z. B. separate Access-Control-Layer) funktionieren.

### Decision

Wir implementieren einen zweistufigen Flow:

1. /group/<group_id>/ ist die zentrale Gruppenseite.

- Dort wird bei jedem Aufruf geprüft, ob der Nutzer Mitglied ist.
- Falls nicht, erfolgt ein Redirect auf /join/<group_id>/.

2. /join/<group_id>/ dient als Beitrittsseite (Passwortabfrage).

- Bei GET: Formular anzeigen
- Bei POST: Passwort prüfen und Nutzer in group_members eintragenkt.

### Cause

- Klare Trennung von Verantwortlichkeiten
    - /group/... = Inhalte anzeigen / Gruppen-Features
    - /join/... = Membership herstellen (mit Passwortprüfung)
- Zuverlässiger Zugriffsschutz
    - Selbst wenn jemand direkt die URL /group/<id>/ kennt, greift die Membership-Prüfung und leitet auf den Join-Prozess um
- Verhindert doppelte Mitgliedschaften
    - Vor dem Eintragen wird geprüft, ob bereits ein Eintrag in group_members existiert.
- Einfacher Implementierungsaufwand
- Bessere User Experience als “harte” Fehler
    - Statt 403/404 bekommen Nutzer direkt den „richtigen nächsten Schritt“ (Join-Seite), wenn ihnen die Berechtigung fehlt.

*Decision was taken by:* Max Stiasny

### Regarded options

Wir haben zwei Alternativen in Betracht gezogen:

+ Redirect-Flow: Zugriff auf Gruppenseite prüft Membership und leitet ggf. auf Join-Seite um (gewählt)
+ Gruppenseite immer öffentlich, Inhalte je nach Membership ausblenden
+ Bei fehlender Membership direkt 403 Forbidden anzeigen (kein Join-Flow)

| Kriterium | Redirect-Flow (gewählt) | Öffentlich + Ausblenden | 403 Forbidden | 
| --- | --- | --- | --- |
| **Zugriffsschutz** | ✔️ Stark  | ❔ Fehleranfällig | ✔️ Stark |
| **User Experience** | ✔️ Führt Nutzer direkt zum Beitritt | ❌ Unklar, was zu tun ist | ❌ Sackgasse |
| **Implementierungsaufwand** | ✔️ Gering | ❔ Mittel (viele Sonderfälle im Template) | ✔️ Gering |
| **MVP-Tauglichkeit** | ✔️ Hoch | ❔ Mittel | ❌ Niedrig |


---

## 05: Authentifizierung über Flask-Session und `login_required`

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Geschützte Bereiche (z. B. Gruppen, Overlay, Profil) dürfen nur von eingeloggten Nutzern aufgerufen werden.

### Entscheidung
Wir verwenden **session-basierte Authentifizierung** über Flask (`session['user_id']`) und schützen Routen mit einem **`login_required` Decorator**.

### Begründung
- Einfach umzusetzen und gut für ein MVP geeignet  
- Keine zusätzliche Infrastruktur (JWT, OAuth etc.) nötig  
- Klare und zentrale Zugriffskontrolle

### Betrachtete Optionen

| Kriterium | Session + Decorator (gewählt) | JWT/Token | OAuth |
|----------|-------------------------------|-----------|-------|
| Aufwand | ✔️ niedrig | ❌ höher | ❌ hoch |
| MVP-tauglich | ✔️ | ❔ | ❌ |


---

## 06: Passwort-Handling im Klartext für das MVP

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Passwörter für Login und Gruppenbeitritt müssen geprüft werden. Es stellt sich die Frage, ob diese gehasht oder direkt verglichen werden sollen.

### Entscheidung
Passwörter werden im MVP **ungehasht gespeichert und verglichen**.

### Begründung
- Fokus liegt auf Funktionalität und Lernziel  
- Reduzierte Komplexität  
- Hashing kann in einer späteren Version ergänzt werden

### Konsequenzen / Risiken
- ❌ Sicherheitsrisiko  
- ❌ Nicht best-practice-konform  
- ✅ Schnell und einfach für MVP

### Betrachtete Optionen

| Kriterium | Klartext (gewählt) | Hashing |
|----------|-------------------|---------|
| Aufwand | ✔️ niedrig | ❌ höher |
| Sicherheit | ❌ schlecht | ✔️ gut |


---

## 07: Zugriffsschutz über Membership-Check mit Redirect statt 403

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Nicht-Mitglieder sollen keinen Zugriff auf Gruppen- oder Overlay-Seiten haben, sollen aber möglichst einfach beitreten können.

### Entscheidung
Bei fehlender Mitgliedschaft wird der Nutzer **auf die Join-Seite weitergeleitet**, statt einen 403-Fehler auszugeben.

### Begründung
- Bessere User Experience  
- Klare Führung zum nächsten Schritt  
- Einfache Umsetzung

### Betrachtete Optionen

| Kriterium | Redirect (gewählt) | 403 Forbidden |
|----------|--------------------|---------------|
| UX | ✔️ gut | ❌ schlecht |
| Aufwand | ✔️ niedrig | ✔️ niedrig |


---

## 08: Suche mit SQL `LIKE` und vorbereinigtem Query-Parameter

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Es wird eine einfache Suchfunktion für Gruppen und Challenges benötigt.

### Entscheidung
Die Suche erfolgt über `LIKE '%query%'` in SQL. Der Suchstring wird in Python mit `strip()` und `lower()` vorbereitet.

### Begründung
- Sehr einfacher Ansatz  
- Ausreichend für kleine Datenmengen  
- Keine zusätzlichen Abhängigkeiten

### Konsequenzen / Risiken
- ❌ Case-Insensitive-Verhalten DB-abhängig  
- ❌ Performance bei großen Datenmengen  
- ✅ MVP-geeignet

---

## 09: Statusmodell für Gruppen-Challenges

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Challenges innerhalb einer Gruppe können geplant, aktiv oder abgeschlossen sein.

### Entscheidung
Wir verwenden ein Statusfeld mit den Werten:
- `queued`
- `active`
- `done`

Zusätzlich werden Zeitstempel wie `started_at` und `finished_at` gespeichert.

### Begründung
- Klare Domänenlogik  
- Gute Erweiterbarkeit  
- Einfache Filterung nach Status

---

## 10: Nur eine aktive Challenge pro Gruppe (Applikationslogik)

### Meta
**Status**  
: In Arbeit – **Entschieden** – Obsolet

### Problemstellung
Pro Gruppe darf immer nur eine Challenge aktiv sein.

### Entscheidung
Die Einschränkung wird **applikationsseitig** umgesetzt:
1. Alle aktiven Challenges werden auf `queued` gesetzt  
2. Die gewählte Challenge wird auf `active` gesetzt

### Begründung
- Einfacher als DB-Constraints  
- MVP-freundlich  
- Verständlich im Code

### Konsequenzen / Risiken
- ❌ Race-Conditions bei parallelen Requests möglich  
- ✅ Akzeptabel bei geringer Last

---