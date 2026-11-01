# Umwandlung, Referenz, In-Place-Methoden, `copy` und `deepcopy`

**Tag 1, Einheit 07**  
**Skript:** `tag1/07_konvertierung_referenzen_kopien.py`

## Ziel

Sie wandeln Werte zwischen Text, Zahl, Liste und Dictionary um. Sie erkennen, wann zwei Namen dasselbe Objekt meinen, und Sie kopieren eine verschachtelte Messgruppe so, dass spätere Änderungen nicht zurückwirken.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `sorted_snapshot` und `independent_groups` ergänzen.
4. In der Konsole `check_copies()` aufrufen.

## Umwandlung

| Aufruf | Ergebnis | Hinweis |
| --- | --- | --- |
| `int("20")` | `20` | Text aus Ziffern wird zur ganzen Zahl |
| `str(20)` | `"20"` | Zahl wird Text |
| `float("20.5")` | `20.5` | Text wird Gleitkommazahl |
| `int(20.9)` | `20` | Der Nachkommateil fällt weg, es wird nicht gerundet |
| `list(ein_dict.items())` | Liste von Paaren | Schlüssel und Wert nebeneinander |
| `dict(paare)` | Dictionary | der Weg zurück |

`int("20.5")` schlägt fehl, weil der Text keine ganze Zahl ist. Das Skript führt diesen Aufruf nicht aus.

## Zwei Namen, ein Objekt

```python
first = [20.2, 19.8, 20.0]
second = first
second.append(21.0)
```

`first` und `second` sind nicht zwei Listen. Es sind zwei Namen für dieselbe Liste. `append` ändert dieses eine Objekt, deshalb sieht `first` den neuen Wert ebenfalls.

Eine Zahl funktioniert anders, weil Sie sie nicht an Ort und Stelle ändern, sondern den Namen neu binden. Das war die Zuweisung `celsius = 21.0` in Einheit 02.

## In-Place-Methoden

`sorted(first)` baut eine neue Liste und lässt `first` in Ruhe.

`first.sort()` sortiert `first` selbst und gibt `None` zurück. Wer das Ergebnis von `sort` oder `append` weiterverwendet, arbeitet mit `None`, nicht mit der Liste.

## `copy` und `deepcopy`

`copy.copy` legt eine neue äußere Liste an. Die Einträge darin sind weiterhin dieselben Objekte. Bei einer Liste von Zahlen genügt das, weil Zahlen nicht nachträglich innen verändert werden.

`copy.deepcopy` kopiert auch die verschachtelten Listen. Das brauchen Sie, wenn eine Gruppe selbst wieder Listen enthält.

Das Skript geht von dieser Gruppe aus:

```python
groups = [["bath", 20.1], ["room", 21.5]]
```

Es ändert danach den ersten Temperaturwert auf 25,0 und hängt eine weitere Gruppe an. Danach gilt:

- `alias` ist `groups` und enthält die Änderung und den neuen Eintrag.
- Die flache Kopie enthält die geänderte Innentemperatur, aber nicht den neuen Eintrag. Die innere Liste war geteilt, die äußere nicht.
- Die tiefe Kopie steht noch auf 20,1 und 21,5.

## Übung

- `sorted_snapshot([20.0, 19.0, 21.0])` liefert `[19.0, 20.0, 21.0]`. Die übergebene Liste bleibt unsortiert. Eine flache Kopie reicht.
- `independent_groups` liefert eine tiefe Kopie. Wenn der Aufrufer danach eine Innentemperatur ändert, bleibt Ihre Kopie bei den alten Werten.

## Lösung

```python
def solution_sorted_snapshot(values):
    snapshot = copy.copy(values)
    snapshot.sort()
    return snapshot

def solution_independent_groups(groups):
    return copy.deepcopy(groups)
```

Weiter mit `tag2/08_verzweigungen.md`. Die Zusammenfassung des Tages steht in `Tag1_Zusammenfassung.md`.
