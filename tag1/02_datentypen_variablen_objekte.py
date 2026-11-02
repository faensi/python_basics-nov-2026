# Datentypen, Klassen, Variablen, Objekte
#
# Tag 1, Einheit 02
# Skript: `tag1/02_datentypen_variablen_objekte.py`
#
# Ziel
#
# Du unterscheidest Zahl, Text, Wahrheitswert und den leeren Wert `None`. Du bindest einen Namen an einen Wert und denselben Namen später an einen anderen Wert.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten. Nach einem Lauf zeigt der Variablenexplorer die Namen.

# Vier Begriffe
#
# Ein Objekt ist ein Wert im Speicher, zum Beispiel die Zahl 20,1 oder der Text `bath`.
#
# Der Datentyp sagt, was du mit dem Objekt tun darfst. Eine Temperatur in Grad Celsius ist hier eine Gleitkommazahl, eine Anzahl eine ganze Zahl, ein Sensorname ein Text.
#
# Die Klasse ist das Bauteil, das solche Objekte erzeugt. `type(20.1)` liefert die Klasse `float`. Jeder Wert ist ein Objekt einer Klasse. Eigene Klassen schreibst du am Tag 4.
#
# Eine Variable ist ein Name, der auf ein Objekt zeigt. Der Name steht links, der Wert rechts: `celsius = 20.1`.
#
# | Wert | Klasse | Rolle |
# | --- | --- | --- |
# | `3` | `int` | Anzahl |
# | `20.1` | `float` | Temperatur |
# | `"bath"` | `str` | Name des Sensors |
# | `True` | `bool` | Ja-oder-nein-Kennzeichen |
# | `None` | `NoneType` | noch kein Wert vorhanden |
#
# `True` und `False` sind eigene Werte. `None` ist nicht die Zahl 0 und nicht der leere Text. Es bedeutet: hier liegt nichts.

count = 3
celsius = 20.1
label = "bath"
valid = True
missing = None
print("count", count, type(count).__name__)
print("celsius", celsius, type(celsius).__name__)
print("label", label, type(label).__name__)
print("valid", valid, type(valid).__name__)
print("missing", missing, type(missing).__name__)

# Namen neu binden
#
# `earlier = celsius` und danach `celsius = 21.0`: der Name `earlier` zeigt weiter auf 20,1. Nur `celsius` zeigt danach auf 21,0. Du hast das erste Objekt nicht verändert, sondern einen Namen umgehängt.
#
# Derselbe Name darf danach auf ein Objekt einer anderen Klasse zeigen. In C oder Java wäre das eine andere, fest deklarierte Variable.

earlier = celsius
celsius = 21.0
print("earlier", earlier)
print("celsius", celsius)
value = 20
print("value as number", value, type(value).__name__)
value = "bath"
print("value as text", value, type(value).__name__)

# Übung
#
# Schreibe eigene Namen. Die Werte `3`, `20.1` und `"bath"` übernimmst du nicht.
#
# - `count` ist eine ganze Zahl.
# - `celsius` ist eine Temperatur mit Nachkommastelle.
# - `label` ist ein Text.
# - `valid` ist `True` oder `False`.
# - `missing` ist `None`.
#
# Merke dir danach die Temperatur unter `earlier` und hänge `celsius` auf eine andere Temperatur um. Gib die Namen aus.

# lösung ab hier:
count =
celsius =
label =
valid =
missing =
earlier =
celsius =
print("exercise", label, count, earlier, celsius, valid, missing)

# Lösung

count = 5
celsius = 18.4
label = "hall"
valid = False
missing = None
earlier = celsius
celsius = 19.0
print("solution", label, count, earlier, celsius, valid, missing)

# Weiter mit `tag1/03_listen_tupel_slicing.ipynb`.
