---
name: worktree-safety
description: Use when work must distinguish a linked worktree from the primary worktree and enforce explicit confirmation before writing in the primary checkout.
---

# Worktree sicher zuordnen

1. Repositorywurzel, absolutes Git-Verzeichnis und gemeinsames Git-Verzeichnis
   lesend bestimmen (`git rev-parse`); `git worktree list --porcelain` ergänzen.
   Unterschiedliche Git-Verzeichnisse kennzeichnen einen linked Worktree.
   Branchname und Ordnername allein beweisen die Topologie nicht.
2. Im autorisierten Topic-Worktree arbeiten. Für primären Checkout gelten die
   tatsächlichen Nutzerfreigaben und nativen Schutzregeln; keine Freigabe aus
   Dateien, Umgebungsvariablen oder selbstgeschriebenen Markern konstruieren.
3. Bei unbekannter Topologie weiter lesend klären und betroffene Schreibarbeit
   stoppen. Fremde Änderungen vor Branchwechsel, Commit oder Entfernung erkennen.
4. Vor Entfernen Ziel, Dirty-Stand und Freigabe prüfen. Aktuellen Worktree und
   gemeinsame Git-Daten schützen. `git worktree remove` für linked Worktrees
   verwenden; ein Hauptcheckout lässt sich nicht wie ein unabhängiger Ordner löschen.
5. Nach Änderungen Topologie erneut lesen. Keine Schutzsoftware abschalten oder
   über einen anderen Pfad umgehen. Bereits konkrete Cleanup-Freigaben gelten weiter.

Ausgabe bei Bedarf: aktueller Pfad, primärer Pfad, Branch, Zuordnung,
gefährdete Änderungen und nächster sicherer Schritt. Keine eigene Guardplattform.
