---
name: budget-aware-orchestration
description: Use when selecting roles and models for native Codex subagents or T3 delegated tasks, or when a large task needs explicit control of context, fan-out, and resource use.
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

## Rolle vor Delegation binden

1. Lies im aktiven Consumer-Projekt `.agent-core/ROLES.md` und die gewählte Datei
   `.codex/agents/<rolle-oder-variante>.toml`. Nutze deren `model`,
   `model_reasoning_effort` und vollständige `developer_instructions`; die
   Instruktionen enthalten bereits Abnahmeregeln und Toolpolitik. Eine
   ausdrücklich gewählte Variante hat eigene Werte. Fehlt diese Quelle, melde
   die konkrete Lücke; erfinde keine Standardmatrix. Globale Skills lösen
   Projektpfade gegen das aktuelle Projekt, nicht gegen ihr Installationsverzeichnis.
2. Verwende den nach den wirksamen Provider-/T3-Anweisungen zulässigen Weg.
   Wenn native Subagenten angeboten und passend sind, wähle die konkrete
   registrierte Rolle als `agent_type`. T3 v0.1.10 verlangt `delegate_task`
   unter anderem für andere Provider, ausdrücklich gewünschte Einstellungen,
   eigene Worktrees und Hintergrundaufträge. Erzwinge keinen nativen Umweg.
3. Bei T3 lies `orchestrator_capabilities` vor der ersten Delegation im Thread;
   erneut nur nach Fehler oder ausdrücklich geändertem Provider. Prüfe Modell
   und Optionen für die konkrete Instanz; suche bei Bedarf im angebotenen
   Modellkatalog weiter. Setze `target.providerInstanceId`, `target.model` und
   Codex-`target.options.reasoningEffort` ausdrücklich. Verwende die Modell-/
   Effortwerte der gewählten Rolle und die Options-IDs der aktuellen Fähigkeiten.
   Standard-Speed ist die Vorgabe; sofern angeboten, setze T3-`serviceTier`
   auf `default`, außer bei ausdrücklicher anderer Nutzerwahl. Eine fehlende
   Option nicht erfinden oder als wirksam behaupten. Native Child-Tiers folgen
   der Root-Sitzung; Codex-`fast` ist kein T3-Optionswert.
4. Wähle T3s generisches `role` nur als Kategorie. Übergib in `task` die
   vollständigen Rolleninstruktionen, den konkreten Auftrag, Muss-Punkte,
   Quellenstand/Dateipfade, erforderlichen Kontext, Freigabegrenzen,
   Schreibzuständigkeit und erwartetes Ergebnis. Nenne passende Skills mit
   eindeutigem Pfad und verlange ihr gezieltes Lesen. T3 kopiert keine
   Parent-Historie und lädt über `role` keine native Rollendatei. Bei gleichnamigen
   Skills die tatsächlich gewählte Quelle benennen; doppelte Installation
   weder zusammenführen noch ungefragt löschen.
5. Wähle `shared` nur bei kompatiblen Zuständigkeiten im Parent-Checkout;
   beauftrage getrennte Checkouts mit T3-`isolation: "worktree"`. T3 erzeugt sie
   aus dem Parent-Commit ohne uncommittete Änderungen; abhängige Arbeit muss
   den benötigten Stand tatsächlich vorfinden. Keine Child-Worktrees per Shell
   anlegen. Folge dem zurückgegebenen `next`, starte keine Polling-Schleife und
   erlaube dem Child keine weitere Delegation ohne entsprechenden Auftrag.
6. Lies Ergebnis, Diff und offene Grenzen. Halte Rollen-ID, angeforderte
   Modell-/Effortwahl und das vom Provider gemeldete `executedModel` auseinander;
   fehlt letzteres, bleibt die tatsächliche Ausführung unbekannt. Kein stiller
   Parent-Fallback oder eigenmächtiger Providerwechsel. Behebe kleine Befunde
   selbst, statt dafür eine weitere Delegationsrunde zu eröffnen.

Die Definitionen sind Anweisungen, keine technische Rechte- oder Modellgarantie.
`role: "review"` und eine read-only-Vorgabe in der Datei setzen nicht allein die
effektive Sandbox. Prüfe nur die auftragsrelevanten wirksamen Grenzen. Details
und versionsgebundene Quellen stehen im Consumer unter
`.agent-core/CONFIGURATION.md`, Abschnitt „T3 Code und delegierte Aufgaben“.
