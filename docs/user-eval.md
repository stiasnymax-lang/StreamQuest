---
title: User Evaluation
nav_order: 4
---

{: .label }
[Max Stiasny]
[Lukas Hoppart]

{: .no_toc }
# User evaluation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Registration & Group Onboarding

### Meta

Status
: **Work in progress** – **Done** – Obsolete

Updated
: 28-Jan-2026

### Goal

Ziel dieser Evaluation war es zu untersuchen,  
**wie verständlich und effizient der Registrierungs- und Gruppenbeitrittsprozess für neue Nutzer ist**.

Zentrale Fragestellungen:
- Wie lange benötigen Nutzer, um einen Account zu erstellen?
- Finden Nutzer selbstständig eine Gruppe oder erstellen eine neue?
- Wo treten Unsicherheiten oder Abbrüche auf?

### Method

Die Evaluation wurde als **moderierter Usability-Test** durchgeführt.

- **Teilnehmer:** 1 Testpersonen (nicht am Projekt beteiligt)
- **Voraussetzungen:** Keine Vorkenntnisse von StreamQuest
- **Setup:**  
  - Desktop-Browser  
  - Lokale Entwicklungsumgebung mit Beispieldaten  
- **Aufgaben:**
  1. Registrierung eines neuen Benutzerkontos
  2. Login mit dem erstellten Account
  3. Beitritt zu einer bestehenden Gruppe *oder* Erstellung einer neuen Gruppe
  4. Aufruf der Gruppenansicht

Während des Tests wurden folgende Daten erhoben:
- Benötigte Zeit pro Aufgabe
- Beobachtete Probleme oder Rückfragen
- Subjektives Feedback der Nutzer nach Abschluss

Alle Testergebnisse wurden manuell protokolliert.

### Results

**Quantitative Ergebnisse:**
- Durchschnittliche Zeit für Registrierung: **ca. 2 Minuten**
- Erfolgsquote Registrierung: **100 %**
- Erfolgsquote Gruppenbeitritt/-erstellung: **80 %**

**Qualitative Beobachtungen:**
- Die Registrierung wurde als **klar und einfach** wahrgenommen
- Zwei Nutzer waren unsicher, ob sie einer Gruppe beitreten oder eine neue erstellen sollen
- Die Bedeutung des Gruppenpassworts war nicht sofort ersichtlich
- Die Navigation innerhalb der Gruppe wurde überwiegend positiv bewertet

### Implications

Aus der Evaluation wurden folgende Erkenntnisse gewonnen:

- Der grundlegende Onboarding-Prozess funktioniert zuverlässig
- Nutzer benötigen jedoch **mehr Orientierung** im Gruppenbereich

Geplante Verbesserungen:
- Klarere Beschriftung und kurze Hinweise bei:
  - Gruppenbeitritt
  - Gruppenerstellung
- Ergänzung erklärender Texte im Guide-Bereich
- Visuelle Hervorhebung zentraler Aktionen (z. B. „Gruppe erstellen“)

Nach Umsetzung dieser Anpassungen soll die Evaluation erneut durchgeführt werden,  
um die Auswirkungen auf Verständlichkeit und Nutzerfluss zu überprüfen.

---

## 02: Group & Overlay Interface Usage

### Meta

Status
: **Work in progress** – **Done** – Obsolete

Updated
: 28-Jan-2026

### Goal

Ziel dieser Evaluation war es zu überprüfen,  
**wie intuitiv und konsistent das Gruppen-Interface sowie das Overlay genutzt werden können**, insbesondere im Hinblick auf typische Anwendungsszenarien wie Stream-Overlays oder Gruppenverwaltung.

Der Fokus lag auf folgenden Fragestellungen:
- Ist der aktuelle Gruppenstatus (aktiv, erledigt, ausstehend) klar ersichtlich?
- Sind zentrale Aktionen schnell auffindbar?
- Eignet sich das Overlay für den Einsatz in einem Stream-Kontext?

### Method

Die Evaluation wurde als **interne Selbst-Evaluation** durchgeführt.

- **Ansatz:** Heuristic Evaluation & Explorative Nutzung
- **Durchführende:** Projektteam
- **Umgebung:**  
  - Desktop-Browser  
  - Lokale Entwicklungsumgebung  
  - Vorhandene Beispiel- und Testdaten  

Getestete Szenarien:
1. Navigation innerhalb einer bestehenden Gruppe
2. Hinzufügen, Aktivieren und Abschließen von Challenges
3. Wechsel zwischen Gruppen-Interface und Overlay
4. Nutzung des Overlays als eigenständige Ansicht (z. B. für Streaming)
5. Bewertung der Informationsdichte und Lesbarkeit

Die Bewertung erfolgte anhand eigener Beobachtungen und wiederholter Nutzung.

### Results

**Positive Beobachtungen:**
- Der Status von Challenges (aktiv, queued, done) ist klar strukturiert
- Das Overlay stellt die wichtigsten Informationen reduziert und übersichtlich dar
- Fortschrittsanzeige vermittelt schnell einen Überblick über den aktuellen Stand
- Trennung zwischen Verwaltungsansicht (Gruppe) und Präsentationsansicht (Overlay) ist sinnvoll

**Identifizierte Schwächen:**
- Einige Aktionen im Gruppen-Interface sind funktional korrekt, aber nicht sofort selbsterklärend
- Die Reihenfolge von queued Challenges ist nicht auf den ersten Blick nachvollziehbar
- Das Overlay bietet bewusst keine Interaktionsmöglichkeiten, was erklärungsbedürftig sein kann

### Implications

Aus der Selbst-Evaluation ergeben sich folgende Maßnahmen:

- Ergänzung kurzer erklärender Texte oder Tooltips im Gruppen-Interface
- Visuelle Hervorhebung besonders häufiger Aktionen (z. B. „Challenge aktiv setzen“)
- Klarere Kommunikation der Rolle des Overlays als **Read-only Ansicht**

Die aktuelle Umsetzung erfüllt die Anforderungen des MVP und eignet sich für den vorgesehenen Einsatzzweck.  
Weitere Verbesserungen können bei zukünftigen Iterationen erfolgen, insbesondere im Rahmen von UI-Polishing und optionaler Client-Side-Interaktivität.

---