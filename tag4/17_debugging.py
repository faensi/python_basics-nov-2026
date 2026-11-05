# Debugging
#
# Tag 4, Einheit 17
# Skript: `tag4/17_debugging.py`
#
# Ziel
#
# Du liest typische Fehlermeldungen, prüfst Zwischenwerte mit `print`,
# erkennst einen einfachen Off-by-one-Fehler und fängst erwartete Fehler mit
# `try` / `except` ab.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Zellen von oben nach unten
# ausführen.

# Was ist Debugging?
#
# Debugging heißt: herausfinden, warum ein Programm nicht das tut, was du
# erwartest. Entweder bricht es ab (Traceback), oder das Ergebnis ist falsch.

# Eine Fehlermeldung lesen
#
# Die absichtlichen Abbrüche bleiben hier auskommentiert, damit F5 durchläuft.
# Im Notebook führst du die Zellen mit dem Fehler aus und liest den Traceback.

numbers = [10.0, 20.0, 30.0]
# print(numbers[5])
print(len(numbers))
print(numbers[0], numbers[-1])

# Typische Fehlermeldungen
#
# NameError: print(temperature)
# TypeError: print("20.1" + 1)
# ValueError: print(float("room"))
# IndexError: print([19.8, 20.1, 19.9][3])
# ZeroDivisionError: print(10 / 0)
# KeyError: print({"sensor": "bath"}["timestamp"])
# FileNotFoundError: open("missing_file.txt")

# Mit `print` Zwischenwerte prüfen

total = 0.0
for value in [1.0, 2.0, 3.0]:
    total = total + value
    print("value", value, "total", total)
print("end", total)

# Off-by-one: einer zu weit
#
# Die Liste hat drei Werte. Die Indizes sind 0, 1 und 2. Die Länge ist 3.
# readings[len(readings)] greift einen Schritt zu weit.

readings = [19.8, 20.1, 19.9]
print("length", len(readings))
print("last valid index", len(readings) - 1)
print("last value", readings[len(readings) - 1])
# print(readings[len(readings)])

index = len(readings)
print("index", index)
print("allowed", 0, "to", len(readings) - 1)
# print(readings[index])

print(readings[len(readings) - 1])
print(readings[-1])

# Fehler abfangen: `try` und `except`
#
# Manchmal soll das Programm weiterlaufen, wenn ein Schritt scheitern kann.
# In Python heißt das `try` / `except`. Sinnvoll bei äußeren Ursachen wie einer
# fehlenden Datei. Off-by-one und Tippfehler korrigierst du, statt sie zu
# verstecken.

path = "data/notes.txt"
try:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    print(text[:40])
except FileNotFoundError:
    print("file not found:", path)

path = "data/does_not_exist.txt"
try:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    print(text)
except FileNotFoundError:
    print("file not found:", path)

value = "20.1"
try:
    number = float(value)
    print(number)
except ValueError:
    print("not a number:", value)

value = "room"
try:
    number = float(value)
    print(number)
except ValueError:
    print("not a number:", value)

# Übung
#
# 1. Lies `path` mit `try` / `except FileNotFoundError`. Wenn die Datei fehlt,
#    gib `print("file not found:", path)` aus. Wenn sie da ist, gib die ersten
#    20 Zeichen aus.
# 2. Wandle `raw` mit `float` um. Fange `ValueError` ab und gib dann
#    `print("not a number:", raw)` aus. Sonst gib die Zahl aus.
#
# Für die Vorgaben unten siehst du zuerst `file not found: data/does_not_exist.txt`
# und danach `not a number: room`.

# gegeben:
path = "data/does_not_exist.txt"
raw = "room"

# lösung ab hier:


print("exercise done")

# Lösung

path = "data/does_not_exist.txt"
raw = "room"

try:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    print(text[:20])
except FileNotFoundError:
    print("file not found:", path)

try:
    number = float(raw)
    print(number)
except ValueError:
    print("not a number:", raw)

# Weiter mit `tag4/18_doctest.ipynb`.
