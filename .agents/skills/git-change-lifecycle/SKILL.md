---
name: git-change-lifecycle
description: Use for any repository-writing task and for branch creation, milestone commits, pushes, pull requests, review fixes, merge readiness, merges, or branch/worktree cleanup so each change stays isolated, recoverable, reviewable, and bounded by the correct human gates.
---

# Git-Änderungen und Abschluss

1. Vor Schreibarbeit Repository, aktuellen Branch, Default-Branch, Worktrees,
   lokalen Diff und gegebenenfalls Upstream lesen. Bei unbekannter Topologie
   oder unabhängigen Änderungen zuerst klären. Read-only braucht keinen Branch.
2. Für eine unabhängige Änderung einen geeigneten Topic-Branch im autorisierten
   Worktree nutzen. Eine Fortsetzung behält den vorhandenen Task-/PR-Branch.
   Implementiere weder auf Default-/geschützten Branches noch im Detached HEAD.
   Der gedeckte abschließende Fast-forward des bezeichneten lokalen
   Hauptcheckouts folgt Schritt 9.
3. Kleine zusammenhängende Änderungen nach passenden Repo-Prüfungen committen.
   Explizite Pfade stagen; keine fremden Änderungen, Secrets oder wissentlich
   defekten Zwischenstände einschließen. Lokale Implementierungsfreigabe deckt
   notwendige Task-Branches und lokale Commits, sofern nicht ausgeschlossen.
4. Ein reiner Analyse-/Reviewauftrag bleibt read-only. Ein konkreter
   Implementierungsauftrag umfasst ohne engeren Nutzerendpunkt den normalen
   Push des eigenen Topic-Branches und einen prüfbereiten Draft-PR. Ein
   menschliches Aufgaben- oder Bereichsmandat kann auch den regulären Merge
   und die Bereinigung eigener integrierter Arbeitsressourcen umfassen.
   Prüfe für jede Wirkung Ziel, Umfang und Grenzen des Mandats. Bei Deckung
   gelten die nachfolgenden Prüfungen ohne erneute Einzelzustimmung. Eine
   ungedeckte Wirkung erfordert eine konkrete Entscheidung.
5. Vor Push Ziel und vollständigen Diff prüfen. Kein Force-Push oder direkter
   Default-Branch-Push. Erste PR bevorzugt als Draft; Ziel, Head und Ergebnis
   nachlesen. Beschreibungen erklären Problem, Änderung, Prüfung und Grenzen.
6. Vor Merge PR-Identität, aktuellen Head, Base, vollständigen Diff, Checks,
   vorgeschriebene Reviews, offene Threads und Mergefähigkeit frisch lesen.
   Ein ausdrücklich autorisierter Merge ist auch nach einem Draft-Default
   möglich, aber nur bei erfüllten Anforderungen; SHA-gebundene Mergeoption
   verwenden. Ungefragter Consumer-Fanout und ungeprüfter Merge bleiben aus.
7. Gedeckte Diagnose, Absicherung und Korrekturen fortsetzen und betroffene
   Checks erneuern. Negative Checks, verlangte menschliche Reviews und offene
   Threads sperren die abhängige Stufe. Native Ablehnungen nicht umgehen.
8. Nach einem Merge den integrierten Ergebnisstand auf dem vorgesehenen
   Remote-Hauptbranch nachlesen, auch bei Squash oder Rebase. Push und
   Auto-Mergevormerkung sind Zwischenstände. Prüfe relevante durch
   Konfliktauflösung oder neue Eingaben geänderte Eigenschaften gezielt nach.
9. Bringe den bezeichneten sauberen lokalen Hauptcheckout per bereits
   autorisiertem Fast-forward auf den frisch bestätigten Remote-Stand.
   Prüfe Remote, Branch, Commit und Arbeitszustand danach und halte den
   Prüfzeitpunkt fest. Fremde Änderungen, unabhängige lokale Commits und
   parallel genutzte Bereiche bleiben geschützt. Bei Abweichung den Rest
   benennen und auf Reset sowie ungefragtes Stash verzichten.

## Gedeckte Abschlussbereinigung

1. Sichere dauerhaft nötige Änderungen, Betriebsinformationen und belegte
   Erkenntnisse rechtzeitig in vorhandenen passenden Quellen und integriere sie
   im vereinbarten Umfang. Schütze Secrets und private Rohdaten.
2. Prüfe vor Entfernung auf allen tatsächlich beteiligten freigegebenen Hosts
   Eigentum, Mandat, Integration sowie Ausführungs-, Dienst- und
   Recoveryabhängigkeiten. Überführe weiter verwendete Dateien zuerst an den
   dauerhaften Betriebsort und prüfe die neue Abhängigkeit.
3. Bereinige ausschließlich eigene entbehrliche Taskressourcen, etwa
   Arbeitskopien, integrierte Branches, Worktrees, Testdaten, Transferdateien,
   Hilfsskripte und Zusatzsicherungen. Beende eigene temporäre Prozesse, deren
   Zweck entfallen ist. Schütze fremde Arbeit, reguläre Backups, gemeinsame
   Caches und Gitdaten. Beachte `worktree-safety` und `backup-restore-validation`.
4. Schütze den aktiven Ausführungskontext. Ein vorhandener Integrator außerhalb
   entbehrlicher Worker-Worktrees kann nach deren Ende den Vollzug prüfen.
   Für den letzten aktiven T3-Worktree nutze nach Erledigung der übrigen Punkte
   nur passend eingerichtete native Möglichkeiten. Die Consumer-Dokumentation
   `.agent-core/CONFIGURATION.md` beschreibt Settle und Cleaner. Berichte
   veranlasst, ausstehend oder nachgelesen entfernt anhand tatsächlicher Evidenz.
5. Lies Entfernung und Prozessende nach. Prüfe bei größeren Beständen auch den
   verfügbaren Speicher am betroffenen Ort. Weise physische Einsparungen nur
   bei zuordenbarer Messung aus. Nenne bei einem offenen Pflichtrest Host,
   Ort/Objekt, Grund und weitere Behandlung. Erledige unabhängige Reste weiter.

Berichte Ergebnis, PR, bestätigten Remote- und lokalen Stand, wesentliche
Prüfungen und Bereinigungsstatus. Für die letzten Löschungen genügen Nachlesen
und Abschlussmeldung. Ein Commit sichert Wiederherstellbarkeit. Eine
Tasknotiz dokumentiert bestehende Freigaben.
Verfügbare Plugins, Apps, MCP-Werkzeuge oder Skills erteilen für einzelne
Aktionen keine Autorisierung. Neue Live-, Credential-, Kosten- oder fremde
Repositorywirkungen benötigen eine konkrete Freigabe.
