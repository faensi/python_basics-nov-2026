# Verzweigungen

**Tag 2, Einheit 08**  
**Skript:** `tag2/08_verzweigungen.py`

## Ziel

In dieser Einheit schreibst du eine Verzweigung mit `if`, `elif` und `else` und verknüpfst Vergleiche mit `and`.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `status` ergänzen.
4. In der Konsole `check_status()` aufrufen.

## Form

Nach dem Doppelpunkt kommt ein eingerückter Block. `elif` prüft den nächsten Fall nur, wenn die bisherigen Bedingungen falsch waren. `else` fängt den Rest.

```python
if difference <= tolerance and reading >= reference:
    print("state: inside, on the high side")
elif reading < reference:
    print("state: below the reference")
else:
    print("state: above the tolerance")
```

Vergleiche sind `<`, `<=`, `>`, `>=`, `==` und `!=`. `=` bleibt die Zuweisung und ist kein Vergleich. `and`, `or` und `not` verknüpfen Bedingungen.

## Übung

Eine Anzeige gilt als innerhalb der Toleranz, wenn der Betrag der Abweichung vom Referenzwert höchstens die Toleranz ist. `abs` liefert den Betrag.

`status(reading, reference, tolerance)` gibt einen von drei Texten zurück:

| Aufruf | Ergebnis |
| --- | --- |
| `status(20.2, 20.0, 0.5)` | `"inside"` |
| `status(21.0, 20.0, 0.5)` | `"high"` |
| `status(19.0, 20.0, 0.5)` | `"low"` |

Liegt die Anzeige innerhalb der Toleranz, ist das Ergebnis `"inside"`, auch wenn sie etwas über oder unter dem Referenzwert liegt. `"high"` und `"low"` gelten nur außerhalb der Toleranz.

## Lösung

```python
def solution_status(reading, reference, tolerance):
    difference = abs(reading - reference)
    if difference <= tolerance:
        return "inside"
    if reading > reference:
        return "high"
    return "low"
```

Weiter mit `tag2/09_schleifen.md`.
