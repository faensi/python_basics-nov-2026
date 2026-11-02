# Standardmodule, Import, Namensräume und `help`

**Tag 3, Einheit 14**  
**Skript:** `tag3/14_module_und_namensraeume.py`

## Ziel

In dieser Einheit bindest du Module der Standardbibliothek ein, unterscheidest die drei üblichen Importformen und liest den Docstring einer Funktion. Dabei siehst du, dass eine Zuweisung in einer Funktion lokal bleibt.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `spread` ergänzen. Benutze `math.fabs`.
4. In der Konsole `check_spread()` aufrufen.
5. Optional in der Konsole: `help(math.fabs)`. Die Ansicht verlässt du mit `q`.

## Drei Importformen

```python
import math
import math as m
from math import fabs
```

Alle drei erreichen die Betragsfunktion. Der Name, unter dem du sie rufst, ist verschieden:

| Form | Aufruf | Namensraum |
| --- | --- | --- |
| `import math` | `math.fabs` | der Modulname bleibt sichtbar |
| `import math as m` | `m.fabs` | kürzerer Name für dasselbe Modul |
| `from math import fabs` | `fabs` | der Name liegt direkt im Skript |

Die erste Form ist in diesem Kurs der Normalfall. Man sieht, woher der Name kommt.

`math` und `csv` gehören zur Standardbibliothek. Sie stehen nicht in `environment.yml`, weil sie mit Python mitgeliefert werden. `doctest` und `unittest` am Tag 4 ebenso.

## CSV mit dem Modul `csv`

Einheit 13 hat die Kommas selbst zerlegt. `csv.DictReader` liest die Kopfzeile und liefert jede Datenzeile als Dictionary. Die Schlüssel sind `timestamp`, `sensor` und `celsius`.

```python
with open(path, encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
```

`newline=""` lässt das Modul `csv` die Zeilenenden selbst erkennen. Das ist der übliche Aufruf für dieses Modul.

## Gültigkeitsbereiche

`first_above` weist `status` zu. Dieser Name gilt in der Funktion, nicht im Rest des Skripts. Den Namen `limit` liest die Funktion nur. Lesen eines globalen Namens braucht kein `global`. Erst eine Zuweisung würde einen lokalen Namen erzeugen, wie am Tag 2.

Eingebaute Namen wie `len` und `open` liegen in einem weiteren Bereich, den Python durchsucht, wenn das Skript und die Funktion den Namen nicht selbst definiert haben.

## Docstring und `help`

Der Docstring ist der Text direkt unter der Funktionszeile. `math.fabs.__doc__` ist dieser Text. In der IPython-Konsole zeigt `help(math.fabs)` dieselbe Hilfe.

## Übung

`spread(19.5, 21.0)` liefert den Betrag der Differenz, also `1.5`. Nutze `math.fabs`.

## Lösung

```python
def solution_spread(low, high):
    return math.fabs(high - low)
```

Weiter mit `tag3/15_eigene_module.md`.
