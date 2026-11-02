# Funktionen: Definition und Aufruf
#
# Tag 2, Einheit 10
# Skript: `tag2/10_funktionen.py`
#
# Ziel
#
# Du definierst eine Funktion, rufst sie auf und gibst mit `return` einen Wert zurück. Eine Funktion ohne `return` liefert `None`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Form
#
# `def` leitet die Definition ein. Der eingerückte Block ist der Körper. Ein Aufruf schreibt die Argumente in die Klammern.
#
# `announce` hat kein `return`. Der Name `result` ist deshalb `None`. Eine Berechnung, deren Ergebnis du weiterverwenden willst, braucht `return`.
#
# Die mittlere Temperatur einer Reihe ist die Summe geteilt durch die Anzahl. `sum` und `len` sind eingebaute Funktionen. Für `[20.0, 21.0, 22.0]` ist der Mittelwert 21,0.

def announce(sensor):
    print("sensor", sensor)

result = announce("bath")
print("announce returns", result)
readings = [20.0, 21.0, 22.0]
average = sum(readings) / len(readings)
print("inline mean", average)

# Übung
#
# Schreibe die Funktion `mean(values)`. Sie gibt die Summe der Werte geteilt durch ihre Anzahl zurück.
#
# `mean([20.0, 21.0, 22.0])` ist `21.0`. Die Liste soll mindestens einen Wert enthalten. Bei einer leeren Liste wäre die Anzahl 0.

# lösung ab hier:
def mean(values):
    result =
    return result

print("exercise", mean([20.0, 21.0, 22.0]))

# Lösung

def mean(values):
    return sum(values) / len(values)

print("solution", mean([20.0, 21.0, 22.0]))

# Weiter mit `tag2/11_parameter_und_sichtbarkeit.ipynb`.
