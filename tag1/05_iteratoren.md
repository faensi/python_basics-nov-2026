# Iteratoren und iterierbare Objekte

**Tag 1, Einheit 05**  
**Skript:** `tag1/05_iteratoren.py`

## Ziel

In dieser Einheit unterscheidest du eine Folge, die man durchlaufen kann, von dem Iterator, der die Werte einzeln herausgibt.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. `first_two` ergänzen.
4. In der Konsole `check_first_two()` aufrufen.

## Zwei Rollen

Eine Liste ist **iterierbar**. Man kann sie durchlaufen. Sie ist selbst nicht der Zähler, der die Werte nacheinander aushändigt.

`iter(werte)` erzeugt einen **Iterator**. `next(iterator)` liefert den nächsten Wert. Nach dem letzten Wert ist der Iterator erschöpft. Ein weiterer Aufruf von `next` endet dann mit `StopIteration`. Das Skript ruft `next` nur so oft auf, wie Werte da sind.

Dieselbe Liste kann mehrere Iteratoren haben. Jeder merkt sich seine eigene Position. Die Liste bleibt davon unberührt.

## Zusammenhang mit der for-Schleife

Die Schleife von Tag 2 spricht dieses Protokoll für dich:

```python
for reading in readings:
    print(reading)
```

Sie holt einen Iterator und ruft `next`, bis die Werte ausgehen. Das Skript zeigt eine solche Schleife einmal, damit der Zusammenhang sichtbar ist. Die Formen `while`, `break` und `continue` kommen in Einheit 09.

## Übung

`first_two([18.2, 18.6, 19.0, 19.4])` liefert `(18.2, 18.6)`.

Hole mit `iter` einen Iterator. Lege zwei eigene Variablen an und hole mit `next` den ersten und den zweiten Wert. Gib beide als Tupel zurück. Geh die Liste nicht mit einem Index durch. Die Reihe im Skript, `19.8, 20.1, 19.9`, ist eine andere.

## Lösung

```python
def solution_first_two(values):
    iterator = iter(values)
    first = next(iterator)
    second = next(iterator)
    return first, second
```

Weiter mit `tag1/06_dictionaries_sets.md`.
