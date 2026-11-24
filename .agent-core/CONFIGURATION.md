# Konfiguration und spätere Verwendung

Quellenstand 23.11.2026. Der Produktvergleich bezieht sich auf Codex 0.171.0
und T3 Stable v0.1.11, Commit `59651c1761f6c63e9b6056839067066968e6a406`.
Die tatsächlich laufende Host-/Clientkonfiguration ist gesondert zu prüfen.

## Quellen und Dateien

Im Autorenrepository liegen Rolle, Alias, Aufgabe und konkrete Variantenwahl
unter `orchestration/roles/`. Die Registry enthält den Modellkatalog und die
festen Parentprofile. Die kurze [Rollenübersicht](ROLES.md) führt zur jeweiligen
nativen Definition und zur Begründung der angebotenen Auswahl.

Die Lieferung enthält 28 fachliche Basisrollen und gezielte Varianten in
`.codex/agents/`. Die Projektbasis `.codex/config.toml` hält die aktiven
Registrierungen und die nativen Child-Einstellungen, einschließlich der
Projektobergrenze von acht parallelen Children. Verwende nur die für die
Aufgabe erforderliche Parallelität innerhalb der tatsächlichen Limits.

Die Parentprofile in `profiles/` sind inaktive Beispiele. Für eine bewusst
gewählte Benutzerkonfiguration unterstützt Codex separate Dateien
`<profil>.config.toml` im Codex-Benutzerverzeichnis und die Auswahl mit
`--profile`. Die Projektbasis setzt keinen Parent-Modellpin.
[Codex-Profile](https://learn.chatgpt.com/docs/config-file/config-advanced)

## Geltung und Priorität

CLI-Overrides haben Vorrang vor vertrauenswürdiger Projektkonfiguration,
danach folgen gewähltes Benutzerprofil, Benutzerkonfiguration und Defaults.
Erzwungene native Richtlinien bleiben wirksam.
[Konfigurationspriorität](https://learn.chatgpt.com/docs/config-file/config-basic)

Codex berücksichtigt die Werte `model` und `model_reasoning_effort` der
gewählten Agentendatei nach der Auswahl aus Spawnwert, `agents`-Default und
Parent. Der Pin in der Datei hat Vorrang. Verwende für eine abweichende Wahl
eine passende angebotene Variante. `name`, `description` und
`developer_instructions` beschreiben die native Rolle. Childdateien binden
Modell und Effort. Die Root-Sitzung bestimmt die wirksamen nativen Grenzen
und den Service-Tier der Children.
[Subagentenreferenz](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## T3 Code und delegierte Aufgaben

Der Skill `budget-aware-orchestration` führt den operativen Ablauf. Die
T3-`role`-Kategorien laden keine Codex-Rollendateien. `delegate_task` übernimmt
keine Parent-Historie und erstellt die Child-Nachricht mit leeren Attachments.
Freigaben, benötigte Quellen und zugängliche Bilder müssen im Teilauftrag
konkret zugeordnet sein. Ein Child-Worktree beginnt am Parent-Commit.
[MCP-Vertrag](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/packages/contracts/src/orchestratorMcp.ts),
[Delegationsserver](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/mcp/OrchestratorMcpService.ts),
[Orchestrierungsanweisungen](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/packages/provider-core/src/server/orchestrationInstructions.ts)

Fehlt `target.model`, kann die gleiche Instanz die Parentauswahl übernehmen,
eine andere Instanz eine eigene Vorgabe. Optionen werden abhängig von
Instanz und Modell geerbt oder überschrieben. Ein explizit leeres Optionsobjekt
löscht sie. Beim nächsten Turn werden ausgewählte Werte nach den tatsächlich
unterstützten Update-Regeln angewandt. Beim Nutzer-Steering reicht T3 die
Pickerwahl an den Adapter weiter. Der Payload von `turn/steer` enthält die
Eingabe und die Ziel-IDs, aber keine Modell- oder Effortwerte. Im unterstützten
manuellen Codex-Pfad kann der Adapter zuvor einen gesetzten Service-Tier per
`thread/settings/update` übermitteln. Schlägt das Update fehl, protokolliert
der Adapter eine Warnung und setzt das Steering fort. Pickerwahl, bestätigte
Übermittlung und tatsächliche Anwendung auf einen Request sind getrennt zu
belegen. Daraus folgt keine rückwirkende Änderung bearbeiteter Requests oder
ihrer Kosten. Custom Models und angebotene allgemeine
Optionswerte sind Auswahlhinweise. Prüfe bei konkretem Bedarf die tatsächliche
Providerantwort und beobachtete Ausführung getrennt.
[Delegationsserver](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/mcp/OrchestratorMcpService.ts),
[Nutzer-Steering](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Orchestrator.ts#L6522-L6565),
[Manualadapter](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/provider/Drivers/CodexDriver.ts#L243-L258),
[Tier-Update](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts#L7931-L7957),
[Steering-Aufruf](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts#L8245-L8263),
[Composer](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/composer.md)

### Providerpfad und Rechte

Managed- und Manual-Instanzen können unterschiedliche Binaries, Benutzerstände
und Startparameter nutzen. Prüfe bei einem konkreten Betriebsproblem die im
Thread gewählte Instanz, deren tatsächlich gestartete Binary und Version,
`CODEX_HOME` beziehungsweise Shadow-Home, den Projektpfad und die
Launch-Overrides. Shell-`codex`, GUI-Updateanzeige und T3-Serverversion
belegen diese Angaben einzeln nicht. Änderungen am Providerstart gelten
für entsprechend neu gestartete Sitzungen.
[Codex-Provider](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/providers-codex.md)

Im geprüften verwalteten Startpfad setzt T3 beide nativen Multi-Agent-Flags
auf `false`. Je nach Runtime-Modus gibt der Adapter ausdrückliche
Approval-/Sandboxwerte an den App-Server weiter. Prüfe den angebotenen Weg
und effektive Rechte der konkreten Instanz. Mandat, native Approval- und
Sandboxgrenzen sowie tatsächliche Dienstrechte gelten unabhängig voneinander.
`never` erweitert keine Sandbox. Eine Sitzungserlaubnis begründet kein
dauerhaftes Mandat. Stimmen Laufzeit-Overrides und Permission Profiles nicht
nachweislich zusammen, erzwinge ihre Kombination nicht. Native Auto-Reviews
und technische Ablehnungen bleiben wirksam.
[Verwalteter Startpfad](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/provider/CodexManagedRuntime.ts),
[Codex-Adapter](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts)

### Modell, Tempo und Verbrauch

Standardtempo bleibt die Ausgangseinstellung. `service_tier = "default"`
in den Parentbeispielen konfiguriert die Root-Sitzung, sofern das Profil
bewusst gewählt wird. Codex-TOML `fast` entspricht dem Request-/T3-
Optionswert `priority`. Setze abweichendes Tempo nur bei ausdrücklicher
Auswahl und tatsächlicher Verfügbarkeit. `max` bezeichnet einen
modellabhängigen Effort. Beschreibungen von Ausführungsmodi ergeben
keine zusätzlichen nativen Schalter.
[Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference),
[Codex-Adapter](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts)

Angeforderte Auswahl, optionales `executedModel` aus der Providerantwort
und nachgewiesene Anwendung sind getrennte Angaben. T3s Codex-Turnwert
`usageScope: main_agent` ist auf den Hauptagenten bezogen. `hasSubagents`
kennzeichnet die Beteiligung weiterer Agenten. Für die Usage-Ansicht
zählt die tatsächlich verfügbare Historie. API-äquivalente Schätzung,
zusätzliche Zahlung und Abonnementverbrauch sind unterschiedliche Größen.
Ohne geeignete Daten bleibt der Gesamtverbrauch unbekannt.
[Turnverbrauch](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/provider/CodexTurnTokenUsage.ts#L136-L170),
[Usage](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/usage.md)

### Native Goals und Wiederaufnahme

`/goal <Zieltext>` setzt in einer unterstützten Codex-Konstellation ein Ziel,
`/goal` zeigt seinen Status. Codex unterstützt `/goal pause`, `/goal resume`
und `/goal clear`. Der geprüfte Slash-Pfad begrenzt Ziele auf 4.000
Unicode-Zeichen, behandelt eine Nachricht mit Anhängen als gewöhnlichen
Prompt und übermittelt kein frei gewähltes Tokenbudget. Umfangreiche
Spezifikationen oder Bilder vorher zugänglich machen und im separaten
knappen Goal auf die maßgeblichen Quellen verweisen. Der native Schemaweg
kennt Budgetdaten. Ein Plan-Goal bleibt im Plan-Modus. Wenn keine weitere
native Fortsetzung erfolgt, kann ein offenes Ziel pausieren. Prüfe den
tatsächlichen Status und die verfügbare Oberfläche.
[Composer](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/composer.md#goals),
[Codex-Adapter](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/orchestration-v2/Adapters/CodexAdapterV2.ts),
[Codex-Goals](https://learn.chatgpt.com/use-cases/follow-goals)

| Mechanismus | Reichweite im verglichenen Stand |
| --- | --- |
| Continue threads after restarts | Standardmäßig ein. Erfordert den erneut gestarteten Hostserver und passende Provider-Resume-Daten. Wartende Freigaben, Antworten oder Secrets und archivierte, gesnoozte oder settled Threads können die Fortsetzung verhindern. Nach drei aufeinanderfolgenden Crash-Recoveries desselben offenen Turns ist eine Nachricht nötig. Ein beendeter Turn oder geplanter Shutdown setzt den Zähler zurück. |
| Resume nach Usage-Limit | Option standardmäßig aus. Benötigt einen geeigneten vom Provider gemeldeten Reset und einen verfügbaren Server. Die native Quote bleibt wirksam. |
| Clientdisconnect | Ein geschlossener Remote-Client lässt den Hostserver separat bestehen. Für Serverbetrieb außerhalb des Clients gibt es den nativen Hintergrunddienst. |
| `/compact` | Unterstützte Kontextreduktion. Wichtige Entscheidungen gehören in den verfügbaren aktuellen Aufgabenstand. |
| Restart agent session | Die nächste Nachricht startet die Providersitzung mit dem vorgesehenen Setup im fortgesetzten Gespräch. Prüfe bei Bedarf die tatsächlich wirksamen Einstellungen. |
| `/clear` | Neuer Providerkontext. In der GUI verbleibende historische Nachrichten sind dem neuen Providerkontext nicht automatisch bekannt. |
| Children und Hintergrundarbeit | Nach Abbruch tatsächliche Zustände prüfen. T3-verwaltete Delegation und native Child-/Shellprozesse folgen ihrem jeweiligen Lebenszyklus. |
| Timeouts | Grenzen für Setup, Toolwartezeit, Inaktivität oder Retry beziehen sich auf den jeweiligen Vorgang. |

Vor erneuter Mutation tatsächliche Effekte und laufende Arbeit nachlesen.
Die Wiederaufnahme folgt `long-running-goal` und dem
[aktuellen Aufgabenstand](templates/HANDOFF.md).
[Restart-Recovery](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/updating.md#before-you-update),
[Usage](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/usage.md),
[Hintergrunddienst](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/background-service.md),
[Composer](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/composer.md)

### Lokaler Hauptstand und native Bereinigung

`Automatically pull` aktualisiert optional geeignete saubere
Default-Checkouts per Fast-forward vom konfigurierten Upstream. Abweichende
Branches, ungetrackte oder geänderte Dateien und unabhängige Commits werden
übersprungen. Prüfe den vereinbarten lokalen Hauptstand nach der Integration.
[Projekteinstellungen](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/project-settings.md#keep-the-default-branch-current)

Der native `t3_thread_organize`-Aufruf mit Aktion `settle` kann für den
eigenen laufenden Thread `settlesWhenTurnEnds` melden. Das bildet die
Vormerkung ab. Die optionale automatische Bereinigung ist standardmäßig
aus und erfasst bekannte T3-verwaltete Worktrees. Aktive Sessions, Terminals,
geteilte Kontexte und andere Guards können die Entfernung verzögern.
Trigger umfassen Start, Policyänderung und stündliche Sweeps. Null Tage
Retentionsdauer bedeutet den nächsten zulässigen Sweep. Prüfe auch
benötigte ignorierte Inhalte wie `.env` vor Freigabe. Branches und
Threadhistorie bleiben erhalten, ebenso nicht zugeordnete Orphanverzeichnisse.
[Toolvertrag](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/mcp/toolkits/thread/tools.ts#L33-L55),
[Cleanupguards](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/storageCleanup.ts#L1277-L1428),
[Entfernung](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/storageCleanup.ts#L1630-L1642),
[Projekteinstellungen](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/project-settings.md)

Der Bericht unter Settings → Worktrees → Cleanup → Last run ist flüchtig,
begrenzt und wird beim nächsten Lauf ersetzt. Für verifizierten
Löschvollzug prüft ein vorhandener externer Kontext den tatsächlichen
Bestand. Vor Turnende kann der aktive Thread den eingerichteten Nachlauf
veranlassen und seine offene Verifikation benennen. `runOnSettle` und
`stopOnSettle` betreffen zugeordnete Projektaktionen. Eigenständige
Remote-Dateien, Prozesse, Branches und Sicherungen bleiben beim
Aufgabenabschluss einzeln zu prüfen. Ein gesettelter oder archivierter
Thread bezeichnet einen Threadzustand.
[Cleanupbericht und Trigger](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/server/src/storageCleanup.ts#L1907-L2027),
[Last-run-Anzeige](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/apps/web/src/components/settings/StorageSettings.tsx#L509-L558),
[Settle und Projektaktionen](https://github.com/pingdotgg/t3code/blob/59651c1761f6c63e9b6056839067066968e6a406/docs/user/thread-sidebar.md)

## Benutzerweite Erweiterungen und Aktionsfreigaben

Bereits installierte und verbundene Erweiterungen bleiben in der nativen
Benutzerkonfiguration. Untersuche Probleme am konkret wirksamen Pfad.
Codex führt gleichnamige Skills getrennt. Nutze die einschlägige Quelle
explizit und erhalte unabhängige lokale oder globale Kopien.
[Skills](https://learn.chatgpt.com/docs/build-skills)

Die Projektbasis setzt `workspace-write` und `on-request`. App-Writes
fordern standardmäßig Freigabe. Open-World- und destruktive App-Werkzeuge
sind in der Basis gesperrt. Ein wirksamer Reviewer ergibt sich aus der
Host-/Projektpriorität oder dem versionsbezogenen Built-in-Default.
Prüfe für eine konkrete Aktion native App- und Tooloverrides und die
geltende Nutzerfreigabe. `mcp_servers.<server>` gilt für eigene Server,
`plugins.<plugin>.mcp_servers.<server>` für Pluginserver. Prüfe den
wirksamen Ort und verwende bei unklarer Klassifikation oder besonders
sensibler Aktion die erforderliche native Prüfung.
[Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference),
[MCP](https://learn.chatgpt.com/docs/extend/mcp)

Eine beauftragte spätere Betriebsprüfung kann anhand unschädlicher
Aktionen lesen, Ablehnung und fehlende Freigabekanäle verifizieren.
Beim Hook `PreToolUse` ist `permissionDecision = "ask"` in der
referenzierten Dokumentation nicht unterstützt. Die nativen Gates
und das [Nutzermandat](templates/REPO_POLICY.md) bleiben maßgeblich.
[Hooks](https://learn.chatgpt.com/docs/hooks)

## Headless-Betrieb und Verfügbarkeitsgrenzen

Auf Hosts ohne nutzbaren Schlüsselbund ist
`mcp_oauth_credentials_store = "file"` eine explizite Benutzeroption.
Schütze den Speicher für den Betriebsbenutzer und trenne Credentials,
OAuth-Zustand, Installation und Cache vom Dateitransport.
[Konfigurationsreferenz](https://learn.chatgpt.com/docs/config-file/config-reference)

Nach einer autorisierten Plugininstallation unterstützt Codex eine neu
gestartete CLI-Sitzung. Abhängig vom Plugin ist eine externe Verbindung nötig.
Die Verfügbarkeit hängt von Oberfläche, Host und Provider ab. Melde konkrete
Einschränkungen und nutze nur bereits erlaubte verfügbare Optionen.
[Plugins](https://learn.chatgpt.com/docs/plugins)

## Start und Fortsetzung im Consumer

Lies Auftrag, lokale Regeln und aktuellen Stand. Erhalte explizite
Modell-, Effort- und Tempowahlen. Nutze nur tatsächlich sichtbare
Sitzungsinformationen. Wende bei Fortsetzung `long-running-goal` an.
Offene Wirkungen und laufende Arbeit müssen vor Wiederholung nachgelesen werden.

## Kompatibilitätsgrenzen

Das native Schema führt `enabled`, `interrupt_message` und
`max_concurrent_threads_per_session` als skalare Felder unter `agents`.
Rollenregistrierungen stehen in separaten Tabellen. Eine ältere CLI, die
solche Felder als Rollen interpretiert, braucht einen passenden neueren
Codex-Stand. Effortstrings sind modellbezogen. Verwende für `max` das
konkret angebotene, dokumentierte Modellpaar und die tatsächliche
Providerunterstützung.
[Konfigurationsschema](https://learn.chatgpt.com/docs/config-schema.json),
[Referenz](https://learn.chatgpt.com/docs/config-file/config-reference)
