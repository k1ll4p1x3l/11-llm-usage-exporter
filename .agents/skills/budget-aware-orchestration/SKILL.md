---
name: budget-aware-orchestration
description: Use when selecting roles and models for native Codex subagents or T3 delegated tasks, or when a large task needs explicit control of context, fan-out, and resource use.
---

# Ressourcenbewusst arbeiten

- Wähle Rolle, Modell und Effort nach Fachaufgabe, Schwierigkeit und Risiko.
  Berücksichtige Ergebnisqualität, Nacharbeit, Koordination, Nutzerunterbrechungen
  und verfügbare Verbrauchsdaten. Erhalte die explizite Nutzerwahl. Leite aus
  langer Laufzeit keinen hohen Effort oder Anlass zum Tempowechsel ab.
- Nutze gezielte Suchen, vorhandene Dateizuordnungen und aktuelle Kurzstände.
  Prüfungen nur nach relevanter Änderung, echtem Fehler oder offener Frage wiederholen.
- Kleine Aufgaben lokal erledigen. Delegation nur bei konkretem Nutzen und
  erlaubter Fähigkeit; wenige disjunkte Teilaufträge, ein Git-Integrator, klare
  Ergebnisse. Keine rekursive Delegation ohne passenden Auftrag.
- Native Parallelitätsgrenzen und vereinbarte Budgets sind Obergrenzen, keine
  Auslastungsziele. Unbekannte Kapazität nicht als freie Kapazität ausgeben.
- Nutze die tatsächlich bereitgestellten Verbrauchs- und Quotenhinweise. T3s
  Codex-Turnwert mit `usageScope: main_agent` umfasst nicht automatisch die
  Descendants. Fehlende Werte bleiben unbekannt. Historische Zahlen belegen
  kein aktuelles Guthaben und kleinere Definitionsdateien keine Einsparung.
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
   registrierte Rolle als `agent_type`. T3 Stable v0.1.11 verlangt `delegate_task`
   unter anderem für andere Provider, ausdrücklich gewünschte Einstellungen,
   eigene Worktrees, Hintergrundaufträge oder ausdrücklich verlangte
   T3-Delegation. Es gelten die aktiven Provideranweisungen.
3. Bei T3 lies `orchestrator_capabilities` vor der ersten Delegation im Thread;
   erneut nur nach Fehler oder ausdrücklich geändertem Provider. Prüfe Modell
   und Optionen für die konkrete Instanz; suche bei Bedarf im angebotenen
   Modellkatalog weiter. Setze `target.providerInstanceId`, `target.model` und
   Codex-`target.options.reasoningEffort` ausdrücklich. Verwende die Modell-/
   Effortwerte der gewählten Rolle und die Options-IDs der aktuellen Fähigkeiten.
   Setze für Standardtempo, sofern angeboten, `target.options.serviceTier`
   auf `default`. Erhalte eine ausdrückliche andere Nutzerwahl anhand der
   angebotenen Werte. Codex-TOML `fast` entspricht dem Request-/T3-Weg
   `priority`. Native Child-Tiers folgen der Root-Sitzung.
4. Wähle T3s generisches `role` nur als Kategorie. Übergib in `task` die
   vollständigen Rolleninstruktionen, den konkreten Auftrag, Muss-Punkte,
   Quellenstand/Dateipfade, erforderlichen Kontext, Freigabegrenzen,
   Schreibzuständigkeit und erwartetes Ergebnis. Nenne passende Skills mit
   eindeutigem Pfad und verlange ihr gezieltes Lesen. T3 kopiert keine
   Parent-Historie und lädt über `role` keine native Rollendatei. Bei gleichnamigen
   Skills die tatsächlich gewählte Quelle benennen. Für Bildprüfung das
   konkrete Bild auf einem erlaubten und im Child erreichbaren Pfad
   bereitstellen. Im geprüften T3-Pfad bleiben Attachments leer. Das Child
   öffnet das Bild selbst und meldet fehlenden Zugriff als Prüfgrenze.
5. Wähle `shared` nur bei kompatiblen Zuständigkeiten im Parent-Checkout;
   beauftrage getrennte Checkouts mit T3-`isolation: "worktree"`. T3 erzeugt sie
   aus dem Parent-Commit ohne uncommittete Änderungen; abhängige Arbeit muss
   den benötigten Stand tatsächlich vorfinden. Keine Child-Worktrees per Shell
   anlegen. Folge dem zurückgegebenen `next`, starte keine Polling-Schleife und
   erlaube dem Child keine weitere Delegation ohne entsprechenden Auftrag.
6. Prüfe bei Steering oder Resume die tatsächlich wirksame Provider-, Modell-
   und Optionsauswahl anhand der angebotenen Update-Regeln. Ein sichtbares
   Custom Model oder Optionsfeld belegt allein keine Unterstützung.
7. Lies Ergebnis, Diff und offene Grenzen. Halte Rollen-ID, angeforderte
   Modell-/Effortwahl und das vom Provider gemeldete `executedModel` auseinander;
   behaupte ohne technische Evidenz keine tatsächliche Modellanwendung.
   Die Selbstauskunft eines Childs genügt dafür nicht. Ein fehlendes Modell
   oder ein inkompatibler Effort braucht eine konkrete Meldung. Behebe kleine Befunde
   selbst, statt dafür eine weitere Delegationsrunde zu eröffnen.

Die Definitionen sind Anweisungen, keine technische Rechte- oder Modellgarantie.
`role: "review"` und eine read-only-Vorgabe in der Datei setzen nicht allein die
effektive Sandbox. Prüfe nur die auftragsrelevanten wirksamen Grenzen. Details
und versionsgebundene Quellen stehen im Consumer unter
`.agent-core/CONFIGURATION.md`, Abschnitt „T3 Code und delegierte Aufgaben“.
