---
name: long-running-goal
description: Use when work should proceed in milestones with durable checkpoints, resumable state, and explicit done criteria.
---

# Längere Aufgaben fortsetzen und abschließen

- Ein Ziel, klare Muss-Punkte, Ausschlüsse und vereinbarter Endpunkt bleiben
  über Unterbrechungen erhalten. Dauer ist kein Selbstzweck.
- Nutze wenige überprüfbare Meilensteine. Der Aufgabenstand nennt Ziel,
  erledigt/offen, Dateien/Commit, tatsächliche Prüfungen und Freigaben,
  kumulative Versuche, wichtige eigene temporäre Ressourcen und nächsten
  sicheren Schritt. Nutze bei Bedarf die vorhandene HANDOFF-Vorlage.
- Nach einem Meilenstein und vor einer absehbaren Unterbrechung kurz aktualisieren.
  Eine normale Markdownnotiz genügt; kein Store, Zustandsautomat oder Dienst.
- Bei Fortsetzung zuerst aktuellen Stand lesen. Prüfe Git, Dateien, externe
  Wirkungen und laufende Arbeit einschließlich Children. Wiederhole bestätigte
  Mutationen nicht blind. Prüfe geänderte Eingaben erneut. Lade Historie
  gezielt für offene Fragen nach. Der Hauptagent hält jüngste Nutzerkorrekturen
  und Freigaben fest. Ein Summarizer verwendet die ihm zugänglichen Quellen.
- Notizen, Toolbeobachtungen, Nutzeraussagen und Schlussfolgerungen unterscheiden.
  Keine erfolgreiche Ausführung aus einer vom Agenten geschriebenen Notiz ableiten.
- Wiederholungen über Hypothesen, Threads und Bearbeiter hinweg zählen. Vorher
  vereinbarte Problem-/Gesamtgrenzen respektieren; ohne erwartbaren Erkenntnisgewinn
  einen Loop beenden und die konkrete Grenze nennen. Keine erfundenen Budgets.
- Kurzer Chatstatus zur vollen Stunde in Europe/Berlin am nächsten sicheren
  Gesprächspunkt nach `autonomous-run`; keine
  garantierte zeitgesteuerte Zustellung. Nur echte Entscheidungen erfordern Antwort.
- Schließe nach den Consumer-AGENTS und bei Git-Arbeit nach
  `git-change-lifecycle` ab.

## Native Goals

Nutze für einen passenden Ergebnisauftrag nur den tatsächlich angebotenen
und autorisierten nativen Goal-Weg. Der Skill beschreibt das Verfahren.
Verbinde das Goal mit überprüfbaren Muss-Punkten und zugänglichen Quellen.
Führe Plan-/Ausführungsmodus, native Berechtigungen, Nutzerautorisierung
und Goalstatus getrennt. Je nach Provider und Unterbrechung kann die native
Fortsetzung ausbleiben. Pause, Blockade, Budget-/Usage-Grenze und erreichtes
Ziel haben unterschiedliche Folgen. Technisch erzwungene Budgets nur bei
belegter nativer Übermittlung melden. Die T3-spezifische Zeichen- und
Anhangsbehandlung sowie Resume-Grenzen stehen in
`.agent-core/CONFIGURATION.md` des aktiven Consumer-Projekts.
