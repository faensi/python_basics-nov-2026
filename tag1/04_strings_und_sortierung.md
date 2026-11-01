# Strings, Stringfunktionen, `sort` und `sorted`

**Tag 1, Einheit 04**  
**Skript:** `tag1/04_strings_und_sortierung.py`

## Ziel

Sie bereinigen einen Sensortext mit String-Methoden. Sie sortieren eine Zahlenliste, ohne die ursprüngliche Liste zu verändern, und Sie erkennen den Unterschied zwischen `sorted` und `sort`.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `clean_label` und `sorted_copy` ergänzen.
4. In der Konsole `check_strings_and_sort()` aufrufen.

## Strings

Ein String ist Text. Er ist unveränderlich: Methoden liefern einen neuen String, sie schreiben den alten nicht um.

| Methode | Wirkung am Beispiel `"  Bath-01  "` |
| --- | --- |
| `strip()` | Leerzeichen an den Enden weg |
| `lower()` | Kleinbuchstaben |
| `split(";")` | an einem Trennzeichen zerlegen, siehe `"bath;room"` |
| `replace(" C", " celsius")` | ein Stück Text ersetzen |
| `startswith("ba")` | prüfen, womit der Text beginnt |

Methoden lassen sich verketten: `label.strip().lower()`.

## `sorted` und `sort`

`sorted(werte)` liefert eine neue, sortierte Liste. Die Liste, die Sie übergeben, bleibt wie sie ist.

`werte.sort()` sortiert an Ort und Stelle. Der Rückgabewert ist `None`, nicht die Liste. Wer `print(werte.sort())` schreibt, sieht `None` und hat die Liste trotzdem verändert. Das ist eine In-Place-Methode. Einheit 07 geht darauf noch einmal ein.

## Übung

- `clean_label("  Bath-01  ")` liefert `"bath-01"`.
- `sorted_copy([20.2, 19.8, 20.0])` liefert `[19.8, 20.0, 20.2]`. Die Liste, die Sie übergeben haben, bleibt `[20.2, 19.8, 20.0]`.

Nutzen Sie `sorted`, nicht `sort`, wenn die Ausgangsliste erhalten bleiben soll.

## Lösung

```python
def solution_clean_label(label):
    return label.strip().lower()

def solution_sorted_copy(values):
    return sorted(values)
```

Weiter mit `tag1/05_iteratoren.md`.
