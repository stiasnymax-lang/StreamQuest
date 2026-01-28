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