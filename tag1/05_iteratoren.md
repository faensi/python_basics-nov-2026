
# Iteratoren und iterierbare Objekte

**Tag 1, Einheit 05**
**Skript:** `tag1/05_iteratoren.py`

## Ziel

In dieser Einheit unterscheidest du eine Folge, die man durchlaufen kann, von dem Iterator, der die Werte einzeln herausgibt.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Übung am Ende des Skripts ergänzen.
4. Skript erneut mit F5 ausführen.

## Zwei Rollen

Eine Liste ist **iterierbar**. Man kann sie durchlaufen. Sie ist selbst nicht der Zähler, der die Werte nacheinander aushändigt.

`iter(werte)` erzeugt einen **Iterator**. `next(iterator)` liefert den nächsten Wert. Nach dem letzten Wert ist der Iterator erschöpft. Ein weiterer Aufruf von `next` endet dann mit `StopIteration`. Das Skript ruft `next` nur so oft auf, wie Werte da sind.

Dieselbe Liste kann mehrere Iteratoren haben. Jeder merkt sich seine eigene Position. Die Liste bleibt davon unberührt.

## Zusammenhang mit der for-Schleife

Die Schleife von Tag 2 spricht dieses Protokoll für dich:

```python
readings=[1,2,3,5,6,7,8,1,3,6,8]

for reading in readings:
    print(reading)
```

Sie holt einen Iterator und ruft `next`, bis die Werte ausgehen. Das Skript zeigt eine solche Schleife einmal, damit der Zusammenhang sichtbar ist. Die Formen `while`, `break` und `continue` kommen in Einheit 09.

## Übung

Hole aus `series` den ersten und den zweiten Wert. Lege mit `iter` einen Iterator an und hole die beiden Werte mit `next` in eigene Variablen. Geh die Liste nicht mit einem Index durch. Das Ergebnis ist `18.2` und `18.6`.

## Lösung

```python
iterator = iter(series)
first = next(iterator)
second = next(iterator)
print(first, second)
```

Weiter mit `tag1/06_dictionaries_sets.md`.
