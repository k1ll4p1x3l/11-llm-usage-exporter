# Varianten und Parentprofile

Generiert aus `orchestration/`. Jede Variante gehört zu einer
[Basisrolle](ROLES.md) und bindet ihr eigenes Modell und ihren Effort.
Die konkrete Verfügbarkeit hängt vom Client und vom Konto ab.

## Rollenvarianten

### code_heavy_worker

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_heavy_worker__astra_6_2_high](../.codex/agents/code_heavy_worker__astra_6_2_high.toml) | `gpt-6.2-astra` | `high` | Komplexer Umbau mit mehreren gekoppelten Schnittstellen und schwer prüfbaren Zustandsübergängen. |

### code_mapper

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_mapper__terra_6_1_medium](../.codex/agents/code_mapper__terra_6_1_medium.toml) | `gpt-6.1-terra` | `medium` | Bildschirmbefund mit zugänglichem Screenshot zu Komponenten und Einstiegspunkten zuordnen. |

### code_medium_worker

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_medium_worker__sol_6_2_high](../.codex/agents/code_medium_worker__sol_6_2_high.toml) | `gpt-6.2-sol` | `high` | Begrenzte Änderung mit verzahnten Zuständen oder anspruchsvoller Regressionseingrenzung. |

### code_review_gate

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_review_gate__astra_6_2_high](../.codex/agents/code_review_gate__astra_6_2_high.toml) | `gpt-6.2-astra` | `high` | Folgenreicher Review über mehrere Komponenten mit schwer überprüfbaren Invarianten. |

### code_simple_worker

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_simple_worker__terra_6_1_medium](../.codex/agents/code_simple_worker__terra_6_1_medium.toml) | `gpt-6.1-terra` | `medium` | Eng begrenzte UI-Korrektur anhand eines verfügbaren Bildbefunds und eines überprüfbaren Sollzustands. |

### code_test_triage

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [code_test_triage__sol_6_2_high](../.codex/agents/code_test_triage__sol_6_2_high.toml) | `gpt-6.2-sol` | `high` | Mehrere plausible Ursachen anhand widersprüchlicher Tests oder verteilter Stacktraces abgrenzen. |

### homelab_critical_planner

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [homelab_critical_planner__astra_6_2_high](../.codex/agents/homelab_critical_planner__astra_6_2_high.toml) | `gpt-6.2-astra` | `high` | Wechselwirkungen kritischer Infrastruktur und unabhängige Recovery-Pfade bei dicht gekoppelten Diensten bewerten. |

### writing_editor

| Variante | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [writing_editor__terra_6_1_high](../.codex/agents/writing_editor__terra_6_1_high.toml) | `gpt-6.1-terra` | `high` | Anspruchsvollere Redaktion mit besonderem Augenmerk auf natürlichen Stil und den Ton der Vorlage. |

## Inaktive Parentprofile

Die Dateien sind feste Beispiele für eine ausdrücklich gewählte Sitzung.

| Profil | Modell | Effort | Einsatz |
| --- | --- | --- | --- |
| [coordinator_deep](profiles/coordinator_deep.config.toml) | `gpt-6.2-sol` | `high` | Koordination mehrerer beteiligter Komponenten mit anspruchsvoller Ursachenanalyse. |
| [coordinator_standard](profiles/coordinator_standard.config.toml) | `gpt-6.2-sol` | `medium` | Normale Koordination mit klar begrenzten Abhängigkeiten. |
| [quality_build](profiles/quality_build.config.toml) | `gpt-6.2-astra` | `max` | Ausdrücklich gewählte höchste Qualitätsstufe für einen komplexen, schwer überprüfbaren Bauauftrag. |
| [review_deep](profiles/review_deep.config.toml) | `gpt-6.2-sol` | `high` | Vertiefte Prüfung von Anforderungen, Nachweisen und Risiken. |
