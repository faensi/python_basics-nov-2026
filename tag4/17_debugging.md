# Debugging in Spyder

**Tag 4, Einheit 17**  
**Skript:** `tag4/17_debugging.py`

## Ziel

In dieser Einheit setzt du einen Haltepunkt, startest den Debugger und liest den falschen Zwischenwert im Variablenexplorer.

## Ablauf

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Lies die Funktion `mean_without_ends`, bevor du sie änderst.
3. Setze einen Haltepunkt in die Zeile mit `return`. Klicke links neben die Zeilennummer. Ein Haltepunkt markiert diese Zeile.
4. Starte über das Menü **Debug** den Eintrag **Debug**. Die Tastenkombination ist in vielen Spyder-Versionen Strg+F5 beziehungsweise Ctrl+F5.
5. Geh mit **Step** einen Schritt. Im Variablenexplorer erscheint `chosen`.
6. Vergleiche `chosen` mit der Reihe. Beende den Lauf mit **Continue**.
7. Korrigiere den Slice, führe die Datei mit F5 aus und rufe `check_mean_without_ends()` auf.

Wenn im Variablenexplorer noch Werte aus einem früheren Lauf stehen, starte die IPython-Konsole neu und debugge erneut.

## Der Fehler

Die Reihe ist `[1.0, 2.0, 3.0, 4.0]`. Der Mittelwert ohne den letzten Wert ist der Mittelwert von 1, 2 und 3, also 2,0.

Die Funktion schneidet stattdessen den ersten Wert ab:

```python
chosen = values[1:]
```

Der Mittelwert von 2, 3 und 4 ist 3,0. F5 druckt dieses falsche Ergebnis und danach den erwarteten Wert 2,0. Der erwartete Wert steht auch in `solution_mean_without_ends`. Der Fehler ist kein Abbruch, sondern ein falsches Ergebnis. Genau dafür ist der Haltepunkt da: das Skript läuft, und ein Name hat den falschen Inhalt.

## Übung

`chosen` soll alle Werte außer dem letzten enthalten. Der Slice dafür ist `values[:-1]`.

Vor der Korrektur druckt `check_mean_without_ends()` die Zeile `expected 2.0 got 3.0`. Nach der Korrektur druckt der Check `ok`.

## Lösung

```python
def solution_mean_without_ends(values):
    chosen = values[:-1]
    return sum(chosen) / len(chosen)
```

Weiter mit `tag4/18_doctest.md`.
