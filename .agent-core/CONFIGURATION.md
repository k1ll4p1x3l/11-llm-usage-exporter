# Konfiguration und spätere Verwendung

Stand: 2026-11-19; Quellen zu Sol/Astra 6.2, Terra 6.1, Skills und T3: 2026-11-19;
historische Modell- und Speedquellen: 2026-09-22/2026-10-16;
Quellenzugriff zu Erweiterungen: 2026-09-16, sonst 2026-09-12.
Gewünschte Einstellung, dokumentierte Fähigkeit und tatsächlich beobachtetes
Verhalten sind verschiedene Aussagen.
Hier liegen Definitionen vor; Konto-/Oberflächenverfügbarkeit bleibt unbekannt.

## Quellen und Dateien

`orchestration/roles/*.json` pflegt Rolle, Alias, Aufgabe und Modellklassen;
`orchestration/registry.v1.json` pflegt Modelle, Efforts, Speedmodus und Profile.
Die nativen Dateien sowie [Rollenübersicht](ROLES.md) werden daraus erzeugt.
Keine automatische Routingengine oder Modellersatzkette. Die Klassen nennen
nur ausdrücklich wählbare Optionen; Mehrfachzuordnungen erzeugen keine Dubletten.
Mit #99 verwenden die acht Economy-Basisrollen weiterhin GPT-6 Luna High;
elf Balanced-Rollen verwenden GPT-6.2 Sol Medium und drei Balanced-Deep- sowie
sechs Deep-Rollen GPT-6.2 Sol High. Balanced-Deep und Deep bleiben fachlich
getrennte Klassen. Das sind bewusste
Repository-Vorgaben nach Aufgabe und Risiko, keine Herstellerdefaults oder
gemessenen Effizienzgewinne. `sol`/`luna` bezeichnen weiterhin GPT-5.6;
`sol_6`/`luna_6` bleiben GPT-6, `sol_6_1` bezeichnet GPT-6.1 Sol.
`sol_6_2`, `astra_6_2` und `terra_6_1` sind neue generationseindeutige Schlüssel;
`astra` und `terra` behalten ihre bisherigen Modell-IDs.
Bestehende qualifizierte Dateinamen behalten ihr Modell-/Effortpaar;
frühere Basisdefaults bleiben als ausdrücklich benannte Varianten erreichbar.
Die aktuellen Terra- und Astra-Optionen ergänzen die historischen Varianten.
Die [Modellauswahl](https://learn.chatgpt.com/docs/model-selection) nennt Sol 6.2
für normale Arbeit und Astra 6.2 für komplexe Projekte; die konkrete
Rollenverteilung ist eine Repositoryentscheidung. API-Modellseiten und ein
einzelner T3-Katalog beweisen keine Verfügbarkeit in jedem Client/Konto.
Die verfügbaren Modell-/Effortpaare stehen nur in
der Registry; Effortnamen sind zwischen Generationen nicht gleichwertig.

Die normalen und komplexen Parent-Profile sowie Qualitäts- und Reviewoptionen
stehen in `profiles/`. Projektrollen stehen im Lieferziel `.codex/agents/`;
`.codex/config.toml` enthält ihre Registrierungen und vorsichtige Rechtevorgaben,
aber keinen globalen Parent-Modellpin. Die acht möglichen Child-Threads sind
nur eine Obergrenze, keine Pflicht zur Delegation oder belegte verfügbare Kapazität.
`coordinator_standard` verwendet Sol 6.2 Medium; `coordinator_deep` und
`review_deep` verwenden Sol 6.2 High. Die ausdrückliche Astra-6.2-High-Reviewoption
ergänzt die bisherige Astra-Option. `quality_build` bevorzugt Astra 6.2 Max und
bietet zusätzlich Sol 6.2 Max sowie die bisherigen Astra-/Sol-Max-Varianten.
Ein Astra-Parent ändert
die ausdrücklich gepinnten Child-Modelle nicht automatisch.

Für die Consumer ist seit der Nutzerentscheidung vom 2026-09-17
ausschließlich Variante 2 maßgeblich: alle 28 Basisrollen binden Modell und
Effort ausdrücklich; `max_concurrent_threads_per_session = 8` ist die native
Projektobergrenze. Die frühere Zusage von Modellvererbung und Grenze 4 ist
abgelöst. Consumer-eigene Dokumentation und Orchestrierungsrichtlinien müssen
dazu passen. Engere tatsächlich wirksame Plattformgrenzen und auftragsbezogene
Budgets bleiben verbindlich; die Definition verleiht keine zusätzliche Kapazität.

## Geltung und Priorität

Nach der [Konfigurationsdokumentation](https://learn.chatgpt.com/docs/config-file/config-basic)
gelten CLI-Overrides vor vertrauenswürdiger Projektkonfiguration, danach das
gewählte Benutzerprofil, Benutzerkonfiguration, Cloud-/Systemdefaults und
Built-ins. Native erzwungene Richtlinien sind davon getrennt und bleiben wirksam.
Ein Skill kann keinen Desktop-Picker korrigieren.

[Profile](https://learn.chatgpt.com/docs/config-file/config-advanced) sind seit
Codex 0.134.0 separate `<profil>.config.toml`-Dateien im Codex-Benutzerverzeichnis;
`--profile <profil>` wählt sie aus. Die hier gelieferten Dateien sind Beispiele
im Repository, keine aktivierte Benutzerinstallation. Eine spätere bewusste
Übernahme in die Benutzerebene liegt beim Nutzer; vorhandene Konfiguration und
explizite Auswahl nicht überschreiben. Alte `[profiles.name]`-Tabellen entfallen.

Bei [Custom Agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
gewinnt ein Modell-/Effortwert in der Agentendatei vor dem zuvor aus Spawnwert,
`agents`-Default und Parent ermittelten Wert. Deshalb pinnt jede gewählte
Rollenvariante Modell und Effort zusammen. Für eine abweichende ausdrückliche
Wahl eine passende Variante auswählen; keinen stillen Override behaupten.
`name`, `description` und `developer_instructions` sind erforderlich.
Live-Rechte des Parents werden erneut angewendet: eine read-only-Vorgabe im
Rollenfile ist deshalb keine alleinige Sicherheitsgarantie.

## T3 Code und delegierte Aufgaben

Quellcodeabgleich: T3 v0.1.10, Revision
`7d32075e3757ded707914e2450c3e392a9665765`, gelesen am 2026-11-19.
Die folgenden Regeln beschreiben diese Schnittstelle; bei anderen Versionen
gelten die tatsächlich angebotenen Werkzeuge und wirksamen Anweisungen.
Es wurde keine lokale Provider-/Agentenausführung geprüft.

### Den angebotenen Delegationsweg verwenden

Die [T3-Orchestrierungsanweisungen](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/packages/provider-core/src/server/orchestrationInstructions.ts)
sehen native Subagenten vor, wenn Provider, angebotenes Modell und Einstellungen
dazu passen. Für andere Provider, ausdrücklich gewünschte Einstellungen,
getrennte Worktrees, Hintergrundaufträge oder ausdrücklich verlangte T3-Delegation
verwenden sie `delegate_task`. Keine native Fähigkeit erzwingen oder einen
gesperrten Weg über CLI, zusätzliche Threads oder andere Konten ersetzen.
Bei nativer Auswahl die angebotene Rollen-ID als `agent_type` verwenden;
die Rollenvariante bestimmt Modell und Effort.

Für T3 vor dem ersten `delegate_task` im Thread `orchestrator_capabilities`
lesen, erneut nur nach Fehler oder ausdrücklich geändertem Provider. Eine
kurze Modellauswahl ist kein vollständiger Katalog; bei Bedarf die angebotene
Modellsuche verwenden. Instanz-ID und unterstützte Optionen aus diesem
Ergebnis nehmen. Ein nicht angebotenes Modell nicht ungefragt ersetzen.

### Die gewählte Codex-Rolle ausdrücklich übertragen

Die generierte [Basistabelle](ROLES.md#basisrollen-für-native-auswahl-und-t3)
zeigt die Defaults; für eine Variante deren `.codex/agents/<name>.toml` lesen.
Die [T3-Schnittstelle](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/packages/contracts/src/orchestratorMcp.ts)
hat keinen `agent_type`-/`config_file`-Parameter. Das generische `role` ersetzt
keine native Rolle. Die Zuordnung folgt diesen Quellen:

| T3-Feld / Auftragsinhalt | Verbindliche Herkunft |
| --- | --- |
| `target.providerInstanceId` | Gewählte verfügbare Instanz aus den Fähigkeiten; keine Host-ID im Standard hinterlegen |
| `target.model` | `model` der gewählten nativen Rollendatei |
| `target.options.reasoningEffort` | `model_reasoning_effort` derselben Datei, sofern für dieses Modell angeboten |
| `target.options.serviceTier` | Standard-Speed: `default`, sofern angeboten; ausdrückliche andere Nutzerwahl erhalten |
| `role` | Passende T3-Kategorie: `general`, `implementation`, `research`, `review`, `design` oder `test`; keine Essentials-Rollen-ID |
| `task` | Vollständige `developer_instructions` der Rolle plus konkreter Auftrag, Muss-Punkte, Dateien/Quellenstand, nötiger Kontext, Skills, Freigaben, Schreibzuständigkeit und Ergebnisformat |
| `isolation` | Bewusst gewähltes gemeinsames Checkout oder von T3 erzeugter Worktree |

Der [T3-Server](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/apps/server/src/mcp/OrchestratorMcpService.ts)
übernimmt ohne `target.model` bei derselben Instanz das Parent-Modell; bei einer
anderen Instanz kann er das erste angebotene Modell wählen. Optionen werden
nur bei gleicher Instanz und gleichem Modell vererbt, einzelne Angaben ergänzen
oder überschreiben sie; ein leeres Optionsobjekt löscht sie. Modell und Effort
deshalb beide setzen. Allein der Wechsel des Modells überträgt den gewünschten
Effort nicht. Fehlende/unzulässige Werte offenlegen, keine stillen Fallbacks.

Der [Codex-Adapter](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts)
verwendet `reasoningEffort` und `serviceTier`. TOML-`service_tier = "fast"`
nicht als T3-Wert kopieren; ein gewünschter anderer Speed braucht die tatsächlich
angebotene T3-Option. Sonstige geerbte Optionen nicht als geprüft oder geändert
darstellen. Kein automatisches Fast, Ultrafast, Ultra oder Daybreak.

### Kontext, Skills und Checkout

Laut [T3-Orchestrierungsdokumentation](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/docs/orchestration-v2/orchestrator-mcp-server.md)
erhält das Child den übergebenen Auftrag und eine optionale Rollenanweisung,
aber keine kopierte Parent-Historie. Deshalb den fachlichen Auftrag einschließlich
vorhandener Freigaben selbstständig verständlich formulieren. Passende Skills
mit ihrem im Zielprojekt zugänglichen Pfad nennen und gezielt lesen lassen;
eine bloße Nennung ist kein Nachweis erfolgreicher Aktivierung.

Codex [führt gleichnamige Skills nicht zusammen](https://learn.chatgpt.com/docs/build-skills).
Bei identischen globalen und projektbezogenen Kopien im Consumer die passende
Projektquelle eindeutig per Pfad verwenden, sofern keine ausdrückliche andere
Auswahl gilt. Bei abweichendem Inhalt Herkunft und Stand klären. Globale Kopien
nicht ungefragt löschen, deaktivieren oder mit Projektwissen überschreiben.
Ein global installierter Skill löst die oben genannten Projektpfade gegen das
aktive Projekt auf. Ein T3-Worktree benötigt die dort vorhandenen Projektdateien;
nicht auf absolute Parent- oder Installationspfade vertrauen.

`shared` verwendet das Parent-Checkout: Zuständigkeiten dürfen sich beim
Schreiben nicht überschneiden. `worktree` lässt T3 ein separates Checkout
aus dem Parent-Commit erzeugen; uncommittete Änderungen bleiben außen vor.
Abhängige Arbeit braucht den tatsächlichen benötigten Stand. Child-Worktrees
nicht im Shellauftrag anlegen. Ein Integrator prüft die Ergebnisse; keine
weitere Delegation im Child ohne Auftrag. Dem zurückgegebenen `next` folgen,
statt laufende Delegationen durch Polling oder neue Threads zu begleiten.

### Provider, Rechte und Ergebnis unterscheiden

Die [Providerdokumentation](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/docs/user/providers-codex.md)
unterscheidet verwaltete ChatGPT-Verbindungen und manuell konfigurierte
Codex-Instanzen. Eine CLI-Anmeldung wechselt nicht automatisch eine verwaltete
Verbindung. Bei einer gezielten späteren Betriebsprüfung die im Thread gewählte
Instanz, deren tatsächliche Binary/Version, `CODEX_HOME`/gegebenenfalls Shadow-Home,
Projektpfad und Launch-Overrides abgleichen. T3-Serverversion, Shell-`codex`
und eine zufällig sichtbare Sandboxversion sind keine austauschbaren Belege.
Launch-Argumente gelten für danach gestartete Sitzungen. Keine automatischen
Provider-, Login- oder Hoständerungen aus diesen Definitionsdateien ableiten.

Der [verwaltete T3-Startpfad](https://github.com/pingdotgg/t3code/blob/7d32075e3757ded707914e2450c3e392a9665765/apps/server/src/provider/CodexManagedRuntime.ts)
setzt in dieser Version beide nativen Multi-Agent-Flags auf `false`; daraus
folgt keine allgemeine Deaktivierung in jeder T3-Instanz. Der Codex-Adapter
übergibt je nach Runtime-Modus ausdrückliche Approval-/Sandboxwerte an den
App-Server. Projekt-TOMLs und textliche Rollenregeln beweisen daher nicht allein
die effektiv wirksamen Rechte. Eine T3-Reviewkategorie ist keine eigene Sandbox;
der Auftrag erweitert weder Berechtigungen noch Nutzerfreigaben.

Bei der Ergebnisprüfung angeforderte Rolle, Modell und Effort festhalten und
mit der vorhandenen Rückmeldung vergleichen. `model` bezeichnet die Auswahl;
das optionale `executedModel` ist eine Providermeldung zur Ausführung und kann
abweichen oder fehlen. Fehlende Evidenz bleibt unbekannt. Die Modellselbstauskunft
des Childs ist kein technischer Nachweis. Diese Definitionen verbessern die
Anweisungen und Nachvollziehbarkeit, erzwingen aber keine T3-seitige Rollenladung.

## Benutzerweite Erweiterungen und Aktionsfreigaben

Bereits installierte, verbundene und unterstützte Plugins, Apps und Skills
werden über die nativen Benutzereinstellungen verwaltet. Für neue Chats oder
Worktrees verlangt diese Definitionsquelle kein zusätzliches Tool-Inventar und
keine erneute Kopie der Pluginregistrierung. Wenn SSH, Terminal und eine manuelle
T3-Instanz denselben Benutzerstand verwenden sollen, ihr wirksames `CODEX_HOME`
gezielt abgleichen; bewusst getrennte Instanzen getrennt lassen. Projektregeln und die
oben beschriebene Konfigurationspriorität bleiben wirksam.

Installation und sichtbarer Werkzeugkatalog sind keine Handlungsfreigabe.
Die gelieferte Projektbasis behält `workspace-write`, `on-request` und bei Apps
`writes`; destruktive und Open-World-Werkzeuge sind zunächst gesperrt. Sie
setzt keinen pauschalen `approvals_reviewer`-Wert. Ohne irgendeinen wirksamen
Reviewer-Override greift der versionsbezogene Built-in-Default. Vorhandene
Host- und höher priorisierte Overrides können anders entscheiden; bewusst
gesetzte projektspezifische Einschränkungen bleiben möglich. Das Entfernen
des Felds konfiguriert daher nicht alle Hosts gleich. Einen ausdrücklich
genehmigten Hoststandard nur in dessen Benutzerkonfiguration setzen und die
wirksame Konfiguration dort prüfen.

Die [native Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference)
unterscheidet App-Aktivierung, Werkzeugfreigabe und Reviewer. Bei ausdrücklich
genehmigten Apps können `destructive_enabled` und `open_world_enabled` gezielt
aktiviert werden. Werkzeugkatalog und Reviewer sind getrennte Einstellungen:
Verfügbarkeit erteilt keine einzelne Aktionsfreigabe. App- und
Werkzeugoverrides sowie die für eine konkrete Aktion wirksame native Prüfung
mitprüfen.

[MCP-Richtlinien](https://learn.chatgpt.com/docs/extend/mcp) gehören für eigene
Server unter `mcp_servers.<server>`, für Pluginserver unter
`plugins.<plugin>.mcp_servers.<server>`. Plugintransporte nicht doppelt anlegen.
`default_tools_approval_mode = "writes"` fragt für nicht als read-only markierte
Werkzeuge; bei unklarer Klassifikation oder besonders sensiblen Aktionen
`prompt` ausdrücklich setzen. Vorhandene native Werkzeuglisten und
projektspezifische Einschränkungen erhalten. Frühere Zusatzinventare erst nach
Zuordnung ihrer Regeln ablösen; unklare Einschränkungen nicht still verwerfen.

Die zuständige Betriebsumgebung prüft bei einer Umstellung tatsächliche
Leseaufrufe sowie Ablehnung und fehlenden Freigabekanal mit einem unschädlichen
Schreibtest. Das gilt auch für direkte Aufrufe und Code Mode, falls verwendet.
Diese Sourceprüfung führt selbst keine Agentenprobe aus.
[Hooks](https://learn.chatgpt.com/docs/hooks) ersetzen native Freigaben nicht:
`PreToolUse` mit `permissionDecision = "ask"` ist laut aktuellem Dokumentationsstand
nicht unterstützt; der Hookfehler hält den Werkzeugaufruf nicht zuverlässig auf.

## Headless-Betrieb und Verfügbarkeitsgrenzen

Für einen Headless-Host ohne nutzbaren Schlüsselbund ist
`mcp_oauth_credentials_store = "file"` eine unterstützte explizite Benutzeroption
([Referenz](https://learn.chatgpt.com/docs/config-file/config-reference)).
Den Anmeldespeicher nur für den Betriebsbenutzer zugänglich halten.
Credentials, OAuth-Zustand, Plugininstallation und Cache gehören nicht in den
Consumer-Dateisync; die Betriebsumgebung verwaltet sie separat.

Nach [Plugininstallation](https://learn.chatgpt.com/docs/plugins) eine neue
CLI-Sitzung starten; eine externe Verbindung kann zusätzlich erforderlich sein.
Die IDE-Erweiterung unterstützt Plugins derzeit nicht. Codex CLI im
IDE-Terminal bleibt eine eigene Oberfläche. Plattformgebundene Plugins und
Desktopfunktionen sind kein zugesicherter Umfang eines Linux-Hosts.
Eine widerrufene Verbindung kann erneute Anmeldung verlangen.

Abweichungen konkret benennen: verfügbar, bewusst eingeschränkt, Verbindung
erforderlich, auf dieser Plattform nicht unterstützt oder Anbieterfehler.
Ein geladener Katalog oder erfolgreicher Diagnosecheck allein beweist keine
Nutzbarkeit und keine wirksame Aktionsfreigabe.

## Start und Fortsetzung im Consumer

1. Ziel, Scope, lokale Projektregeln und aktuellen Aufgabenstand lesen.
2. Explizite Profil-/Modellwahl erhalten. Ohne solche Wahl ein zur Aufgabe
   passendes Profil aus der Rollenübersicht vorschlagen oder im freigegebenen
   Umfang wählen. Modell, Reasoning-Effort und Speed sind getrennte Einstellungen.
3. Nur tatsächlich verfügbare Hinweise über die Sitzung verwenden; Unbekanntes
   offen nennen. Keine Pflicht zu Quotenexporter, Kontoabfrage oder Modellprobe.
4. Fehlende oder inkompatible Wahl: nur eine bereits erlaubte passende Option
   nutzen, sonst die konkrete Einschränkung melden. Keine Quoten-/Safetyumgehung
   und kein bezahlter API-Fallback.
5. Bei Resume Ziel, Commit/Dateien, offene Punkte und bestehende Freigaben
   abgleichen. Ein neuer Thread setzt Problemversuche oder Budget nicht zurück.

## Kompatibilitätsgrenzen

Das am 2026-09-17 erneut gelesene aktuelle
[Config-Schema](https://learn.chatgpt.com/docs/config-schema.json) definiert
`enabled`, `interrupt_message` und `max_concurrent_threads_per_session` als
skalare Eigenschaften von `AgentsToml`; Rollen bleiben zusätzliche Tabellen.
Die [Referenz](https://learn.chatgpt.com/docs/config-file/config-reference)
bestätigt diese Platzierung unter `agents`. Hinweise älterer Consumer-Beispiele
zu Codex 0.137/0.144 sind keine Vorgabe für diese aktuelle Konfiguration.
Eine ältere CLI, die diese Felder als Rollen interpretiert, ist damit inkompatibel;
eine aktuelle passende Version verwenden. Es wird keine getestete Mindestversion
oder lokale Agentenausführung behauptet.

Das [Config-Schema](https://learn.chatgpt.com/docs/config-schema.json) akzeptiert
vom Modell angebotene nichtleere Effortstrings. Die offiziellen Modellseiten
führen `max` für die vorhandenen Qualitätsoptionen auf; die allgemeine
[Config-Referenz](https://learn.chatgpt.com/docs/config-file/config-reference)
listet teils nur Werte bis `xhigh`. Hier bleiben die anhand Modellseite und
Schema belegten Qualitätsoptionen erhalten. Daraus folgt keine Garantie, dass
jede ältere CLI oder Oberfläche diese Auswahl anbietet.

`service_tier` wird aus dem gewählten Speedmodus erzeugt. Die Parent-
Profildateien behalten `service_tier = "default"` für Standard-Speed.
Nach der aktuellen [Subagentenreferenz](https://learn.chatgpt.com/docs/agent-configuration/subagents)
folgt der Service-Tier der Root-Sitzung. Die vorhandenen generierten
Child-Einträge `service_tier = "default"` erzwingen deshalb keinen unabhängigen
Standardmodus gegen einen Fast-Parent und sind keine Sicherheits- oder
Kostengarantie. Für Standard-Speed die Root-Sitzung entsprechend wählen.
Die Registry hält für einen *nicht aktiven*
Fastmodus den nativen Codex-Konfigurationswert `service_tier = "fast"` und
getrennt den Requestwert `priority` fest; letzterer ist kein direkt in TOML
einzutragender Speedwert. Die tatsächliche Verfügbarkeit und Aktivierung hängen
von Client, Modell und Konto ab. API-Tokenpreise, zusätzliche ChatGPT-Credits
und inkludierter Abonnementverbrauch sind verschiedene Größen; aus der
Modellwahl folgt keine feste Ersparnis oder Nachrichtenmenge.
`execution_mode` und `ultra` sind beschreibende
Registry-Metadaten, keine erfundenen nativen Schalter. Der Profilwert `max`
aktiviert weder Fast noch Ultra; zusätzlich angebotene UI-/Moduswerte nicht
ungeprüft in native Effortwerte übersetzen. Fast, Ultrafast und Ultra werden durch
diese Definitionen nicht aktiviert.
Der frühere Spark-Kandidat wurde nach seiner Einstellung aus aktiven
Auswahlpfaden entfernt. Bisherige dokumentierte 5.6- und GPT-6-Alternativen bleiben
ausdrücklich wählbar, solange der jeweilige Client sie bereitstellt.
