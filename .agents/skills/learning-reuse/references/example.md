# Herkunft und Grenze des Lernbeispiels

Das benachbarte `example.json` zeigt eine eng begrenzte übernommene Erfahrung,
kein aktuell auszuführendes Testszenario. Der belegte Fall betraf frisch erzeugte
Python-Testdateien ohne vorherigen Bytecode: `-B` verhindert das Erzeugen von
Bytecode, ignoriert vorhandene Caches aber nicht allgemein.

Die ursprüngliche Prüfung gehört zum historischen Essentials-Stand
`9d44dba5fec10ea726bd4bcd9f588644b102260d`, dort
`tests/test_learning_reuse.py`. Dieser Test ist aus dem aktuellen Produktumfang
entfernt. Er wird nicht erneut gefordert und sein Ergebnis nicht als neuer Lauf
behauptet. Bei einer tatsächlich passenden Consumeraufgabe Version, Umgebung
und Trigger prüfen; das Beispiel allein belegt keine allgemeine Fehlerfreiheit.
