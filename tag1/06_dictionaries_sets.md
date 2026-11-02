# Dictionaries, Sets und Frozensets

**Tag 1, Einheit 06**  
**Skript:** `tag1/06_dictionaries_sets.py`

## Ziel

In dieser Einheit ordnest du einem Sensornamen eine Temperatur zu und bildest die Menge der vorkommenden Namen ohne Doppelte.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. `own_map` und `places_once` ergänzen.
4. In der Konsole `check_mappings()` aufrufen.

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

Lege in `own_map` ein Dictionary mit mindestens drei Sensornamen und Temperaturen an. Die Namen `bath`, `room` und `probe` aus dem Text nimmst du nicht. Trag danach ein weiteres Paar ein, lies genau diesen neuen Wert wieder aus und gib das Dictionary und diesen Wert zurück.

`places_once(["hall", "lab", "hall", "store"])` liefert `frozenset({"hall", "lab", "store"})`. Doppelte Namen fallen weg.

## Lösung

```python
def solution_own_map():
    readings = {"hall": 19.2, "lab": 22.0, "office": 21.1}
    readings["store"] = 17.5
    stored = readings["store"]
    return readings, stored

def solution_places_once(names):
    return frozenset(names)
```

`check_mappings()` lässt andere Namen und Temperaturen zu, solange die Namen aus dem Text nicht vorkommen und der zurückgegebene Wert im Dictionary steht. Die Menge muss ein Frozenset sein.

Weiter mit `tag1/07_konvertierung_referenzen_kopien.md`.
