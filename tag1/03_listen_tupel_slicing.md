# Listen, Tupel und Slicing

**Tag 1, Einheit 03**
**Skript:** `tag1/03_listen_tupel_slicing.py`

## Ziel

In dieser Einheit legst du eine Messreihe in einer Liste ab, einen kurzen festen Datensatz in einem Tupel, und du schneidest mit einem Slice einen Abschnitt heraus.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Übung am Ende des Skripts ergänzen.
4. Skript erneut mit F5 ausführen.

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
start_end = (19.8, 20.2, 9)
start, end = start_end
```

Die zweite Zeile legt die beiden Werte auf zwei Namen. Das nennt man Entpacken.

## Slicing

Ein Slice schreibt Start, Stopp und optional eine Schrittweite in eckige Klammern: `werte[start:stopp]`. Der Start gehört dazu, der Stopp nicht. Weggelassene Grenzen reichen bis zum Anfang oder bis zum Ende.

| Ausdruck          | Bedeutung                             |
| ----------------- | ------------------------------------- |
| `readings[1:4]` | vom zweiten bis vor den fünften Wert |
| `readings[:3]`  | die ersten drei Werte                 |
| `readings[-2:]` | die letzten zwei Werte                |
| `readings[::2]` | jeder zweite Wert                     |

Ein Slice einer Liste ist eine neue Liste. Wenn du an diese neue Liste etwas anhängst, bleibt die ursprüngliche Liste unverändert. Das Skript zeigt das am Präfix.

## Übung

Schreibe am Ende des Skripts eine eigene Liste mit mindestens vier Temperaturen. Die Reihe `19.8, 20.1, 19.9, 20.0, 20.2` aus dem Text nimmst du nicht. Hänge mit `append` eine weitere Temperatur an. Lege ein Tupel `ends` mit dem ersten und dem letzten Wert an.

Aus `sample` nimmst du den zweiten und den dritten Wert in eine neue Liste. Für diese Reihe ist das `[18.4, 19.1]`.

## Lösung

```python
own = [18.0, 18.5, 17.9, 19.2]
own.append(18.8)
ends = (own[0], own[-1])
second_and_third = sample[1:3]
print(own, ends, second_and_third)
```

Weiter mit `tag1/04_strings_und_sortierung.md`.
