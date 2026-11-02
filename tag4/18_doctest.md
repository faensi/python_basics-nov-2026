# Systematisches Testen und `doctest`

**Tag 4, Einheit 18**  
**Skript:** `tag4/18_doctest.py`

## Ziel

In dieser Einheit formulierst du zu einer Funktion konkrete Beispiele und lässt das Modul `doctest` diese Beispiele aus dem Docstring ausführen.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen. Die Zeile `doctest: ... tests, 0 failures` meldet den Erfolg.
3. Lies die Docstrings von `mean`, `format_deviation` und `within_tolerance`.
4. Optional im Terminal, aus dem Ordner `python_basics-nov-2026`:

```bash
python -m doctest tag4/18_doctest.py
```

Ohne Befund ist die Ausgabe leer. Das ist der Erfolg. F5 im Skript zählt die Beispiele zusätzlich laut.

## Was systematisches Testen hier heißt

Ein Test nennt eine Eingabe und das erwartete Ergebnis, bevor du den Lauf bewertest. Für eine kleine reine Funktion reichen drei Lagen:

- der übliche Fall, zum Beispiel zwei Temperaturen
- der Rand, zum Beispiel eine einzelne Temperatur oder die Abweichung 0
- die Grenze einer Toleranz, einmal noch innerhalb und einmal außerhalb

Schlägt ein Beispiel fehl, prüfe zuerst die Funktion. Das erwartete Ergebnis änderst du nur, wenn es selbst falsch war. Ein Test, den du an den Fehler anpasst, prüft nichts mehr.

`doctest` und `unittest` gehören zur Standardbibliothek. Sie stehen nicht in `environment.yml`.

## Was `doctest` vergleicht

Im Docstring steht ein Aufruf wie in der Konsole, mit `>>>`. Die nächste Zeile ist die erwartete Darstellung des Ergebnisses. Leerzeichen zählen. `'+1.0'` und `'+1.00'` sind nicht dasselbe.

Eine erwartete Ausnahme schreibst du so:

```text
>>> mean([])
Traceback (most recent call last):
...
ValueError: values must not be empty
```

Die Zeile `...` steht für den übrigen Traceback. `doctest` prüft danach den Fehlertyp und die Meldung.

## Die Beispiele in dieser Datei

`mean([20.0, 22.0])` ist 21,0. Eine einzelne Zahl ist ihr eigener Mittelwert. Eine leere Reihe löst `ValueError` aus.

`format_deviation` formatiert die Differenz mit Vorzeichen und einer Nachkommastelle. 21,0 gegen 20,0 ergibt den Text `+1.0`, 19,0 gegen 20,0 den Text `-1.0`.

`within_tolerance(20.4, 20.0, 0.5)` ist wahr, `within_tolerance(20.5, 20.0, 0.5)` ist ebenfalls wahr, weil die Grenze dazugehört, und `within_tolerance(20.6, 20.0, 0.5)` ist falsch.

## Übung

Der Nullfall für die formatierte Abweichung ist das dritte Beispiel in `format_deviation`: gleiche Anzeige und Referenz ergeben `'+0.0'`. Lies es als Muster, wenn du später ein eigenes Beispiel ergänzt. Ein zusätzliches Beispiel kommt direkt unter die vorhandenen `>>>`-Zeilen, mit der erwarteten Ausgabe in der nächsten Zeile. F5 muss danach bei 0 Fehlern bleiben.

## Lösung

Der Nullfall steht bereits im Docstring:

```python
>>> format_deviation(20.0, 20.0)
'+0.0'
```

Die Funktion rundet die Differenz auf eine Stelle und formatiert sie mit `"{:+.1f}".format(...)`.

Weiter mit `tag4/19_unittest.md`.
