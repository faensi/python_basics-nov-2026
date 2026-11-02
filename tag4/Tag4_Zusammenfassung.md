# Tag 4: Klassen, Debugging und Tests

## Behandelte Themen

1. **Klassen** (Einheit 16). Klasse, Instanz, `__init__`, `self`, Methode. Keine Vererbung.
2. **Debugging** (Einheit 17). Haltepunkt, Menü **Debug**, Einzelschritt, Variablenexplorer, falscher Slice.
3. **Systematisches Testen und doctest** (Einheit 18). Beispiel im Docstring, üblicher Fall, Rand, Grenze, `python -m doctest`.
4. **unittest** (Einheit 19). `TestCase`, `assertEqual`, `assertRaises`, eine absichtliche Fehlermeldung.

## Wichtige Konzepte

- Zwei Instanzen teilen ihre Attribute nicht, wenn die Werte auf `self` liegen.
- Ein Debugger hilft bei einem falschen Ergebnis, nicht nur bei einem Abbruch.
- Ein Test nennt das erwartete Ergebnis. Bei einem Fehlschlag änderst du zuerst die Funktion.
- `doctest` vergleicht die Textdarstellung, einschließlich Leerzeichen und Vorzeichen.
- `unittest` sammelt benannte Testmethoden.

## Stichpunkte

- Kelvin aus Grad Celsius: zur Zahl 273,15 addieren.
- Der fehlerhafte Slice `values[1:]` wirft den ersten Wert weg. `values[:-1]` wirft den letzten weg.
- `check_is_within` und `check_mean_without_ends` prüfen die Übungen der Einheiten 16 und 17.
- Die Einheiten 18 und 19 prüfen sich beim Ausführen selbst.

## Zum Schluss

Die vier Tage hängen an derselben kleinen Messsituation: eine Reihe von Temperaturen, ein Referenzwert, eine Toleranz. Listen und Schnitte, Schleifen und Funktionen, Dateien und das Modul `measurement`, zuletzt eine Klasse `Reading` und Tests dafür.

Das Arbeitsverzeichnis bleibt `this_course`. Die Umgebung bleibt `python_grundlagen` in Spyder.
