# Strings, Stringfunktionen, `sort` und `sorted`
#
# Tag 1, Einheit 04
# Skript: `tag1/04_strings_und_sortierung.py`
#
# Ziel
#
# Du bereinigst einen Sensortext mit String-Methoden und unterscheidest `sorted` von `sort`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Strings
#
# Ein String ist Text. Er ist unveränderlich. Methoden liefern einen neuen String, sie schreiben den alten nicht um.
#
# | Methode | Wirkung am Beispiel |
# | --- | --- |
# | `strip()` | Leerzeichen an den Enden von `"  Bath-01  "` weg |
# | `lower()` | Kleinbuchstaben |
# | `split(";")` | `"bath;room"` an einem Trennzeichen zerlegen |
# | `replace(" C", " celsius")` | ein Stück Text ersetzen |
# | `startswith("ba")` | prüfen, womit der Text beginnt |
#
# Methoden lassen sich verketten: `label.strip().lower()`.

# `sorted` und `sort`
#
# `sorted(werte)` liefert eine neue, sortierte Liste. Die Liste, die du übergibst, bleibt wie sie ist.
#
# `werte.sort()` sortiert an Ort und Stelle. Der Rückgabewert ist `None`, nicht die Liste. Wer `print(werte.sort())` schreibt, sieht `None` und hat die Liste trotzdem verändert.

raw_label = "  Bath-01  "
print("strip", raw_label.strip())
print("lower", raw_label.strip().lower())
print("split", "bath;room".split(";"))
print("replace", "20.1 C".replace(" C", " celsius"))
print("startswith", "bath".startswith("ba"))
readings = [20.2, 19.8, 20.0]
print("sorted copy", sorted(readings))
print("original after sorted", readings)
print("sort returns", readings.sort())
print("original after sort", readings)

# Übung
#
# Aus `probe` machst du den Text `"probe_7"`. Entferne die Leerzeichen an den Enden, schreibe klein und ersetze den Bindestrich durch einen Unterstrich.
#
# Aus `series` machst du eine neue sortierte Liste `[18.0, 19.2, 21.5]`. `series` bleibt `[21.5, 18.0, 19.2]`. Nutze `sorted`, nicht `sort`.

# gegeben:
probe = "  Probe-7  "
series = [21.5, 18.0, 19.2]

# lösung ab hier:
tidy =
ordered =
print("exercise", tidy)
print("exercise", ordered, series)

# Lösung

probe = "  Probe-7  "
series = [21.5, 18.0, 19.2]
tidy = probe.strip().lower().replace("-", "_")
ordered = sorted(series)
print("solution", tidy)
print("solution", ordered, series)

# Weiter mit `tag1/05_iteratoren.ipynb`.
