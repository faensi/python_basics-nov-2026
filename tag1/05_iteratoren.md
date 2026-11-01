# Iteratoren und iterierbare Objekte

**Tag 1, Einheit 05**  
**Skript:** `tag1/05_iteratoren.py`

## Ziel

Sie unterscheiden eine Folge, die man durchlaufen kann, von dem Iterator, der die Werte einzeln herausgibt.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `first_value` ergänzen.
4. In der Konsole `check_first_value()` aufrufen.

## Zwei Rollen

Eine Liste ist **iterierbar**. Man kann sie durchlaufen. Sie ist selbst nicht der Zähler, der die Werte nacheinander aushändigt.

`iter(werte)` erzeugt einen **Iterator**. `next(iterator)` liefert den nächsten Wert. Nach dem letzten Wert ist der Iterator erschöpft. Ein weiterer Aufruf von `next` endet dann mit `StopIteration`. Das Skript ruft `next` nur so oft auf, wie Werte da sind.

Dieselbe Liste kann mehrere Iteratoren haben. Jeder merkt sich seine eigene Position. Die Liste bleibt davon unberührt.

## Zusammenhang mit der for-Schleife

Die Schleife von Tag 2 spricht dieses Protokoll für Sie:

```python
for reading in readings:
    print(reading)
```

Sie holt einen Iterator und ruft `next`, bis die Werte ausgehen. Das Skript zeigt eine solche Schleife einmal, damit der Zusammenhang sichtbar ist. Die Formen `while`, `break` und `continue` kommen in Einheit 09.

## Übung

`first_value([19.8, 20.1, 19.9])` soll `19.8` liefern. Holen Sie mit `iter` einen Iterator und mit genau einem `next` den ersten Wert. Gehen Sie die Liste nicht von Hand mit einem Index durch.

## Lösung

```python
def solution_first_value(values):
    iterator = iter(values)
    return next(iterator)
```

Weiter mit `tag1/06_dictionaries_sets.md`.
