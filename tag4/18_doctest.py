# Systematisches Testen und `doctest`
#
# Tag 4, Einheit 18
# Skript: `tag4/18_doctest.py`
#
# Ziel
#
# Du schreibst zu einer Funktion ein konkretes Beispiel und lässt das Modul `doctest` dieses Beispiel aus dem Docstring ausführen.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten. Die letzte Zelle meldet `doctest: ... tests, 0 failures`.
#
# Im Terminal, aus dem Ordner `python_basics-nov-2026`:
#
#     python -m doctest tag4/18_doctest.py
#
# Ohne Befund ist die Ausgabe leer. Das ist der Erfolg.

# Was systematisches Testen hier heißt
#
# Ein Test nennt eine Eingabe und das erwartete Ergebnis. Für eine kleine Funktion reichen drei Lagen: der übliche Fall, der Rand und die Grenze einer Toleranz.
#
# Schlägt ein Beispiel fehl, prüfe zuerst die Funktion. Das erwartete Ergebnis änderst du nur, wenn es selbst falsch war. `doctest` und `unittest` gehören zur Standardbibliothek.
#
# Im Docstring steht ein Aufruf wie in der Konsole, mit `>>>`. Die nächste Zeile ist die erwartete Darstellung. Leerzeichen zählen. `'+1.0'` und `'+1.00'` sind nicht dasselbe.
#
# Eine erwartete Ausnahme schreibst du so:
#
#     >>> mean([])
#     Traceback (most recent call last):
#     ...
#     ValueError: values must not be empty
#
# Die Zeile `...` steht für den übrigen Traceback. `doctest` prüft danach den Fehlertyp und die Meldung.

# Die Beispiele
#
# `mean([20.0, 22.0])` ist 21,0. Eine einzelne Zahl ist ihr eigener Mittelwert. Eine leere Reihe löst `ValueError` aus.
#
# `format_deviation` formatiert die Differenz mit Vorzeichen und einer Nachkommastelle. 21,0 gegen 20,0 ergibt `+1.0`, 19,0 gegen 20,0 ergibt `-1.0`, gleiche Werte ergeben `+0.0`.
#
# `within_tolerance(20.4, 20.0, 0.5)` ist wahr. `within_tolerance(20.5, 20.0, 0.5)` ist ebenfalls wahr, weil die Grenze dazugehört. `within_tolerance(20.6, 20.0, 0.5)` ist falsch.

def mean(values):
    """Return the arithmetic mean of a non-empty series.

    >>> mean([20.0, 22.0])
    21.0
    >>> mean([20.0])
    20.0
    >>> mean([])
    Traceback (most recent call last):
    ...
    ValueError: values must not be empty
    """
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def format_deviation(reading, reference):
    """Return the signed deviation with one decimal place.

    >>> format_deviation(21.0, 20.0)
    '+1.0'
    >>> format_deviation(19.0, 20.0)
    '-1.0'
    >>> format_deviation(20.0, 20.0)
    '+0.0'
    """
    difference = round(reading - reference, 1)
    return "{:+.1f}".format(difference)


def within_tolerance(reading, reference, tolerance):
    """Return True when the absolute deviation stays within tolerance.

    >>> within_tolerance(20.4, 20.0, 0.5)
    True
    >>> within_tolerance(20.5, 20.0, 0.5)
    True
    >>> within_tolerance(20.6, 20.0, 0.5)
    False
    """
    if tolerance < 0:
        raise ValueError("tolerance must not be negative")
    return abs(reading - reference) <= tolerance

# Übung
#
# Schreibe `celsius_to_kelvin(celsius)`. Sie addiert 273,15. Der Docstring enthält ein Beispiel: aus 0,0 Grad Celsius werden 273,15 Kelvin. Die erwartete Zeile unter `>>>` steht schon da. Ergänze die `return`-Zeile.

# gegeben:
def celsius_to_kelvin(celsius):
    """Convert Celsius to kelvin.

    >>> celsius_to_kelvin(0.0)
    273.15
    """
    # lösung ab hier:
    return celsius +


print("exercise", celsius_to_kelvin(0.0))

# Lösung
#
# Die letzte Zelle ersetzt die Funktion und führt alle Beispiele aus.

def celsius_to_kelvin(celsius):
    """Convert Celsius to kelvin.

    >>> celsius_to_kelvin(0.0)
    273.15
    """
    return celsius + 273.15

print("solution", celsius_to_kelvin(0.0))
if __name__ == "__main__":
    import doctest

    failures, tests = doctest.testmod(verbose=False)
    print("doctest: {0} tests, {1} failures".format(tests, failures))

# Weiter mit `tag4/19_unittest.ipynb`.
