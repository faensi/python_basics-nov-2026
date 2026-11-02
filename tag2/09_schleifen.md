# Schleifen

**Tag 2, Einheit 09**  
**Skript:** `tag2/09_schleifen.py`

## Ziel

In dieser Einheit schreibst du `while`- und `for`-Schleifen, eine Indexschleife analog zu C und C++, und setzt `continue`, `break`, `else` und `pass` gezielt ein.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. `count_until_above` ergänzen.
4. In der Konsole `check_count_until_above()` aufrufen.

## `while` und `for`

`while` wiederholt, solange die Bedingung gilt, und du musst die Zählvariable selbst erhöhen, sonst endet die Schleife nicht.

`for reading in readings` geht die Werte der Reihe durch. Das ist die Schleife, die in Einheit 05 den Iterator benutzt hat.

## Indexschleife wie in C und C++

In C schreibst du oft:

```c
for (int index = 0; index < n; index++) {
    printf("%d %f\n", index, readings[index]);
}
```

In Python übernimmt `range` die Zählung von 0 bis vor `len(readings)`:

```python
for index in range(len(readings)):
    print(index, readings[index])
```

Wenn du den Index nicht brauchst, ist `for reading in readings` die deutlichere Form.

## `continue`, `break`, `else`, `pass`

- `continue` bricht nur diesen Durchlauf ab und macht mit dem nächsten Wert weiter. Im Skript wird so ein fehlender Wert `None` übersprungen.
- `break` verlässt die Schleife ganz.
- `else` an einer Schleife läuft, wenn die Schleife **nicht** mit `break` verlassen wurde. Es ist kein Ersatz für `else` an `if`.
- `pass` ist eine leere Anweisung. Sie hält den Platz, solange ein Zweig noch keinen Code hat. Das Skript benutzt `pass` für negative Werte, die in der Reihe nicht vorkommen.

## Übung

`count_until_above([20.0, 20.2, 21.0, 19.0], 20.5)` zählt die führenden Werte, die höchstens 20,5 sind, und hört beim ersten größeren Wert auf. Der letzte Wert 19,0 wird nicht mehr gezählt, weil die Schleife bei 21,0 endet. Das Ergebnis ist `2`.

## Lösung

```python
def solution_count_until_above(values, limit):
    count = 0
    for value in values:
        if value > limit:
            break
        count = count + 1
    return count
```

Weiter mit `tag2/10_funktionen.md`.
