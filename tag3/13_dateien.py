# Dateien lesen und schreiben
#
# Tag 3, Einheit 13
# Skript: `tag3/13_dateien.py`
#
# Ziel
#
# Du liest das Probenprotokoll und die Messreihe aus `data/` und schreibst einen kurzen Bericht nach `data/report.txt`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Liegt es auf `tag3`, findet Python `data/readings.csv` nicht und meldet `FileNotFoundError`. Skript mit F5, oder die Zellen von oben nach unten.

# Lesen
#
# `open` öffnet eine Datei. `with` schließt sie wieder, auch wenn das Lesen abbricht. `encoding="utf-8"` legt die Zeichencodierung fest.
#
# `data/notes.txt` ist das Probenprotokoll. `data/readings.csv` beginnt mit einer Kopfzeile `timestamp,sensor,celsius`. Danach steht in jeder Zeile ein Zeitpunkt, ein Sensorname und eine Temperatur, getrennt durch Kommas. `split(",")` zerlegt eine Zeile. Die Kopfzeile überspringst du mit einem ersten `readline`. Die Temperatur im Text wandelst du mit `float` um.

# Schreiben
#
# `"w"` legt die Datei neu an und ersetzt einen vorhandenen Inhalt. Jede Berichtszeile endet mit `"\n"`.
#
# `data/report.txt` ist ein Ergebnis, keine Vorlage. Du darfst die Datei löschen. Der nächste Lauf schreibt sie neu.

with open("data/notes.txt", encoding="utf-8") as handle:
    notes = handle.read()
print(notes)
bath = []
with open("data/readings.csv", encoding="utf-8") as handle:
    handle.readline()
    for line in handle:
        if not line.strip():
            continue
        _timestamp, name, celsius = line.strip().split(",")
        if name == "bath":
            bath.append(float(celsius))
print("bath", bath)
lines = []
for celsius in bath:
    lines.append("bath: {:.1f} C".format(celsius))
with open("data/report.txt", "w", encoding="utf-8") as handle:
    for line in lines:
        handle.write(line + "\n")
print("wrote data/report.txt")

# Übung
#
# Lies `data/readings.csv` noch einmal. Sammle die Temperaturen des Sensors `room` in der Liste `room`, in der Reihenfolge der Datei. Es sind fünf Werte, beginnend mit 21,4. Schreibe keine Funktion. Die Datei `data/report.txt` lässt du in dieser Übung unverändert.

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
