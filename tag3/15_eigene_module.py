# Eigene Module, Dokumentation und Hilfe
#
# Tag 3, Einheit 15
# Skript: `tag3/15_eigene_module.py`
# Modul: `tag3/measurement.py`
#
# Ziel
#
# Du lagerst Funktionen in eine eigene Datei aus, importierst sie und liest die
# Hilfe aus dem Docstring.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Öffne zuerst `tag3/measurement.py`,
# dann diese Einheit. Skript mit F5, oder die Zellen von oben nach unten.
# Optional: `help(measurement.mean)` und die Ansicht mit `q` verlassen.

# Warum eine zweite Datei
#
# `measurement.py` enthält Mittelwert, Abweichung, Toleranzprüfung und die
# Umrechnung von Grad Celsius nach Kelvin. Der Dateiname ohne `.py` ist der
# Name im `import`.

from pathlib import Path
print(Path("tag3/measurement.py").exists())
print(Path("tag3/measurement.py").name)

# Modul finden
#
# Liegt das Arbeitsverzeichnis auf dem Kursordner, findet Python `measurement.py`
# nicht von allein. Die nächsten Zeilen legen den Ordner `tag3` in den Suchpfad.

import sys

module_dir = Path("tag3")
if not (module_dir / "measurement.py").exists():
    module_dir = Path(".")
sys.path.insert(0, str(module_dir.resolve()))
print(module_dir.resolve())

# Import des eigenen Moduls

import measurement
print(measurement)
print(type(measurement))

print(measurement.mean)
print(callable(measurement.mean))

# `mean`

readings = [20.0, 21.0, 22.0]
print(measurement.mean(readings))

print(measurement.mean([19.0, 21.0]))
print(measurement.mean([20.0]))

# `deviation` und `within_tolerance`

print(measurement.deviation(21.4, 21.0))
print(round(measurement.deviation(21.4, 21.0), 1))

print(measurement.within_tolerance(21.4, 21.0, 0.5))
print(measurement.within_tolerance(22.0, 21.0, 0.5))

# `celsius_to_kelvin`

print(measurement.celsius_to_kelvin(20.0))
print(measurement.celsius_to_kelvin(0.0))

# Docstring und Hilfe
#
# Der englische Text unter `def mean` in `measurement.py` ist der Docstring.

print(measurement.mean.__doc__)

print(measurement.deviation.__doc__)
print(measurement.within_tolerance.__doc__)

# Kurzer Alias

import measurement as m
print(m.mean([20.0, 22.0]))
print(m.celsius_to_kelvin(20.0))

# Alles in einem Durchgang

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
# - `"within"`: ob dieser Mittelwert innerhalb der Toleranz um `reference` liegt,
#   geprüft mit `measurement.within_tolerance`
#
# Für `[20.0, 21.0, 22.0]`, Referenz 21,0 und Toleranz 0,5 entsteht
# `{"mean": 21.0, "within": True}`.

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

# Weiter mit `tag4/16_klassen.ipynb`. Die Zusammenfassung des Tages steht in
# `tag3/Tag3_Zusammenfassung.md`.
