# Standardmodule, Import, Namensräume und `help`
#
# Tag 3, Einheit 14
# Skript: `tag3/14_module_und_namensraeume.py`
#
# Ziel
#
# Du bindest Module der Standardbibliothek ein, unterscheidest die drei üblichen Importformen und liest den Docstring einer Funktion. Eine Zuweisung in einer Funktion bleibt lokal.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten. Optional in der Konsole: `help(math.fabs)`. Die Ansicht verlässt du mit `q`.

# Drei Importformen
#
#     import math
#     import math as m
#     from math import fabs
#
# | Form | Aufruf | Namensraum |
# | --- | --- | --- |
# | `import math` | `math.fabs` | der Modulname bleibt sichtbar |
# | `import math as m` | `m.fabs` | kürzerer Name für dasselbe Modul |
# | `from math import fabs` | `fabs` | der Name liegt direkt im Skript |
#
# Die erste Form ist in diesem Kurs der Normalfall. Man sieht, woher der Name kommt. `math` und `csv` gehören zur Standardbibliothek. Sie stehen nicht in `environment.yml`. `doctest` und `unittest` am Tag 4 ebenso.

# CSV mit dem Modul `csv`
#
# Einheit 13 hat die Kommas selbst zerlegt. `csv.DictReader` liest die Kopfzeile und liefert jede Datenzeile als Dictionary. Die Schlüssel sind `timestamp`, `sensor` und `celsius`. `newline=""` lässt das Modul die Zeilenenden selbst erkennen.

# Gültigkeitsbereiche und Docstring
#
# `first_above` weist `status` zu. Dieser Name gilt in der Funktion, nicht im Rest des Skripts. Den Namen `limit` liest die Funktion nur. Lesen eines globalen Namens braucht kein `global`. Erst eine Zuweisung würde einen lokalen Namen erzeugen, wie am Tag 2.
#
# Eingebaute Namen wie `len` und `open` liegen in einem weiteren Bereich. Python durchsucht ihn, wenn das Skript und die Funktion den Namen nicht selbst definiert haben.
#
# Der Docstring ist der Text direkt unter der Funktionszeile. `math.fabs.__doc__` ist dieser Text. In der IPython-Konsole zeigt `help(math.fabs)` dieselbe Hilfe. Docstrings in diesem Kurs sind Englisch.

import csv
import math
import math as m
from math import fabs

print("math.fabs", math.fabs(-0.4))
print("m.fabs", m.fabs(-0.4))
print("fabs", fabs(-0.4))
print("doc", math.fabs.__doc__.splitlines()[0])

def first_above(values, limit):
    status = "inside"
    for value in values:
        if value > limit:
            status = "above"
            break
    return status

limit = 21.0
print("limit outside", limit)
print("status", first_above([20.0, 21.4], limit))
print("limit still", limit)

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
# Der Abstand zwischen `low` und `high` ist der Betrag der Differenz. Lege ihn in `spread` ab. Nutze `math.fabs`. Für 19,5 und 21,0 ist das Ergebnis `1.5`.

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
