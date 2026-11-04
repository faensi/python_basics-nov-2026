# Standardmodule, Import, Namensräume und `help`
#
# Tag 3, Einheit 14
# Skript: `tag3/14_module_und_namensraeume.py`
#
# Ziel
#
# Du bindest Module der Standardbibliothek ein, unterscheidest die drei üblichen
# Importformen, liest einen Docstring und siehst, dass eine Zuweisung in einer
# Funktion lokal bleibt. Danach liest du die Messreihe mit dem Modul `csv`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen
# von oben nach unten. Optional in der Konsole: `help(math.fabs)`. Die Ansicht
# verlässt du mit `q`.

# Was ist ein Modul?
#
# Ein Modul ist eine Python-Datei mit wiederverwendbaren Namen. Die
# Standardbibliothek kommt mit Python. Beispiele: `math`, `csv`.

import math
print(math)
print(type(math))

# Form 1: `import math`

print(math.fabs(-0.4))
print(math.sqrt(9.0))

value = -2.5
print(math.fabs(value))
print(value)

# Form 2: `import math as m`

import math as m
print(m.fabs(-0.4))
print(m.pi)

# Form 3: `from math import fabs`

from math import fabs
print(fabs(-0.4))
print(fabs(1.2))

# Die drei Formen nebeneinander

print("math.fabs", math.fabs(-0.4))
print("m.fabs", m.fabs(-0.4))
print("fabs", fabs(-0.4))

# Docstring und `help`
#
# Der Docstring steht unter der Definition. `help(math.fabs)` zeigt ihn in der
# Konsole. Docstrings in diesem Kurs sind Englisch.

doc = math.fabs.__doc__
print(doc.splitlines()[0])

def add_one(value):
    """Return value plus one."""
    return value + 1

print(add_one(3))
print(add_one.__doc__)

# Lokal und global
#
# Eine Zuweisung in einer Funktion erzeugt einen lokalen Namen. Globale Namen
# darfst du lesen, ohne `global` zu schreiben.

limit = 21.0
print("outside", limit)

def show_limit():
    print("inside", limit)

show_limit()
print("still", limit)

def first_above(values, limit):
    status = "inside"
    for value in values:
        if value > limit:
            status = "above"
            break
    return status

print(first_above([20.0, 21.4], 21.0))
print(first_above([20.0, 20.5], 21.0))

limit = 21.0
print("limit outside", limit)
print("status", first_above([20.0, 21.4], limit))
print("limit still", limit)

# Das Modul `csv`
#
# `csv.DictReader` liest die Kopfzeile und liefert jede Datenzeile als Dictionary.
# `newline=""` gehört zum empfohlenen Muster.

import csv
print(csv)
print(csv.DictReader)

row = {"sensor": "bath", "celsius": "19.94"}
print(row["sensor"])
print(float(row["celsius"]))

with open("data/readings.csv", encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    first = next(reader)
print(first)
print(first["sensor"], first["celsius"])

# Messreihe mit `csv` und `math`

bath = []
with open("data/readings.csv", encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    for row in reader:
        if row["sensor"] == "bath":
            bath.append(float(row["celsius"]))
print("bath count", len(bath))
print("bath spread", round(math.fabs(max(bath) - min(bath)), 1))

# Übung
#
# Der Abstand zwischen `low` und `high` ist der Betrag der Differenz. Lege ihn
# in `spread` ab. Nutze `math.fabs`. Für 19,5 und 21,0 ist das Ergebnis `1.5`.

# gegeben:
low = 19.5
high = 21.0

# lösung ab hier:
spread =
print("exercise", spread)

# Lösung

low = 19.5
high = 21.0
spread = math.fabs(high - low)
print("solution", spread)

# Weiter mit `tag3/15_eigene_module.ipynb`.
