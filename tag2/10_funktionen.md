# Funktionen: Definition und Aufruf

**Tag 2, Einheit 10**  
**Skript:** `tag2/10_funktionen.py`

## Ziel

In dieser Einheit definierst du eine Funktion, rufst sie auf und gibst mit `return` einen Wert zurück. Außerdem weißt du, dass eine Funktion ohne `return` das Objekt `None` liefert.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. `mean` ergänzen.
4. In der Konsole `check_mean()` aufrufen.

## Form

`def` leitet die Definition ein. Der eingerückte Block ist der Körper. Ein Aufruf schreibt die Argumente in die Klammern.

```python
def announce(sensor):
    print("sensor", sensor)

result = announce("bath")
```

`announce` hat kein `return`. `result` ist deshalb `None`. Eine Berechnung, deren Ergebnis du weiterverwenden willst, braucht `return`.

Die mittlere Temperatur einer Reihe ist die Summe geteilt durch die Anzahl:

```python
average = sum(readings) / len(readings)
```

`sum` und `len` sind eingebaute Funktionen. Für `[20.0, 21.0, 22.0]` ist der Mittelwert 21,0.

## Übung

Schreibe `mean(values)` mit dieser Rechnung.

`check_mean()` erwartet `mean([20.0, 21.0, 22.0]) == 21.0`.

Die Lösung im Skript weist eine leere Reihe zusätzlich ab, mit `raise ValueError`. `check_mean` prüft diesen Fall nicht. Leere Reihen sind kein gültiger Mittelwert, weil die Anzahl 0 wäre.

## Lösung

```python
def solution_mean(values):
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
```

Weiter mit `tag2/11_parameter_und_sichtbarkeit.md`.
