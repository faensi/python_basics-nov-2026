# Umwandlung, Referenz, In-Place-Methoden, `copy` und `deepcopy`
#
# Tag 1, Einheit 07
# Skript: `tag1/07_konvertierung_referenzen_kopien.py`
#
# Ziel
#
# Du wandelst Werte zwischen Text, Zahl, Liste und Dictionary um, erkennst, wann zwei Namen dasselbe Objekt meinen, und kopierst eine verschachtelte Gruppe so, dass eine spätere Änderung nicht zurückwirkt.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Umwandlung
#
# | Aufruf | Ergebnis | Hinweis |
# | --- | --- | --- |
# | `int("20")` | `20` | Text aus Ziffern wird zur ganzen Zahl |
# | `str(20)` | `"20"` | Zahl wird Text |
# | `float("20.5")` | `20.5` | Text wird Gleitkommazahl |
# | `int(20.9)` | `20` | Der Nachkommateil fällt weg, es wird nicht gerundet |
# | `list(ein_dict.items())` | Liste von Paaren | Schlüssel und Wert nebeneinander |
# | `dict(paare)` | Dictionary | der Weg zurück |
#
# `int("20.5")` schlägt fehl, weil der Text keine ganze Zahl ist. Die nächste Zelle führt diesen Aufruf nicht aus.

number = int("20")
text = str(number)
print("int to str", text, type(text).__name__)
print("str to float", float("20.5"))
print("float to int truncates", int(20.9))
reading_map = {"bath": 20.1, "room": 21.5}
as_pairs = list(reading_map.items())
restored = dict(as_pairs)
print("pairs", sorted(as_pairs))
print("restored", sorted(restored.items()))

# Zwei Namen, ein Objekt
#
# `second = first` legt keinen zweiten Datenbestand an. Es sind zwei Namen für dieselbe Liste. `append` ändert dieses eine Objekt, deshalb sieht `first` den neuen Wert ebenfalls.
#
# Eine Zahl funktioniert anders, weil du sie nicht an Ort und Stelle änderst, sondern den Namen neu bindest. Das war die Zuweisung `celsius = 21.0` in Einheit 02.

# In-Place-Methoden und Kopien
#
# `sorted(first)` baut eine neue Liste und lässt `first` in Ruhe. `first.sort()` sortiert `first` selbst und gibt `None` zurück.
#
# `copy.copy` legt eine neue äußere Liste an. Die Einträge darin sind weiterhin dieselben Objekte. Bei einer Liste von Zahlen genügt das.
#
# `copy.deepcopy` kopiert auch die verschachtelten Listen. Das brauchst du, wenn eine Gruppe selbst wieder Listen enthält. Die nächste Zelle ändert den ersten Temperaturwert auf 25,0 und hängt eine weitere Gruppe an.
#
# - `alias` ist `groups` und enthält die Änderung und den neuen Eintrag.
# - Die flache Kopie enthält die geänderte Innentemperatur, aber nicht den neuen Eintrag.
# - Die tiefe Kopie steht noch auf 20,1 und 21,5.

import copy

first = [20.2, 19.8, 20.0]
second = first
second.append(21.0)
print("shared list", first)
print("sorted leaves the source", sorted(first), first)
print("list.sort returns", first.sort())
print("source after sort", first)
groups = [["bath", 20.1], ["room", 21.5]]
alias = groups
shallow = copy.copy(groups)
deep = copy.deepcopy(groups)
alias[0][1] = 25.0
alias.append(["probe", 18.0])
print("alias", alias)
print("shallow shares inner lists", shallow)
print("deep stays independent", deep)

# Übung
#
# Mach aus `text_celsius` die Gleitkommazahl `18.6` und lege sie in `celsius` ab.
#
# Kopiere `numbers` flach nach `snapshot` und sortiere nur die Kopie mit `sort`. `numbers` bleibt `[22.0, 17.5, 19.5]`. Die Kopie ist `[17.5, 19.5, 22.0]`.
#
# Lege von `log` eine tiefe Kopie in `independent` an.

# gegeben:
import copy

text_celsius = "18.6"
numbers = [22.0, 17.5, 19.5]
log = [["hall", 19.2], ["lab", 22.0]]

# lösung ab hier:
celsius =
snapshot =
independent =
print("exercise", celsius)
print("exercise", snapshot, numbers)
print("exercise", independent)

# Lösung

import copy

text_celsius = "18.6"
numbers = [22.0, 17.5, 19.5]
log = [["hall", 19.2], ["lab", 22.0]]
celsius = float(text_celsius)
snapshot = copy.copy(numbers)
snapshot.sort()
independent = copy.deepcopy(log)
print("solution", celsius)
print("solution", snapshot, numbers)
print("solution", independent)

# Weiter mit `tag2/08_verzweigungen.ipynb`. Die Zusammenfassung des Tages steht in `tag1/Tag1_Zusammenfassung.md`.
