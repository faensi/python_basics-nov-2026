# Parameter und Sichtbarkeit
#
# Tag 2, Einheit 11
# Skript: `tag2/11_parameter_und_sichtbarkeit.py`
#
# Ziel
#
# Du rufst eine Funktion mit Positions- und mit Schlüsselwortargumenten auf, unterscheidest einen lokalen Namen von einem globalen und vermeidest eine Liste als Standardargument.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Positions- und Schlüsselwortargumente
#
# `clip` begrenzt eine Anzeige auf ein Intervall. Beide Aufrufe meinen dasselbe: `clip(22.0, 19.0, 21.0)` und `clip(22.0, low=19.0, high=21.0)`. Beim ersten entscheidet die Position, beim zweiten der Name des Parameters. Schlüsselwortargumente stehen nur nach den Positionsargumenten.
#
# Ein Parameter darf einen Standardwert haben. Dann darfst du das Argument beim Aufruf weglassen.

# Lokal und global
#
# Ein Name, den du in einer Funktion zuweist, ist lokal. Er verdeckt einen gleichnamigen Namen außerhalb. `shadow` setzt `step` auf 5 und lässt den globalen Zähler auf 0.
#
# Wer den globalen Namen wirklich ändern will, schreibt `global step` vor der Zuweisung. `advance` macht das. Bevorzuge in diesem Kurs Rückgabewerte. `global` steht hier, damit die Wirkung nicht versehentlich passiert.
#
# Parameter sind lokale Namen der Funktion.

# Standardwert und dasselbe Objekt
#
# Ein Standardwert wird einmal erzeugt, nicht bei jedem Aufruf. Eine Liste als Standard teilen sich alle Aufrufe, die das Argument weglassen. Der zweite Aufruf von `buggy_collect` sieht den Wert aus dem ersten Aufruf noch in der Liste. Das ist derselbe Effekt wie zwei Namen für ein Objekt in Einheit 07.
#
# Die sichere Form nimmt `None` als Standard und legt die Liste im Körper an. Das tut `collect`.
#
# Führst du die Zelle mit `buggy_collect` ein zweites Mal aus, hängen die alten Werte noch in der Liste. Starte dann den Kernel neu, in Spyder die IPython-Konsole.

def clip(reading, low, high):
    if reading < low:
        return low
    if reading > high:
        return high
    return reading

print("positional", clip(22.0, 19.0, 21.0))
print("keyword", clip(22.0, low=19.0, high=21.0))

step = 0

def shadow():
    step = 5
    return step

def advance():
    global step
    step = step + 1
    return step

print("local step", shadow())
print("global step still", step)
print("after advance", advance())
print("global step now", step)

def collect(reading, series=None):
    if series is None:
        series = []
    series.append(reading)
    return series

def buggy_collect(reading, series=[]):
    series.append(reading)
    return series

print("first collect", collect(20.0))
print("second collect", collect(21.0))
print("buggy first", buggy_collect(20.0))
print("buggy second", buggy_collect(21.0))

# Übung
#
# Schreibe `shift(reading, offset=0.0)`. Die Funktion gibt die Anzeige plus den Offset zurück.
#
# `shift(20.0)` liefert `20.0`, weil der Offset dann 0 ist. `shift(20.0, offset=0.5)` liefert `20.5`.

# lösung ab hier:
def shift(reading, offset=0.0):
    adjusted =
    return adjusted

print("exercise", shift(20.0), shift(20.0, offset=0.5))

# Lösung

def shift(reading, offset=0.0):
    return reading + offset

print("solution", shift(20.0), shift(20.0, offset=0.5))

# Weiter mit `tag3/12_eingabe_und_formatierung.ipynb`. Die Zusammenfassung des Tages steht in `tag2/Tag2_Zusammenfassung.md`.
