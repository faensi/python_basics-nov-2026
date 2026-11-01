# Debugging in Spyder

**Tag 4, Einheit 17**  
**Skript:** `tag4/17_debugging.py`

## Ziel

Sie setzen einen Haltepunkt, starten den Debugger und lesen den falschen Zwischenwert im Variablenexplorer.

## Ablauf

1. Arbeitsverzeichnis: `this_course`.
2. Lesen Sie die Funktion `mean_without_ends`, bevor Sie sie ändern.
3. Setzen Sie einen Haltepunkt in die Zeile mit `return`. Klicken Sie links neben die Zeilennummer. Ein Haltepunkt markiert diese Zeile.
4. Starten Sie über das Menü **Debug** den Eintrag **Debug**. Die Tastenkombination ist in vielen Spyder-Versionen Strg+F5 beziehungsweise Ctrl+F5.
5. Gehen Sie mit **Step** einen Schritt. Im Variablenexplorer erscheint `chosen`.
6. Vergleichen Sie `chosen` mit der Reihe. Beenden Sie den Lauf mit **Continue**.
7. Korrigieren Sie den Slice, führen Sie die Datei mit F5 aus und rufen Sie `check_mean_without_ends()` auf.

Wenn im Variablenexplorer noch Werte aus einem früheren Lauf stehen, starten Sie die IPython-Konsole neu und debuggen Sie erneut.

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
