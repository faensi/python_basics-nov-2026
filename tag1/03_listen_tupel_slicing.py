# Listen, Tupel und Slicing
#
# Tag 1, Einheit 03
# Skript: `tag1/03_listen_tupel_slicing.py`
#
# Ziel
#
# Du legst eine Messreihe in einer Liste ab, einen kurzen festen Datensatz in einem Tupel, und du schneidest mit einem Slice einen Abschnitt heraus.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Liste
#
# Eine Liste hält Werte in einer Reihenfolge. Sie darf wachsen. `append` hängt einen Wert hinten an. Der Index beginnt bei 0. `readings[0]` ist der erste Wert, `readings[-1]` der letzte.

# Tupel
#
# Ein Tupel ist eine feste Folge. Es passt zu einem kurzen Datensatz, der sich nicht mehr verändern soll. Ein Tupel hat kein `append`.
#
#     start_end = (19.8, 20.2)
#     start, end = start_end
#
# Die zweite Zeile legt die beiden Werte auf zwei Namen. Das nennt man Entpacken.

# Slicing
#
# Ein Slice schreibt Start, Stopp und optional eine Schrittweite in eckige Klammern: `werte[start:stopp]`. Der Start gehört dazu, der Stopp nicht. Weggelassene Grenzen reichen bis zum Anfang oder bis zum Ende.
#
# | Ausdruck | Bedeutung |
# | --- | --- |
# | `readings[1:4]` | vom zweiten bis vor den fünften Wert |
# | `readings[:3]` | die ersten drei Werte |
# | `readings[-2:]` | die letzten zwei Werte |
# | `readings[::2]` | jeder zweite Wert |
#
# Ein Slice einer Liste ist eine neue Liste. Wenn du an diese neue Liste etwas anhängst, bleibt die ursprüngliche Liste unverändert.

readings = [19.8, 20.1, 19.9, 20.0, 20.2]
start_end = (19.8, 20.2)
start, end = start_end
print("start", start, "end", end)
readings.append(20.3)
print("after append", readings)
print("first", readings[0])
print("last", readings[-1])
print("slice 1:4", readings[1:4])
print("prefix", readings[:3])
print("suffix", readings[-2:])
print("every second", readings[::2])
prefix = readings[:3]
prefix.append(0.0)
print("prefix after its own append", prefix)
print("readings unchanged", readings)

# Übung
#
# `sample` ist vorgegeben. Lege eine eigene Liste `own` mit mindestens vier Temperaturen an. Die Reihe `19.8, 20.1, 19.9, 20.0, 20.2` nimmst du nicht. Hänge mit `append` eine weitere Temperatur an. Lege ein Tupel `ends` mit dem ersten und dem letzten Wert von `own` an.
#
# Aus `sample` nimmst du den zweiten und den dritten Wert in `second_and_third`. Für diese Reihe ist das `[18.4, 19.1]`.

# gegeben:
sample = [18.0, 18.4, 19.1, 17.6]

# lösung ab hier:
own =
own.append()
ends =
second_and_third =
print("exercise", own, ends, second_and_third)

# Lösung

sample = [18.0, 18.4, 19.1, 17.6]
own = [18.0, 18.5, 17.9, 19.2]
own.append(18.8)
ends = (own[0], own[-1])
second_and_third = sample[1:3]
print("solution", own, ends, second_and_third)

# Weiter mit `tag1/04_strings_und_sortierung.ipynb`.
