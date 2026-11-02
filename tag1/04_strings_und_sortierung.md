# Strings, Stringfunktionen, `sort` und `sorted`

**Tag 1, Einheit 04**  
**Skript:** `tag1/04_strings_und_sortierung.py`

## Ziel

In dieser Einheit bereinigst du einen Sensortext mit String-Methoden, sortierst eine Zahlenliste, ohne die ursprüngliche Liste zu verändern, und erkennst den Unterschied zwischen `sorted` und `sort`.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `python_basics-nov-2026`.
2. Skript mit F5 ausführen.
3. Übung am Ende des Skripts ergänzen.
4. Skript erneut mit F5 ausführen.

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

`sorted(werte)` liefert eine neue, sortierte Liste. Die Liste, die du übergibst, bleibt wie sie ist.

`werte.sort()` sortiert an Ort und Stelle. Der Rückgabewert ist `None`, nicht die Liste. Wer `print(werte.sort())` schreibt, sieht `None` und hat die Liste trotzdem verändert. Das ist eine In-Place-Methode. Einheit 07 geht darauf noch einmal ein.

## Übung

Aus `probe` machst du den Text `"probe_7"`. Entferne die Leerzeichen an den Enden, schreibe klein und ersetze den Bindestrich durch einen Unterstrich.

Aus `series` machst du eine neue sortierte Liste `[18.0, 19.2, 21.5]`. `series` bleibt `[21.5, 18.0, 19.2]`. Nutze `sorted`, nicht `sort`.

## Lösung

```python
tidy = probe.strip().lower().replace("-", "_")
ordered = sorted(series)
print(tidy)
print(ordered, series)
```

Weiter mit `tag1/05_iteratoren.md`.
