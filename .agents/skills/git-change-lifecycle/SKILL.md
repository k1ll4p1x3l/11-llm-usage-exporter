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
4. Push, PR, Merge und Cleanup sind unterscheidbare Wirkungen. Eine konkrete
   bestehende Stufenfreigabe nutzen; bei fehlender Autorisierung den vorbereiteten
   Diff und die gewünschten Schritte gebündelt vorlegen. Kein obligatorischer
   JSON-Vertrag, keine feste künstliche Frist und keine Selbstfreigabe durch Hashes.
5. Vor Push Ziel und vollständigen Diff prüfen. Kein Force-Push oder direkter
   Default-Branch-Push. Erste PR bevorzugt als Draft; Ziel, Head und Ergebnis
   nachlesen. Beschreibungen erklären Problem, Änderung, Prüfung und Grenzen.
6. Vor Merge PR-Identität, aktuellen Head, Base, Checks, vorgeschriebene Reviews,
   offene Threads und Mergefähigkeit frisch lesen. Nur bei gültiger Freigabe
   und erfüllten Anforderungen integrieren; SHA-gebundene Mergeoption verwenden.
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
