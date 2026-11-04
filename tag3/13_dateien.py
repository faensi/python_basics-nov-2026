# Dateien lesen und schreiben
#
# Tag 3, Einheit 13
# Skript: `tag3/13_dateien.py`
#
# Ziel
#
# Du öffnest Textdateien, liest Zeilen, zerlegst eine einfache CSV-Datei von Hand
# und schreibst einen kurzen Bericht nach `data/report.txt`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Liegt es auf `tag3`, findet Python
# `data/readings.csv` nicht und meldet `FileNotFoundError`. Skript mit F5, oder
# die Zellen von oben nach unten.

# Pfad und Arbeitsverzeichnis
#
# Pfade in diesem Kurs beginnen mit `data/` und gelten vom Kursordner aus.
# Der String `data/notes.txt` ist relativ. Wenn die Datei fehlt, prüfe zuerst
# das Arbeitsverzeichnis.

path = "data/notes.txt"
print(path)
print(type(path))

# `open` und `with`
#
# `open(path, encoding="utf-8")` öffnet eine Datei zum Lesen. Ohne zweiten
# Positionsparameter ist der Modus `r` (read). `with` schließt die Datei wieder.

handle = open("data/notes.txt", encoding="utf-8")
print(handle)
handle.close()

with open("data/notes.txt", encoding="utf-8") as handle:
    print(handle.closed)
print("after with", handle.closed)

# Ganze Datei lesen: `read`

with open("data/notes.txt", encoding="utf-8") as handle:
    notes = handle.read()
print(notes[:80])

print(len(notes))
print(notes.count("\n"))
print("Bad" in notes)

# Zeile für Zeile: `readline` und `for`
#
# `readline()` liest genau eine Zeile. Eine `for`-Schleife über den Handle läuft
# alle restlichen Zeilen ab.

with open("data/notes.txt", encoding="utf-8") as handle:
    first = handle.readline()
print(repr(first))

with open("data/notes.txt", encoding="utf-8") as handle:
    handle.readline()
    second = handle.readline()
print(repr(second))

count = 0
with open("data/notes.txt", encoding="utf-8") as handle:
    for line in handle:
        count = count + 1
print("lines", count)

# Eine Zeile säubern: `strip`

raw = "  bath,20.1\n"
clean = raw.strip()
print(repr(clean))

# CSV von Hand: `split` und `float`
#
# `data/readings.csv` beginnt mit der Kopfzeile `timestamp,sensor,celsius`.
# `split(",")` zerlegt den Text. `float` wandelt die Temperatur um.

line = "2026-03-02T08:00:00,bath,19.94"
parts = line.split(",")
print(parts)

timestamp, name, text_value = parts
celsius = float(text_value)
print(name, celsius)

with open("data/readings.csv", encoding="utf-8") as handle:
    header = handle.readline().strip()
print(header)

# Messwerte sammeln

bath = []
with open("data/readings.csv", encoding="utf-8") as handle:
    handle.readline()
    for line in handle:
        if not line.strip():
            continue
        _timestamp, name, text_value = line.strip().split(",")
        if name == "bath":
            bath.append(float(text_value))
print("bath count", len(bath))
print("bath first", bath[0])
print("bath last", bath[-1])

# Schreiben: Modus `w`
#
# `open(path, "w", encoding="utf-8")` legt die Datei neu an. `write` schreibt Text.
# `data/report.txt` ist ein Ergebnis, keine Vorlage.

path = "data/report.txt"
text = "bath: 20.0 C\n"
print(repr(text))

with open("data/report.txt", "w", encoding="utf-8") as handle:
    handle.write("bath: 20.0 C\n")
print("wrote one line")

with open("data/report.txt", encoding="utf-8") as handle:
    print(handle.read())

# Bericht aus der Liste

line = "bath: {:.1f} C".format(19.94)
print(line)
print(repr(line + "\n"))

lines = []
for celsius in bath[:3]:
    lines.append("bath: {:.1f} C".format(celsius))
print(lines)

with open("data/report.txt", "w", encoding="utf-8") as handle:
    for line in lines:
        handle.write(line + "\n")
print("wrote data/report.txt")

# Alles in einem Durchgang

with open("data/notes.txt", encoding="utf-8") as handle:
    notes = handle.read()
print(notes[:60])

bath = []
with open("data/readings.csv", encoding="utf-8") as handle:
    handle.readline()
    for line in handle:
        if not line.strip():
            continue
        _timestamp, name, celsius = line.strip().split(",")
        if name == "bath":
            bath.append(float(celsius))
print("bath", len(bath), bath[0], bath[-1])

lines = []
for celsius in bath:
    lines.append("bath: {:.1f} C".format(celsius))
with open("data/report.txt", "w", encoding="utf-8") as handle:
    for line in lines:
        handle.write(line + "\n")
print("wrote data/report.txt")

# Übung
#
# Lies `data/readings.csv` noch einmal. Sammle die Temperaturen des Sensors `room`
# in der Liste `room`, in der Reihenfolge der Datei. Der erste Wert ist 21,4.
# Die Liste hat so viele Einträge, wie `room`-Zeilen in der Datei stehen.
# Schreibe keine Funktion. Die Datei `data/report.txt` lässt du in dieser Übung
# unverändert.

# gegeben:
path = "data/readings.csv"

# lösung ab hier:
room =
with open(path, encoding="utf-8") as handle:
    handle.readline()
    for line in handle:
        if not line.strip():
            continue
        _timestamp, name, celsius = line.strip().split(",")
        if name == "room":
            room.append()
print("exercise", room)

# Lösung

room = []
with open("data/readings.csv", encoding="utf-8") as handle:
    handle.readline()
    for line in handle:
        if not line.strip():
            continue
        _timestamp, name, celsius = line.strip().split(",")
        if name == "room":
            room.append(float(celsius))
print("solution", room)

# Weiter mit `tag3/14_module_und_namensraeume.ipynb`.
