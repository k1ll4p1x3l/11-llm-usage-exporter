---
name: budget-aware-orchestration
description: Use for large, expensive, or multi-agent tasks where token usage, fan-out, and checkpoint timing need explicit control.
---

# Ressourcenbewusst arbeiten

- Wähle Modell und Rolle passend zu Schwierigkeit und Risiko. Nutze für einfache
  Aufgaben eine geeignete sparsame Option, ohne die erforderliche Qualität zu
  senken. Explizite Nutzerwahl beachten; das Bearbeitermodell ist kein globaler Pin.
- Nutze gezielte Suchen, vorhandene Dateizuordnungen und aktuelle Kurzstände.
  Prüfungen nur nach relevanter Änderung, echtem Fehler oder offener Frage wiederholen.
- Kleine Aufgaben lokal erledigen. Delegation nur bei konkretem Nutzen und
  erlaubter Fähigkeit; wenige disjunkte Teilaufträge, ein Git-Integrator, klare
  Ergebnisse. Keine rekursive Delegation ohne passenden Auftrag.
- Native Parallelitätsgrenzen und vereinbarte Budgets sind Obergrenzen, keine
  Auslastungsziele. Unbekannte Kapazität nicht als freie Kapazität ausgeben.
- Tatsächlich bereitgestellte Verbrauchs- und Quotenhinweise nutzen. Fehlende
  Werte bleiben unbekannt; eine erlaubte Text-/Dateiaufgabe erfordert deshalb
  keinen Exporter oder Messdienst. Historische Zahlen sind kein aktuelles Guthaben.
- API-Preisproxy, Abonnementverbrauch und zusätzliche Zahlung unterscheiden.
  Keine erfundenen Prozentwerte oder garantierten Einsparungen. Neue kostenpflichtige
  Wege und gewünschte Modellwechsel brauchen passende Autorisierung.
- Kontingentsperren nicht durch Konten, APIs, Threads oder Modelle umgehen.
  Vorhandene Plattforminformationen und echte Nutzergrenzen bleiben maßgeblich.
- Begrenze ergebnislose Problemloops anhand der vereinbarten kumulativen Grenzen
  und erwarteter Erkenntnis. Umbenennung oder Wiederaufnahme setzt nichts zurück.
  Ohne neue Evidenz keine weitere Review-/Hypothesenkampagne.
- Nach Muss-Erfüllung und erlaubtem Abschluss beenden. Ressourcenbewusstsein
  rechtfertigt weder eine still verkleinerte Aufgabe noch zusätzliche Infrastruktur.
