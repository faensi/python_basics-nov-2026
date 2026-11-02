# Datentypen, Klassen, Variablen, Objekte

**Tag 1, Einheit 02**
**Skript:** `tag1/02_datentypen_variablen_objekte.py`

## Ziel

In dieser Einheit unterscheidest du Zahl, Text, Wahrheitswert und den leeren Wert `None` und kannst einen Namen an einen Wert binden und denselben Namen später an einen anderen Wert binden.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Funktion `own_binding` ergänzen.
4. In der Konsole `check_own_binding()` aufrufen.

Schau danach in den Variablenexplorer. Dort stehen die Namen aus dem Skript, sobald es gelaufen ist.

## Vier Begriffe

Ein **Objekt** ist ein Wert im Speicher, zum Beispiel die Zahl 20,1 oder der Text `bath`.

Der **Datentyp** sagt, was du mit dem Objekt tun darfst. Eine Temperatur in Grad Celsius ist hier eine Gleitkommazahl, eine Anzahl eine ganze Zahl, ein Sensorname ein Text.

Die **Klasse** ist das Bauteil, das solche Objekte erzeugt. `type(20.1)` liefert die Klasse `float`. Jeder Wert ist ein Objekt einer Klasse. Eigene Klassen schreibst du am Tag 4. Heute reichen die eingebauten Klassen.

Eine **Variable** ist ein Name, der auf ein Objekt zeigt. Der Name steht links, der Wert rechts:

```python
celsius = 20.1
```

## Die Werte im Skript

| Wert im Skript | Klasse       | Rolle in der Messung     |
| -------------- | ------------ | ------------------------ |
| `3`          | `int`      | Anzahl                   |
| `20.1`       | `float`    | Temperatur               |
| `"bath"`     | `str`      | Name des Sensors         |
| `True`       | `bool`     | Ja-oder-nein-Kennzeichen |
| `None`       | `NoneType` | noch kein Wert vorhanden |

`True` und `False` sind eigene Werte. `None` bedeutet nicht die Zahl 0 und nicht den leeren Text. Es bedeutet: hier liegt nichts.

## Namen neu binden

```python
earlier = celsius
celsius = 21.0
```

`earlier` zeigt weiter auf 20,1. Nur der Name `celsius` zeigt danach auf 21,0, und du hast das erste Objekt nicht verändert, sondern einen Namen umgehängt.

Derselbe Name darf danach auf ein Objekt einer anderen Klasse zeigen. Das Skript bindet `value` erst an eine Zahl und dann an einen Text. In C oder Java wäre das eine andere, fest deklarierte Variable.

## Übung

Lege in `own_binding` eigene Namen an. Die Werte aus dem Skript, also `3`, `20.1` und `"bath"`, übernimmst du nicht.

- `count` ist eine ganze Zahl, aber nicht 3.
- `celsius` ist eine Temperatur mit Nachkommastelle, aber nicht 20,1.
- `label` ist ein Text, aber nicht `bath`.
- `valid` ist ein Wahrheitswert, also `True` oder `False`.
- `missing` ist der leere Wert `None`.

Merke dir danach die Temperatur unter dem Namen `earlier` und hänge `celsius` auf eine andere Temperatur um. Die beiden Temperaturen sind verschieden.

Gib in dieser Reihenfolge zurück: `label`, `count`, `earlier`, `celsius`, `valid`, `missing`.

## Lösung

```python
def solution_own_binding():
    count = 5
    celsius = 18.4
    label = "hall"
    valid = False
    missing = None
    earlier = celsius
    celsius = 19.0
    return label, count, earlier, celsius, valid, missing
```

`check_own_binding()` prüft die Arten der Werte und dass die beiden Temperaturen verschieden sind. Andere passende Werte sind ebenfalls richtig.

Weiter mit `tag1/03_listen_tupel_slicing.md`.
