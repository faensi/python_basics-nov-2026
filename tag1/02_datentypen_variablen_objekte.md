# Datentypen, Klassen, Variablen, Objekte

**Tag 1, Einheit 02**  
**Skript:** `tag1/02_datentypen_variablen_objekte.py`

## Ziel

Sie unterscheiden Zahl, Text, Wahrheitswert und den leeren Wert `None`. Sie können einen Namen an einen Wert binden und denselben Namen später an einen anderen Wert binden.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. Funktion `describe` ergänzen.
4. In der Konsole `check_describe()` aufrufen.

Schauen Sie danach in den Variablenexplorer. Dort stehen die Namen aus dem Skript, sobald es gelaufen ist.

## Vier Begriffe

Ein **Objekt** ist ein Wert im Speicher, zum Beispiel die Zahl 20,1 oder der Text `bath`.

Der **Datentyp** sagt, was Sie mit dem Objekt tun dürfen. Eine Temperatur in Grad Celsius ist hier eine Gleitkommazahl, eine Anzahl eine ganze Zahl, ein Sensorname ein Text.

Die **Klasse** ist das Bauteil, das solche Objekte erzeugt. `type(20.1)` liefert die Klasse `float`. Jeder Wert ist ein Objekt einer Klasse. Eigene Klassen schreiben Sie am Tag 4. Heute reichen die eingebauten Klassen.

Eine **Variable** ist ein Name, der auf ein Objekt zeigt. Der Name steht links, der Wert rechts:

```python
celsius = 20.1
```

## Die Werte im Skript

| Wert im Skript | Klasse | Rolle in der Messung |
| --- | --- | --- |
| `3` | `int` | Anzahl |
| `20.1` | `float` | Temperatur |
| `"bath"` | `str` | Name des Sensors |
| `True` | `bool` | Ja-oder-nein-Kennzeichen |
| `None` | `NoneType` | noch kein Wert vorhanden |

`True` und `False` sind eigene Werte. `None` bedeutet nicht die Zahl 0 und nicht den leeren Text. Es bedeutet: hier liegt nichts.

## Namen neu binden

```python
earlier = celsius
celsius = 21.0
```

`earlier` zeigt weiter auf 20,1. Nur der Name `celsius` zeigt danach auf 21,0. Sie haben das erste Objekt nicht verändert, sondern einen Namen umgehängt.

Derselbe Name darf danach auf ein Objekt einer anderen Klasse zeigen. Das Skript bindet `value` erst an eine Zahl und dann an einen Text. In C oder Java wäre das eine andere, fest deklarierte Variable.

## Übung

`describe` soll den Namen der Klasse als Text liefern. Erwartet wird:

| Aufruf | Ergebnis |
| --- | --- |
| `describe(20.1)` | `"float"` |
| `describe(3)` | `"int"` |
| `describe("bath")` | `"str"` |
| `describe(True)` | `"bool"` |
| `describe(None)` | `"NoneType"` |

`type(value).__name__` ist dieser Name.

## Lösung

```python
def solution_describe(value):
    return type(value).__name__
```

Weiter mit `tag1/03_listen_tupel_slicing.md`.
