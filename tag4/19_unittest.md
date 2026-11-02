# `unittest`

**Tag 4, Einheit 19**  
**Skript:** `tag4/19_unittest.py`

## Ziel

In dieser Einheit liest du einen Testfall, erkennst einen fehlgeschlagenen Vergleich an der Meldung und lässt die echten Tests für Mittelwert und Toleranz laufen.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. Lies zuerst die Beispielmeldung, dann die Klassen `MeanTests` und `ToleranceTests`.

Im Terminal, aus dem Ordner `this_course`:

```bash
python tag4/19_unittest.py
```

## Aufbau

`unittest.TestCase` sammelt Prüfungen. Jede Methode, deren Name mit `test` beginnt, ist ein Test. `self.assertEqual` verlangt Gleichheit. `self.assertTrue` und `self.assertFalse` verlangen einen Wahrheitswert.

`with self.assertRaises(ValueError)` verlangt, dass der eingerückte Aufruf `ValueError` auslöst. Das `with` ist hier keine Datei, sondern die Prüfung der Testbibliothek: Bleibt die Ausnahme aus, schlägt der Test fehl.

Die Funktionen `mean` und `within_tolerance` sind dieselben Rechnungen wie in `tag3/measurement.py`. Sie stehen in dieser Datei noch einmal, damit der Test ohne Pfadtrick lesbar bleibt.

## Eine absichtliche Fehlermeldung

`FailureSample` vergleicht 1 mit 2. Dieser Test gehört nicht zur Messaufgabe. F5 führt ihn getrennt aus und druckt die Meldung, ohne den Prozess deswegen abzubrechen. Dabei siehst du `AssertionError`, die beiden Werte und den Namen `test_mismatch`.

Die anschließenden Tests von `MeanTests` und `ToleranceTests` müssen bestehen. Sonst beendet das Skript sich mit einem Fehlercode.

## Was die echten Tests abdecken

- Mittelwert von 20 und 22 ist 21.
- Eine einzelne Messung ist ihr eigener Mittelwert.
- Eine leere Reihe löst `ValueError` aus.
- Die Abweichung 0,4 liegt bei Toleranz 0,5 innen.
- Die Abweichung 0,5 liegt auf der Grenze und gilt als innen.
- Die Abweichung 1,0 liegt außen.
- Eine negative Toleranz löst `ValueError` aus.

## Übung

Lies `test_empty_series` und `test_on_the_boundary` und ordne jede Methode einer der drei Lagen aus Einheit 18 zu: üblicher Fall, Rand, Grenze. Die Methoden sind die ausgearbeitete Lösung dieser Zuordnung. Ändere die erwarteten Werte nicht, um eine Meldung zum Verschwinden zu bringen.

## Lösung

Der Rand der leeren Reihe:

```python
def test_empty_series(self):
    with self.assertRaises(ValueError):
        mean([])
```

Die Grenze der Toleranz:

```python
def test_on_the_boundary(self):
    self.assertTrue(within_tolerance(20.5, 20.0, 0.5))
```

Damit ist der Kurs durch. Die Zusammenfassung steht in `Tag4_Zusammenfassung.md`.
