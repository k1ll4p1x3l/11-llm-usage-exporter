---
name: git-change-lifecycle
description: Use for any repository-writing task and for branch creation, milestone commits, pushes, pull requests, review fixes, merge readiness, merges, or branch/worktree cleanup so each change stays isolated, recoverable, reviewable, and bounded by the correct human gates.
---

# Git-Änderungen und Abschluss

1. Vor Schreibarbeit Repository, aktuellen Branch, Default-Branch, Worktrees,
   lokalen Diff und gegebenenfalls Upstream lesen. Bei unbekannter Topologie
   oder unabhängigen Änderungen zuerst klären. Read-only braucht keinen Branch.
2. Für eine unabhängige Änderung einen geeigneten Topic-Branch im autorisierten
   Worktree nutzen; eine Fortsetzung behält den vorhandenen Task-/PR-Branch.
   Default-/geschützte Branches und Detached HEAD bleiben read-only.
3. Kleine zusammenhängende Änderungen nach passenden Repo-Prüfungen committen.
   Explizite Pfade stagen; keine fremden Änderungen, Secrets oder wissentlich
   defekten Zwischenstände einschließen. Lokale Implementierungsfreigabe deckt
   notwendige Task-Branches und lokale Commits, sofern nicht ausgeschlossen.
4. Ein reiner Analyse-/Reviewauftrag bleibt read-only. Ein konkreter
   Implementierungsauftrag umfasst ohne engeren Nutzerendpunkt den normalen
   Push des eigenen Topic-Branches und einen prüfbereiten Draft-PR. Push, PR,
   Merge und Cleanup bleiben unterscheidbare Wirkungen: Merge und Cleanup
   brauchen ihre eigene konkrete Freigabe oder einen diese Stufen ausdrücklich
   umfassenden Auftrag. Fehlende Freigaben gebündelt am vorbereiteten Diff
   klären; gültige Freigaben bei normalen Korrekturen weiter nutzen. Kein
   obligatorischer JSON-Vertrag und keine Selbstfreigabe durch Hashes.
5. Vor Push Ziel und vollständigen Diff prüfen. Kein Force-Push oder direkter
   Default-Branch-Push. Erste PR bevorzugt als Draft; Ziel, Head und Ergebnis
   nachlesen. Beschreibungen erklären Problem, Änderung, Prüfung und Grenzen.
6. Vor Merge PR-Identität, aktuellen Head, Base, vollständigen Diff, Checks,
   vorgeschriebene Reviews, offene Threads und Mergefähigkeit frisch lesen.
   Ein ausdrücklich autorisierter Merge ist auch nach einem Draft-Default
   möglich, aber nur bei erfüllten Anforderungen; SHA-gebundene Mergeoption
   verwenden. Ungefragter Consumer-Fanout und ungeprüfter Merge bleiben aus.
7. Normale Scopefehler mit bestehender Freigabe korrigieren und betroffene
   Checks erneuern. Negative Checks, verlangte menschliche Reviews und offene
   Threads bleiben Gates. Native Ablehnungen nicht umgehen.
8. Mergeergebnis auf dem Default-Branch nachlesen. Nur freigegebene eigene,
   integrierte Branches und Worktrees bereinigen; fremde Änderungen erhalten.
   Ein Hauptcheckout kann gemeinsame Git-Daten anderer Worktrees enthalten:
   diese nicht zusammen mit seinem Arbeitsbaum löschen.

Abschluss nennt Worktree/Branch, Commit, Remote-/PR-Stand, Prüfung, verbleibende
Grenze und nächsten Schritt. Ein Commit ist Wiederherstellbarkeit, kein
Korrektheits- oder Freigabenachweis. Eine Tasknotiz dokumentiert Rechte nur.
Verfügbare Plugins, Apps, MCP-Werkzeuge oder Skills erteilen für einzelne
Aktionen keine Autorisierung. Neue Live-, Credential-, Kosten- oder fremde
Repositorywirkungen benötigen eine konkrete Freigabe.
