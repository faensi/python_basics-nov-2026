# Eigene Module, Dokumentation und Hilfe

**Tag 3, Einheit 15**  
**Skript:** `tag3/15_eigene_module.py`  
**Modul:** `tag3/measurement.py`

## Ziel

Sie lagern Funktionen in eine eigene Datei aus, importieren sie und lesen die Hilfe aus dem Docstring.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Öffnen Sie zuerst `measurement.py`, dann das Skript der Einheit.
3. Skript mit F5 ausführen.
4. `summary` ergänzen.
5. In der Konsole `check_summary()` aufrufen.
6. Optional: `help(measurement.mean)` und die Ansicht mit `q` verlassen.

## Warum eine zweite Datei

`measurement.py` enthält den Mittelwert, die Abweichung, die Toleranzprüfung und die Umrechnung von Grad Celsius nach Kelvin. Das sind dieselben Rechnungen wie an den vorigen Tagen, jetzt an einem Ort, den mehrere Skripte nutzen können.

Die Datei liegt neben `15_eigene_module.py`. Wenn Sie das Skript mit F5 starten, findet `import measurement` diese Datei, weil Spyder den Ordner des Skripts durchsucht. Ein `import measurement` in einer beliebigen anderen Konsole ohne diesen Ordner findet die Datei nicht.

## Docstring

Der englische Text unter `def mean` ist der Docstring. Er beschreibt, was die Funktion leistet, nicht jede Zeile im Körper. `measurement.mean.__doc__` gibt ihn aus. Das Skript druckt ihn bei F5.

Docstrings in diesem Kurs sind Englisch, wie die übrigen Programmnamen. Der Erklärungstext für Sie bleibt in dieser Markdown-Datei.

## Übung

`summary(values, reference, tolerance)` liefert ein Dictionary mit zwei Schlüsseln:

- `"mean"`: `measurement.mean(values)`
- `"within"`: ob dieser Mittelwert innerhalb der Toleranz um `reference` liegt, geprüft mit `measurement.within_tolerance`

`check_summary()` erwartet für `[20.0, 21.0, 22.0]`, Referenz 21,0 und Toleranz 0,5:

```python
{"mean": 21.0, "within": True}
```

## Lösung

```python
def solution_summary(values, reference, tolerance):
    average = measurement.mean(values)
    return {
        "mean": average,
        "within": measurement.within_tolerance(average, reference, tolerance),
    }
```

Weiter mit `tag4/16_klassen.md`. Die Zusammenfassung des Tages steht in `Tag3_Zusammenfassung.md`.
