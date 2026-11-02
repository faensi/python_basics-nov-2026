# Schleifen
#
# Tag 2, Einheit 09
# Skript: `tag2/09_schleifen.py`
#
# Ziel
#
# Du schreibst `while`- und `for`-Schleifen, eine Indexschleife und setzt `continue`, `break`, `else` und `pass` gezielt ein.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# `while` und `for`
#
# `while` wiederholt, solange die Bedingung gilt. Du musst die Zählvariable selbst erhöhen, sonst endet die Schleife nicht.
#
# `for reading in readings` geht die Werte der Reihe durch. Das ist die Schleife, die in Einheit 05 den Iterator benutzt hat.

# Indexschleife wie in C und C++
#
# In C schreibst du oft:
#
#     for (int index = 0; index < n; index++) {
#         printf("%d %f\n", index, readings[index]);
#     }
#
# In Python übernimmt `range` die Zählung von 0 bis vor `len(readings)`:
#
#     for index in range(len(readings)):
#         print(index, readings[index])
#
# Wenn du den Index nicht brauchst, ist `for reading in readings` die deutlichere Form.

# `continue`, `break`, `else`, `pass`
#
# - `continue` bricht nur diesen Durchlauf ab und macht mit dem nächsten Wert weiter. So wird ein fehlender Wert `None` übersprungen.
# - `break` verlässt die Schleife ganz.
# - `else` an einer Schleife läuft, wenn die Schleife nicht mit `break` verlassen wurde. Es ist kein Ersatz für `else` an `if`.
# - `pass` ist eine leere Anweisung. Sie hält den Platz, solange ein Zweig noch keinen Code hat.

readings = [19.0, 20.0, 21.0]
print("while:")
index = 0
while index < len(readings):
    print(index, readings[index])
    index = index + 1
print("range:")
for index in range(len(readings)):
    print(index, readings[index])
print("for:")
for reading in readings:
    print(reading)
print("continue skips a missing value:")
series = [20.0, None, 21.0]
for reading in series:
    if reading is None:
        continue
    print(reading)
print("break and else:")
limit = 22.0
for reading in readings:
    if reading > limit:
        print("stopped at", reading)
        break
else:
    print("no value above the limit")
for reading in readings:
    if reading < 0:
        pass
    else:
        print("kept", reading)

# Übung
#
# Zähle in `count`, wie viele Werte am Anfang von `values` höchstens `limit` sind. Höre beim ersten größeren Wert auf. Der Wert 19,0 am Ende wird nicht mehr gezählt, weil die Schleife bei 21,0 endet. Das Ergebnis ist `2`.
#
# Nutze `for` und `break`. Schreibe keine Funktion.

# gegeben:
values = [20.0, 20.2, 21.0, 19.0]
limit = 20.5

# lösung ab hier:
count =
for value in values:
    if :
        break
    count =
print("exercise", count)

# Lösung

values = [20.0, 20.2, 21.0, 19.0]
limit = 20.5
count = 0
for value in values:
    if value > limit:
        break
    count = count + 1
print("solution", count)

# Weiter mit `tag2/10_funktionen.ipynb`.
