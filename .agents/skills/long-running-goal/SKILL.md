---
name: long-running-goal
description: Use when work should proceed in milestones with durable checkpoints, resumable state, and explicit done criteria.
---

# Längere Aufgaben fortsetzen und abschließen

- Ein Ziel, klare Muss-Punkte, Ausschlüsse und vereinbarter Endpunkt bleiben
  über Unterbrechungen erhalten. Dauer ist kein Selbstzweck.
- Nutze wenige überprüfbare Meilensteine. Der Aufgabenstand nennt Ziel,
  erledigt/offen, Dateien/Commit, relevante Befunde, tatsächliche Freigaben,
  Problemhistorie mit kumulativen Versuchen und nächsten sicheren Schritt.
- Nach einem Meilenstein und vor einer absehbaren Unterbrechung kurz aktualisieren.
  Eine normale Markdownnotiz genügt; kein Store, Zustandsautomat oder Dienst.
- Bei Fortsetzung zuerst aktuellen Stand lesen, Git/Dateien und notwendige
  externe Fakten frisch prüfen. Historie nur für eine konkrete offene Frage
  nachladen. Geänderte relevante Eingaben entwerten die zugehörige alte Prüfung.
- Notizen, Toolbeobachtungen, Nutzeraussagen und Schlussfolgerungen unterscheiden.
  Keine erfolgreiche Ausführung aus einer vom Agenten geschriebenen Notiz ableiten.
- Wiederholungen über Hypothesen, Threads und Bearbeiter hinweg zählen. Vorher
  vereinbarte Problem-/Gesamtgrenzen respektieren; ohne erwartbaren Erkenntnisgewinn
  einen Loop beenden und die konkrete Grenze nennen. Keine erfundenen Budgets.
- Kurzer Chatstatus zur vollen Stunde in Europe/Berlin am nächsten sicheren
  Gesprächspunkt nach `autonomous-run`; keine
  garantierte zeitgesteuerte Zustellung. Nur echte Entscheidungen erfordern Antwort.
- Muss-Punkte und erlaubten Abschluss gegen aktuelle Evidenz prüfen. Optionale
  Verbesserungen werden keine neuen Muss-Punkte. Bei Zielerfüllung aufhören;
  Zwischenstand, erschöpftes Budget und Blockade sind keine erfolgreiche Abnahme.
