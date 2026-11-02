# Dictionaries, Sets und Frozensets

**Tag 1, Einheit 06**  
**Skript:** `tag1/06_dictionaries_sets.py`

## Ziel

In dieser Einheit ordnest du einem Sensornamen eine Temperatur zu und bildest die Menge der vorkommenden Namen ohne Doppelte.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Übung am Ende des Skripts ergänzen.
4. Skript erneut mit F5 ausführen.

## Dictionary

Ein Dictionary speichert Paare aus Schlüssel und Wert. Der Sensorname ist der Schlüssel, die Temperatur der Wert.

```python
readings = {"bath": 20.1, "room": 21.5}
readings["probe"] = 18.7
readings["bath"]
```

Schlüssel in diesem Kurs sind Texte. `sorted(readings)` liefert die Schlüssel als sortierte Liste. Die Sortierung brauchst du nur für eine stabile Anzeige: ein Dictionary garantiert dir keine bestimmte Druckreihenfolge als Teil der Aufgabe.

`items()` liefert die Paare. Daraus wird in Einheit 07 wieder ein Dictionary.

Ein Zugriff auf einen fehlenden Schlüssel bricht ab. Frage nur Schlüssel ab, die du eingetragen hast.

## Set und Frozenset

Ein Set enthält jeden Wert höchstens einmal. Aus `["bath", "room", "bath", "bath"]` wird die Menge mit `bath` und `room`. Die Menge hat keine Position. `"bath" in unique` prüft die Mitgliedschaft.

Ein Frozenset ist eine Menge, die du danach nicht mehr änderst. Es hat kein `add`. Es eignet sich als festes Ergebnis, das der Aufrufer nicht versehentlich erweitert.

Zwei Mengen mit denselben Elementen sind gleich, auch wenn die Elemente in unterschiedlicher Reihenfolge hineingekommen sind.

## Übung

Lege ein Dictionary mit mindestens drei Sensornamen und Temperaturen an. Die Namen `bath`, `room` und `probe` aus dem Text nimmst du nicht. Trag danach ein weiteres Paar ein und lies diesen neuen Wert wieder aus.

Aus `places` machst du ein Frozenset. Doppelte Namen fallen weg. Das Ergebnis enthält `hall`, `lab` und `store`.

## Lösung

```python
own = {"hall": 19.2, "lab": 22.0, "office": 21.1}
own["store"] = 17.5
stored = own["store"]
once = frozenset(places)
print(own, stored)
print(once)
```

Weiter mit `tag1/07_konvertierung_referenzen_kopien.md`.
