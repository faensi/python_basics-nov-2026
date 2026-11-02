# Tag 3: Ein- und Ausgabe und Module

## Behandelte Themen

1. **Eingabe und Format** (Einheit 12). `input`, der alte Name `raw_input`, Prozentformat, Methode `format`.
2. **Dateien** (Einheit 13). `open`, `with`, Lesen, Schreiben, CSV-Zeilen von Hand.
3. **Standardmodule** (Einheit 14). `import`, `import as`, `from ... import`, `math`, `csv`, Docstring, lokal und global.
4. **Eigenes Modul** (Einheit 15). `measurement.py`, Import der Nachbardatei, `help`.

## Wichtige Konzepte

- `input` liefert Text. Zahlen entstehen erst mit `float` oder `int`.
- Pfade zu den Beispieldaten beginnen mit `data/` und gelten vom Ordner `python_basics-nov-2026` aus.
- `with` schließt die Datei.
- Ein Modul ist eine Python-Datei. Der Dateiname ohne `.py` ist der Name im `import`.
- Der Docstring steht im Programm auf Englisch. `help` zeigt ihn in der Konsole.

## Stichpunkte

- Im Programm steht der Dezimalpunkt, zum Beispiel in `"bath: 20.1 C"`.
- `newline=""` gehört zum Lesen mit `csv.DictReader`.
- Eine Liste als Standardargument bleibt ein Fehler. Das hast du am Tag 2 gesehen. Das Modul legt keine solche Liste an.
- Die Übungen sind Zeilen im Skript. Eine eigene Funktion brauchst du dafür nicht. Die Funktionen stehen in `measurement.py`.

## Nächster Tag

Tag 4: eine kurze Einführung in Klassen, danach Debugging und Tests. Beginne mit `tag4/16_klassen.ipynb`.
