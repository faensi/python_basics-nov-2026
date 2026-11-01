# Listen, Tupel und Slicing

**Tag 1, Einheit 03**  
**Skript:** `tag1/03_listen_tupel_slicing.py`

## Ziel

Sie legen eine Messreihe in einer Liste ab, einen kurzen festen Datensatz in einem Tupel, und Sie schneiden mit einem Slice einen Abschnitt heraus.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `middle_readings` und `last_three` ergänzen.
4. In der Konsole `check_slices()` aufrufen.

## Liste

Eine Liste hält Werte in einer Reihenfolge. Sie darf wachsen. `append` hängt einen Wert hinten an.

```python
readings = [19.8, 20.1, 19.9, 20.0, 20.2]
readings.append(20.3)
```

Der Index beginnt bei 0. `readings[0]` ist der erste Wert, `readings[-1]` der letzte.

## Tupel

Ein Tupel ist eine feste Folge. Es passt zu einem kurzen Datensatz, der sich nicht mehr verändern soll, etwa Anfang und Ende einer Reihe. Ein Tupel hat kein `append`.

```python
start_end = (19.8, 20.2)
start, end = start_end
```

Die zweite Zeile legt die beiden Werte auf zwei Namen. Das nennt man Entpacken.

## Slicing

Ein Slice schreibt Start, Stopp und optional eine Schrittweite in eckige Klammern: `werte[start:stopp]`. Der Start gehört dazu, der Stopp nicht. Weggelassene Grenzen reichen bis zum Anfang oder bis zum Ende.

| Ausdruck | Bedeutung |
| --- | --- |
| `readings[1:4]` | vom zweiten bis vor den fünften Wert |
| `readings[:3]` | die ersten drei Werte |
| `readings[-2:]` | die letzten zwei Werte |
| `readings[::2]` | jeder zweite Wert |

Ein Slice einer Liste ist eine neue Liste. Wenn Sie an diese neue Liste etwas anhängen, bleibt die ursprüngliche Liste unverändert. Das Skript zeigt das am Präfix.

## Übung

Die Reihe im Check ist `[19.8, 20.1, 19.9, 20.0, 20.2]`.

- `middle_readings` liefert die Reihe ohne den ersten und ohne den letzten Wert: `[20.1, 19.9, 20.0]`.
- `last_three` liefert die letzten drei Werte: `[19.9, 20.0, 20.2]`.

## Lösung

```python
def solution_middle_readings(values):
    return values[1:-1]

def solution_last_three(values):
    return values[-3:]
```

Weiter mit `tag1/04_strings_und_sortierung.md`.
