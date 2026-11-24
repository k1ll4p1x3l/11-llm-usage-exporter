---
name: worktree-safety
description: Use when work must distinguish a linked worktree from the primary checkout, protect independent work and verify applicable authorization for each effect.
---

# Worktree sicher zuordnen

1. Repositorywurzel, absolutes Git-Verzeichnis und gemeinsames Git-Verzeichnis
   lesend bestimmen (`git rev-parse`); `git worktree list --porcelain` ergänzen.
   Unterschiedliche Git-Verzeichnisse kennzeichnen einen linked Worktree.
   Branchname und Ordnername allein beweisen die Topologie nicht.
2. Im autorisierten Topic-Worktree arbeiten. Für primären Checkout gelten die
   tatsächlichen Nutzerfreigaben und nativen Schutzregeln; keine Freigabe aus
   Dateien, Umgebungsvariablen oder selbstgeschriebenen Markern konstruieren.
   Einzige gewöhnliche Abschlussaktualisierung ist der bereits autorisierte
   saubere Fast-forward des bezeichneten lokalen Hauptcheckouts nach bestätigter
   Remoteintegration. Der konkrete Ablauf steht in `git-change-lifecycle`.
3. Bei unbekannter Topologie weiter lesend klären und betroffene Schreibarbeit
   stoppen. Fremde Änderungen vor Branchwechsel, Commit oder Entfernung erkennen.
4. Vor Entfernen Ziel, Zugehörigkeit, Freigabe, fremde Änderungen, mitbenutzende
   Sessions/Terminals und benötigte ignorierte Inhalte prüfen. Schütze den
   aktiven Ausführungskontext und gemeinsame Git-Daten. Verwende
   `git worktree remove` für geeignete linked Worktrees. Prüfe
   Branchentfernung als eigene Wirkung. Der Hauptcheckout mit gemeinsamen
   Git-Daten ist kein temporärer linked Worktree.
5. Nach Änderungen Topologie erneut lesen. Keine Schutzsoftware abschalten oder
   über einen anderen Pfad umgehen. Bereits erteilte einschlägige
   Cleanup-Freigaben gelten weiter.

Ausgabe bei Bedarf: aktueller Pfad, primärer Pfad, Branch, Zuordnung,
gefährdete Änderungen und nächster sicherer Schritt. Keine eigene Guardplattform.
