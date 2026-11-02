# Dateien lesen und schreiben

**Tag 3, Einheit 13**  
**Skript:** `tag3/13_dateien.py`

## Ziel

In dieser Einheit liest du das Probenprotokoll und die Messreihe aus `data/` und schreibst einen kurzen Bericht nach `data/report.txt`.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`. Liegt es auf `tag3`, findet Python `data/readings.csv` nicht und meldet `FileNotFoundError`.
2. Skript mit F5 ausführen.
3. `load_celsius` und `write_report` ergänzen.
4. In der Konsole `check_files()` aufrufen.

## Lesen

`open` öffnet eine Datei. `with` schließt sie wieder, auch wenn das Lesen abbricht. Den Umgang mit Fehlern im Allgemeinen behandelt dieser Kurs nicht. `with` ist hier nur der sichere Rahmen um eine Datei.

```python
with open(path, encoding="utf-8") as handle:
    text = handle.read()
```

`encoding="utf-8"` legt die Zeichencodierung fest. Die Beispieldateien enthalten nur ASCII-Zeichen, der Parameter bleibt trotzdem gesetzt.

`read_notes("data/notes.txt")` liefert das ganze Protokoll als einen String. Die Pfade sind vom Kursordner aus geschrieben.

## Eine CSV-Datei ohne Zusatzmodul

`data/readings.csv` beginnt mit einer Kopfzeile:

```text
timestamp,sensor,celsius
```

Danach steht in jeder Zeile ein Zeitpunkt, ein Sensorname und eine Temperatur, getrennt durch Kommas. `split(",")` zerlegt eine Zeile. Die Kopfzeile überspringst du mit einem ersten `readline`.

Die Temperatur im Text wandelst du mit `float` um, wie in Einheit 12.

## Schreiben

`"w"` legt die Datei neu an und ersetzt einen vorhandenen Inhalt. Jede Berichtszeile schreibst du mit einem Zeilenende `"\n"`.

`data/report.txt` ist ein Ergebnis des Skripts, keine Vorlage, und du darfst die Datei löschen. Der nächste Lauf schreibt sie neu.

## Übung

- `load_celsius("data/readings.csv", "bath")` liefert die fünf Bad-Temperaturen in der Dateireihenfolge: 19,8, 20,1, 19,9, 20,0 und 20,2 Grad Celsius.
- `write_report("data/report.txt", ["bath: 20.1 C"])` erzeugt eine Datei, deren Inhalt genau `bath: 20.1 C` plus ein Zeilenende ist.

## Lösung

```python
def solution_load_celsius(path, sensor):
    selected = []
    with open(path, encoding="utf-8") as handle:
        handle.readline()
        for line in handle:
            if not line.strip():
                continue
            _timestamp, name, celsius = line.strip().split(",")
            if name == sensor:
                selected.append(float(celsius))
    return selected

def solution_write_report(path, lines):
    with open(path, "w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(line + "\n")
```

Weiter mit `tag3/14_module_und_namensraeume.md`.
