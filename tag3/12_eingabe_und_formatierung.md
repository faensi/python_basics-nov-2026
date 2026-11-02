# Eingabe und formatierte Ausgabe

**Tag 3, Einheit 12**  
**Skript:** `tag3/12_eingabe_und_formatierung.py`

## Ziel

In dieser Einheit liest du eine Eingabe als Text, wandelst sie in eine Zahl und formatierst eine Zeile auf zwei Wegen: mit dem Prozentoperator und mit der Methode `format`.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen. F5 fragt nichts ab.
3. `format_line`, `format_line_method` und `parse_reading` ergänzen.
4. In der Konsole `check_formatting()` aufrufen.
5. Wenn du eine echte Eingabe sehen willst: in der Konsole `demo_input()` aufrufen, in die Konsole klicken und eine Zahl tippen.

## `input`

`input` liest eine Zeile von der Tastatur und gibt sie als String zurück. Die Frage erscheint in der IPython-Konsole, nicht im Editor. Wirkt das Skript angehalten, liegt der Fokus oft noch im Editor.

In Python 2 hieß die Funktion für eine Textzeile `raw_input`. In Python 3 heißt sie `input`. `raw_input` gibt es hier nicht.

Weil F5 in diesem Kurs ohne Tastatur durchlaufen soll, steht die Abfrage in `demo_input` und wird von `main` nicht aufgerufen.

## Zwei Formatierungen

Dieselbe Zeile, eine Nachkommastelle:

```python
"%s: %.1f C" % (sensor, celsius)
"{}: {:.1f} C".format(sensor, celsius)
```

`%s` und `{}` stehen für den Sensornamen, `%.1f` und `{:.1f}` für die Temperatur mit einer Nachkommastelle. Für den Sensor `bath` und 20,1 Grad Celsius entsteht der Text `bath: 20.1 C`.

Im Python-Text bleibt der Punkt das Dezimalzeichen. Im deutschen Satz schreibst du das Komma.

Eine neuere Schreibweise sind f-Strings, etwa `f"{sensor}: {celsius:.1f} C"`. Die Aufgaben dieser Einheit bleiben beim Prozentoperator und bei `format`, weil das die beiden verlangten Wege sind.

## Übung

- `format_line("bath", 20.0)` liefert `"bath: 20.0 C"` mit dem Prozentoperator.
- `format_line_method("bath", 20.0)` liefert denselben Text mit `format`.
- `parse_reading(" 20.5 ")` liefert die Zahl `20.5`. Entferne äußere Leerzeichen und rufe `float` auf.

## Lösung

```python
def solution_format_line(sensor, celsius):
    return "%s: %.1f C" % (sensor, celsius)

def solution_format_line_method(sensor, celsius):
    return "{}: {:.1f} C".format(sensor, celsius)

def solution_parse_reading(text):
    return float(text.strip())
```

Weiter mit `tag3/13_dateien.md`.
