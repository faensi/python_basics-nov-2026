# Eigene Module, Dokumentation und Hilfe
#
# Tag 3, Einheit 15
# Skript: `tag3/15_eigene_module.py`
# Modul: `tag3/measurement.py`
#
# Ziel
#
# Du lagerst Funktionen in eine eigene Datei aus, importierst sie und liest die Hilfe aus dem Docstring.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Öffne zuerst `tag3/measurement.py`, dann diese Einheit. Skript mit F5, oder die Zellen von oben nach unten. Optional: `help(measurement.mean)` und die Ansicht mit `q` verlassen.

# Warum eine zweite Datei
#
# `measurement.py` enthält den Mittelwert, die Abweichung, die Toleranzprüfung und die Umrechnung von Grad Celsius nach Kelvin. Das sind dieselben Rechnungen wie an den vorigen Tagen, jetzt an einem Ort, den mehrere Skripte nutzen können.
#
# Die Datei liegt neben diesem Skript. Wenn du das Skript mit F5 startest, findet `import measurement` diese Datei, weil Spyder den Ordner des Skripts durchsucht. Ein `import measurement` in einer Konsole ohne diesen Ordner findet die Datei nicht.
#
# Der englische Text unter `def mean` ist der Docstring. Er beschreibt, was die Funktion leistet. `measurement.mean.__doc__` gibt ihn aus.

import measurement

readings = [20.0, 21.0, 22.0]
print("mean", measurement.mean(readings))
print("deviation", round(measurement.deviation(21.4, 21.0), 1))
print("within", measurement.within_tolerance(21.4, 21.0, 0.5))
print("kelvin", measurement.celsius_to_kelvin(20.0))
print("doc:", measurement.mean.__doc__)

# Übung
#
# Lege ein Dictionary `result` mit zwei Schlüsseln an.
#
# - `"mean"`: der Mittelwert von `values`, über `measurement.mean`
# - `"within"`: ob dieser Mittelwert innerhalb der Toleranz um `reference` liegt, geprüft mit `measurement.within_tolerance`
#
# Für `[20.0, 21.0, 22.0]`, Referenz 21,0 und Toleranz 0,5 entsteht `{"mean": 21.0, "within": True}`.

# gegeben:
import measurement

values = [20.0, 21.0, 22.0]
reference = 21.0
tolerance = 0.5

# lösung ab hier:
average =
result =
print("exercise", result)

# Lösung

import measurement

values = [20.0, 21.0, 22.0]
reference = 21.0
tolerance = 0.5
average = measurement.mean(values)
result = {
    "mean": average,
    "within": measurement.within_tolerance(average, reference, tolerance),
}
print("solution", result)

# Weiter mit `tag4/16_klassen.ipynb`. Die Zusammenfassung des Tages steht in `tag3/Tag3_Zusammenfassung.md`.
