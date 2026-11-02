# Listen, Tupel und Slicing

**Tag 1, Einheit 03**  
**Skript:** `tag1/03_listen_tupel_slicing.py`

## Ziel

In dieser Einheit legst du eine Messreihe in einer Liste ab, einen kurzen festen Datensatz in einem Tupel, und du schneidest mit einem Slice einen Abschnitt heraus.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. `own_readings` und `second_and_third` ergänzen.
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

Ein Slice einer Liste ist eine neue Liste. Wenn du an diese neue Liste etwas anhängst, bleibt die ursprüngliche Liste unverändert. Das Skript zeigt das am Präfix.

## Übung

In `own_readings` legst du eine eigene Liste mit mindestens vier Temperaturen an. Die Reihe `19.8, 20.1, 19.9, 20.0, 20.2` aus dem Text nimmst du nicht. Hänge mit `append` eine weitere Temperatur an. Lege ein Tupel `ends` mit dem ersten und dem letzten Wert an. Gib die Liste und das Tupel zurück.

`second_and_third` gibt den zweiten und den dritten Wert als neue Liste zurück. Für `[18.0, 18.4, 19.1, 17.6]` ist das `[18.4, 19.1]`. Das ist ein anderer Schnitt als `[1:4]`, `[:3]`, `[-2:]` und `[::2]` im Text.

## Lösung

```python
def solution_own_readings():
    readings = [18.0, 18.5, 17.9, 19.2]
    readings.append(18.8)
    ends = (readings[0], readings[-1])
    return readings, ends

def solution_second_and_third(values):
    return values[1:3]
```

`check_slices()` lässt bei der eigenen Liste andere passende Zahlen zu. Der Schnitt muss für die genannte Reihe genau diese beiden Werte liefern.

Weiter mit `tag1/04_strings_und_sortierung.md`.
