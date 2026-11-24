# Basisrollen

Generiert aus `orchestration/`. Wähle eine im Client angebotene Rollen-ID.
Die TOML enthält Modellbindung und vollständige Instruktionen.
Weitere Auswahl im [Varianten- und Profilkatalog](VARIANTS.md).

| Rolle / Nickname | Zweck | Modell | Effort | Varianten |
| --- | --- | --- | --- | --- |
| [automation_planner](../.codex/agents/automation_planner.toml) / Bulma | Plant CI/CD und Automation read-only mit Idempotenz, Guardrails und Rollback. | `gpt-6.2-sol` | `high` | — |
| [ci_cd_worker](../.codex/agents/ci_cd_worker.toml) / Vegeta | Implementiert GitHub Actions, lokale Skripte und CI/CD im zugewiesenen Scope. | `gpt-6.2-sol` | `medium` | — |
| [code_heavy_worker](../.codex/agents/code_heavy_worker.toml) / Broly | Bearbeitet komplexe Logik, Refactorings und Migrationen im zugewiesenen Scope. | `gpt-6.2-sol` | `high` | [Varianten](VARIANTS.md#code_heavy_worker) |
| [code_mapper](../.codex/agents/code_mapper.toml) / Trunks | Erkundet Codebase, Einstiegspunkte, Tests, Abhaengigkeiten und Risiken read-only. | `gpt-6-luna` | `high` | [Varianten](VARIANTS.md#code_mapper) |
| [code_medium_worker](../.codex/agents/code_medium_worker.toml) / Gohan | Implementiert normale Features und Bugfixes im zugewiesenen Scope. | `gpt-6.2-sol` | `medium` | [Varianten](VARIANTS.md#code_medium_worker) |
| [code_review_gate](../.codex/agents/code_review_gate.toml) / Piccolo | Prüft Änderungen lesend auf Soll-Erfüllung, Korrektheit, Regressionen, Sicherheit und fehlende Nachweise. | `gpt-6.2-sol` | `high` | [Varianten](VARIANTS.md#code_review_gate) |
| [code_simple_worker](../.codex/agents/code_simple_worker.toml) / Goten | Implementiert kleine, klar begrenzte Code- oder Textaenderungen mit Tests. | `gpt-6-luna` | `high` | [Varianten](VARIANTS.md#code_simple_worker) |
| [code_test_triage](../.codex/agents/code_test_triage.toml) / Android 17 | Analysiert Testfehler, Logs und Stacktraces read-only. | `gpt-6.2-sol` | `medium` | [Varianten](VARIANTS.md#code_test_triage) |
| [data_analyst](../.codex/agents/data_analyst.toml) / Buu | Erstellt reproduzierbare Datenanalysen, Skripte, Tabellen und Visualisierungen. | `gpt-6.2-sol` | `medium` | — |
| [data_quality_auditor](../.codex/agents/data_quality_auditor.toml) / Android 18 | Prueft strukturierte Daten read-only auf Qualitaet, Plausibilitaet und Leakage. | `gpt-6.2-sol` | `medium` | — |
| [decision_analyst](../.codex/agents/decision_analyst.toml) / Whis | Vergleicht Optionen, Kriterien, Trade-offs und Risiken read-only. | `gpt-6.2-sol` | `high` | — |
| [docs_writer](../.codex/agents/docs_writer.toml) / Pan | Pflegt README, Changelog, Nutzerdoku und knappe technische Erklaerungen. | `gpt-6-luna` | `high` | — |
| [homelab_critical_patch_author](../.codex/agents/homelab_critical_patch_author.toml) / Jiren | Bereitet kritische Homelab-Patches im Repo vor, wendet sie aber nicht live an. | `gpt-6.2-sol` | `high` | — |
| [homelab_critical_planner](../.codex/agents/homelab_critical_planner.toml) / Beerus | Plant kritische Firewall-, DNS-, IAM-, Storage- und Backup-Aenderungen read-only. | `gpt-6.2-sol` | `high` | [Varianten](VARIANTS.md#homelab_critical_planner) |
| [homelab_inventory](../.codex/agents/homelab_inventory.toml) / Tien | Erfasst Hardware, Dienste, Netzwerk, Storage und Backups read-only. | `gpt-6-luna` | `high` | — |
| [homelab_light_worker](../.codex/agents/homelab_light_worker.toml) / Krillin | Bearbeitet risikoarme Homelab-Doku, Templates und Hilfsskripte. | `gpt-6-luna` | `high` | — |
| [homelab_log_triage](../.codex/agents/homelab_log_triage.toml) / Chiaotzu | Ordnet Homelab-Logs und Servicefehler read-only ein. | `gpt-6.2-sol` | `medium` | — |
| [homelab_security_reviewer](../.codex/agents/homelab_security_reviewer.toml) / Android 16 | Prüft Homelab-Konfigurationen lesend auf Exposition, Secrets, Betriebsrisiken und Wiederherstellbarkeit. | `gpt-6.2-sol` | `high` | — |
| [homelab_service_worker](../.codex/agents/homelab_service_worker.toml) / Goku | Bearbeitet Compose, Ansible, Monitoring und lokale Automation. Führt ausdrücklich zugewiesene und gedeckte Livearbeit aus. | `gpt-6.2-sol` | `medium` | — |
| [long_context_summarizer](../.codex/agents/long_context_summarizer.toml) / Roshi | Pflegt Checkpoints, Task-Logs und Resume-Plaene fuer lange Laeufe. | `gpt-6-luna` | `high` | — |
| [project_planner](../.codex/agents/project_planner.toml) / Shenron | Plant Meilensteine, Abhaengigkeiten, Reviewpunkte und risikoarme Reihenfolge. | `gpt-6.2-sol` | `high` | — |
| [repo_bootstrapper](../.codex/agents/repo_bootstrapper.toml) / Cabba | Erstellt eine sichere, generische Arbeitsbasis fuer neue oder unklare Repositories. | `gpt-6.2-sol` | `medium` | — |
| [requirements_analyst](../.codex/agents/requirements_analyst.toml) / Videl | Klaert Ziel, Scope, Annahmen, Akzeptanzkriterien und gebuendelte Rueckfragen. | `gpt-6.2-sol` | `medium` | — |
| [research_mapper](../.codex/agents/research_mapper.toml) / Yamcha | Plant Suchstrategie, Primaerquellen und Evidenzpfade read-only. | `gpt-6-luna` | `high` | — |
| [security_secret_scanner](../.codex/agents/security_secret_scanner.toml) / Cell | Prueft read-only auf Secrets, riskante Defaults und versehentliche Exposition. | `gpt-6.2-sol` | `high` | — |
| [source_reliability_reviewer](../.codex/agents/source_reliability_reviewer.toml) / Frieza | Bewertet Quellen read-only nach Autoritaet, Aktualitaet und Widerspruechen. | `gpt-6.2-sol` | `medium` | — |
| [writing_architect](../.codex/agents/writing_architect.toml) / Caulifla | Plant Outline, Argumentationsbogen und Konsistenz langer Texte read-only. | `gpt-6.2-sol` | `medium` | — |
| [writing_editor](../.codex/agents/writing_editor.toml) / Kale | Bearbeitet Abschnitte und Langtexte im zugewiesenen Scope. | `gpt-6-luna` | `high` | [Varianten](VARIANTS.md#writing_editor) |
