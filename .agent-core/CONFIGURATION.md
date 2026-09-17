# Konfiguration und spätere Verwendung

Stand: 2026-09-17; Quellenzugriff zu Erweiterungen: 2026-09-16, sonst 2026-09-12.
Gewünschte Einstellung, dokumentierte Fähigkeit und tatsächlich beobachtetes
Verhalten sind verschiedene Aussagen.
Hier liegen Definitionen vor; Konto-/Oberflächenverfügbarkeit bleibt unbekannt.

## Quellen und Dateien

`orchestration/roles/*.json` pflegt Rolle, Alias, Aufgabe und Modellklassen;
`orchestration/registry.v1.json` pflegt Modelle, Efforts, Speedmodus und Profile.
Die nativen Dateien sowie [Rollenübersicht](ROLES.md) werden daraus erzeugt.
Keine automatische Routingengine oder Modellersatzkette. Die Klassen nennen
nur ausdrücklich wählbare Optionen; Mehrfachzuordnungen erzeugen keine Dubletten.

Die normalen und komplexen Parent-Profile sowie Qualitäts- und Reviewoptionen
stehen in `profiles/`. Projektrollen stehen im Lieferziel `.codex/agents/`;
`.codex/config.toml` enthält ihre Registrierungen und vorsichtige Rechtevorgaben,
aber keinen globalen Parent-Modellpin. Die acht möglichen Child-Threads sind
nur eine Obergrenze, keine Pflicht zur Delegation oder belegte verfügbare Kapazität.

Für alle acht Empfänger ist seit der Nutzerentscheidung vom 2026-09-17
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

## Benutzerweite Erweiterungen und Aktionsfreigaben

Bereits installierte, verbundene und unterstützte Plugins, Apps und Skills
werden über die nativen Benutzereinstellungen verwaltet. Für neue Chats oder
Worktrees verlangt diese Definitionsquelle kein zusätzliches Tool-Inventar und
keine erneute Kopie der Pluginregistrierung. SSH, Terminal und App-Server sollen
für denselben Benutzer dasselbe `CODEX_HOME` verwenden. Projektregeln und die
oben beschriebene Konfigurationspriorität bleiben wirksam.

Installation und sichtbarer Werkzeugkatalog sind keine Handlungsfreigabe.
Die gelieferte Projektbasis behält `workspace-write`, `on-request`, Reviewer
`user` und bei Apps `writes`; destruktive und Open-World-Werkzeuge sind zunächst
gesperrt. Ein ausdrücklich genehmigter Hoststandard gehört in die
Benutzerkonfiguration. Er darf nicht ungefragt zum allgemeinen Consumerdefault
werden. Ob konkrete Projekt- oder Werkzeugregeln ihn übersteuern, muss die
zuständige Umgebung anhand der wirksamen Konfiguration prüfen.

Die [native Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference)
unterscheidet App-Aktivierung, Werkzeugfreigabe und Reviewer. Bei ausdrücklich
genehmigten Apps können `destructive_enabled` und `open_world_enabled` gezielt
aktiviert werden; benötigte menschliche Aktionsfreigaben weiterhin mit Reviewer
`user` vorsehen. App- und Werkzeugoverrides mitprüfen.

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

`service_tier` wird aus dem gewählten Speedmodus erzeugt. Der Standard fordert
keinen Priority-/Fastmodus an. `execution_mode` und `ultra` sind beschreibende
Registry-Metadaten, keine erfundenen nativen Schalter; höchste Reasoningqualität
ist nicht automatisch Fast oder ein gesonderter Ausführungsmodus.
Der bisherige Spark-Kandidat bleibt wegen unbelegter Effortkompatibilität ohne
native Ausgabe. Seine ausdrücklich definierten Alternativen bleiben wählbar.
