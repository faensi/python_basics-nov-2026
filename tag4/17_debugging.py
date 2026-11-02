# Debugging in Spyder
#
# Tag 4, Einheit 17
# Skript: `tag4/17_debugging.py`
#
# Ziel
#
# Du setzt einen Haltepunkt, startest den Debugger und liest den falschen Zwischenwert im Variablenexplorer.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`.

# Ablauf
#
# 1. Lies `mean_without_ends`, bevor du sie änderst.
# 2. Setze einen Haltepunkt in die Zeile mit `return`. Klicke links neben die Zeilennummer.
# 3. Starte über das Menü Debug den Eintrag Debug. In vielen Spyder-Versionen ist das Strg+F5.
# 4. Geh mit Step einen Schritt. Im Variablenexplorer erscheint `chosen`.
# 5. Vergleiche `chosen` mit der Reihe. Beende den Lauf mit Continue.
# 6. Korrigiere den Slice und führe die Datei mit F5 aus.
#
# Wenn im Variablenexplorer noch Werte aus einem früheren Lauf stehen, starte die IPython-Konsole neu und debugge erneut.
#
# Im Notebook gibt es keinen Spyder-Haltepunkt. Öffne für diese Einheit das Skript.

# Der Fehler
#
# Die Reihe ist `[1.0, 2.0, 3.0, 4.0]`. Der Mittelwert ohne den letzten Wert ist der Mittelwert von 1, 2 und 3, also 2,0.
#
# Die Funktion schneidet stattdessen den ersten Wert ab: `chosen = values[1:]`. Der Mittelwert von 2, 3 und 4 ist 3,0. Der Fehler ist kein Abbruch, sondern ein falsches Ergebnis. Dafür ist der Haltepunkt da: das Skript läuft, und ein Name hat den falschen Inhalt.

def mean_without_ends(values):
    """Return the mean of every value except the last one.

    The slice below is intentionally wrong.
    """
    chosen = values[1:]
    return sum(chosen) / len(chosen)

sample = [1.0, 2.0, 3.0, 4.0]
print("sample", sample)
print("buggy result", mean_without_ends(sample))
print("Set a breakpoint on the return line of mean_without_ends.")

# Übung
#
# `chosen` soll alle Werte außer dem letzten enthalten. Der Slice dafür ist `values[:-1]`. Trag ihn in der Übung ein. Die Funktion weiter oben bleibt falsch, damit du dort den Haltepunkt setzen kannst. Das Ergebnis ist `2.0`.

# gegeben:
sample = [1.0, 2.0, 3.0, 4.0]

# lösung ab hier:
def mean_without_ends(values):
    chosen =
    return sum(chosen) / len(chosen)


print("exercise", mean_without_ends(sample))

# Lösung
#
# Die Funktion oben bleibt für den Debugger falsch, bis du den Slice änderst. Die Lösung zeigt die korrigierte Rechnung unter einem zweiten Namen.

def mean_without_last(values):
    """Return the mean of every value except the last one."""
    chosen = values[:-1]
    return sum(chosen) / len(chosen)

sample = [1.0, 2.0, 3.0, 4.0]
print("solution", mean_without_last(sample))

# Weiter mit `tag4/18_doctest.ipynb`.
