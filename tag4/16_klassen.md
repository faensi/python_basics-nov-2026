# Kurze Einführung in Klassen

**Tag 4, Einheit 16**  
**Skript:** `tag4/16_klassen.py`

## Ziel

In dieser Einheit definierst du eine Klasse mit Konstruktor und Methoden, erzeugst zwei Instanzen und hältst deren Daten auseinander.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Ergänze die Methode `is_within`.
4. In der Konsole `check_is_within()` aufrufen.

Das ist eine kurze Einführung. Vererbung, besondere Methodennamen und Entwurfsmuster gehören nicht zu diesem Kurs.

## Klasse und Instanz

Am Tag 1 war `float` die Klasse der Temperaturzahl. `Reading` ist eine Klasse, die du selbst schreibst. Ein Aufruf `Reading("bath", 20.1)` erzeugt eine **Instanz**. `bath` und `room` im Skript sind zwei Instanzen. `type(bath).__name__` ist `"Reading"`.

`__init__` richtet eine neue Instanz ein. `self` ist diese Instanz. `self.sensor` und `self.celsius` gehören zu ihr, nicht zur Klasse insgesamt.

```python
bath = Reading("bath", 20.1)
room = Reading("room", 21.5)
room.celsius = 21.6
```

Danach steht `bath.celsius` noch auf 20,1. Die Zuweisung hat nur `room` getroffen.

## Methode

`deviation` und `kelvin` sind Methoden. Der Aufruf `bath.deviation(20.0)` übergibt `bath` als `self`. Die Differenz zur Referenz ist dieselbe Rechnung wie `measurement.deviation` am Tag 3, jetzt an die Instanz gebunden.

`kelvin` rechnet Grad Celsius nach Kelvin: es addiert 273,15. Für 20,1 Grad Celsius zeigt das Skript 293,25.

## Übung

`is_within(reference, tolerance)` steht auf der Klasse und gibt `True` zurück, wenn der Betrag der Abweichung höchstens die Toleranz ist. Nutze `self.deviation`.

| Aufruf | Ergebnis |
| --- | --- |
| `Reading("bath", 20.4).is_within(20.0, 0.5)` | `True` |
| `Reading("bath", 21.0).is_within(20.0, 0.5)` | `False` |

## Lösung

Die prüfbare Fassung steht als Funktion unter der Klasse, weil die Methode in der Klasse die Übung bleibt:

```python
def solution_is_within(reading, reference, tolerance):
    return abs(reading.deviation(reference)) <= tolerance
```

Dieselbe Zeile gehört in `Reading.is_within`, mit `self` anstelle von `reading`.

Weiter mit `tag4/17_debugging.md`.
