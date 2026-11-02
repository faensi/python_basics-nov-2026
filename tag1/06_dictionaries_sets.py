# Dictionaries, Sets und Frozensets
#
# Tag 1, Einheit 06
# Skript: `tag1/06_dictionaries_sets.py`
#
# Ziel
#
# Du ordnest einem Sensornamen eine Temperatur zu und bildest die Menge der vorkommenden Namen ohne Doppelte.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Dictionary
#
# Ein Dictionary speichert Paare aus Schlüssel und Wert. Der Sensorname ist der Schlüssel, die Temperatur der Wert. `readings["probe"] = 18.7` trägt ein weiteres Paar ein. `readings["bath"]` liest einen Wert.
#
# `sorted(readings)` liefert die Schlüssel als sortierte Liste. Die Sortierung brauchst du für eine stabile Anzeige. Ein Dictionary garantiert dir keine bestimmte Druckreihenfolge als Teil der Aufgabe. `items()` liefert die Paare.
#
# Ein Zugriff auf einen fehlenden Schlüssel bricht ab. Frage nur Schlüssel ab, die du eingetragen hast.

# Set und Frozenset
#
# Ein Set enthält jeden Wert höchstens einmal. Aus `["bath", "room", "bath", "bath"]` wird die Menge mit `bath` und `room`. Die Menge hat keine Position. `"bath" in unique` prüft die Mitgliedschaft.
#
# Ein Frozenset ist eine Menge, die du danach nicht mehr änderst. Es hat kein `add`. Zwei Mengen mit denselben Elementen sind gleich, auch wenn die Elemente in unterschiedlicher Reihenfolge hineingekommen sind.

readings = {"bath": 20.1, "room": 21.5}
readings["probe"] = 18.7
print("bath", readings["bath"])
print("keys", sorted(readings))
print("values", sorted(readings.values()))
print("items", sorted(readings.items()))
names = ["bath", "room", "bath", "bath"]
unique = set(names)
frozen = frozenset(names)
print("unique", sorted(unique))
print("bath in frozen", "bath" in frozen)
print("equal contents", unique == set(frozen))

# Übung
#
# Lege ein Dictionary `own` mit mindestens drei Sensornamen und Temperaturen an. Die Namen `bath`, `room` und `probe` nimmst du nicht. Trag danach ein weiteres Paar ein und lies diesen neuen Wert in `stored` aus.
#
# Aus `places` machst du ein Frozenset `once`. Doppelte Namen fallen weg. Das Ergebnis enthält `hall`, `lab` und `store`.

# gegeben:
places = ["hall", "lab", "hall", "store"]

# lösung ab hier:
own =
own[] =
stored =
once =
print("exercise", own, stored)
print("exercise", sorted(once))

# Lösung

places = ["hall", "lab", "hall", "store"]
own = {"hall": 19.2, "lab": 22.0, "office": 21.1}
own["store"] = 17.5
stored = own["store"]
once = frozenset(places)
print("solution", own, stored)
print("solution", sorted(once))

# Weiter mit `tag1/07_konvertierung_referenzen_kopien.ipynb`.
