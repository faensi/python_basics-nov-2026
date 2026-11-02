# Parameter und Sichtbarkeit

**Tag 2, Einheit 11**  
**Skript:** `tag2/11_parameter_und_sichtbarkeit.py`

## Ziel

In dieser Einheit rufst du eine Funktion mit Positions- und mit Schlüsselwortargumenten auf, unterscheidest einen lokalen Namen von einem globalen und vermeidest eine Liste als Standardargument.

## Ablauf in Spyder

1. Arbeitsverzeichnis: `this_course`.
2. Skript mit F5 ausführen.
3. `shift` ergänzen.
4. In der Konsole `check_shift()` aufrufen.

## Positions- und Schlüsselwortargumente

Die Funktion `clip` begrenzt eine Anzeige auf ein Intervall. Beide Aufrufe meinen dasselbe:

```python
clip(22.0, 19.0, 21.0)
clip(22.0, low=19.0, high=21.0)
```

Beim ersten Aufruf entscheidet die Position. Beim zweiten der Name des Parameters. Schlüsselwortargumente dürfen nur nach den Positionsargumenten stehen.

Ein Parameter darf einen Standardwert haben. `shift(reading, offset=0.0)` addiert 0, wenn du keinen Offset angibst.

## Lokal und global

Ein Name, den du in einer Funktion zuweist, ist lokal. Er verdeckt einen gleichnamigen Namen außerhalb. `shadow` setzt `step` auf 5 und lässt den globalen Zähler auf 0.

Wer den globalen Namen wirklich ändern will, schreibt `global step` vor der Zuweisung. `advance` macht das. Bevorzuge in diesem Kurs Rückgabewerte. `global` ist hier nur zu sehen, damit die Wirkung nicht versehentlich passiert.

Parameter sind lokale Namen der Funktion.

## Standardwert und dasselbe Objekt

Ein Standardwert wird einmal erzeugt, nicht bei jedem Aufruf. Eine Liste als Standard teilen sich alle Aufrufe, die das Argument weglassen:

```python
def buggy_collect(reading, series=[]):
    series.append(reading)
    return series
```

Der zweite Aufruf sieht den Wert aus dem ersten Aufruf noch in der Liste. Das ist derselbe Effekt wie zwei Namen für ein Objekt in Einheit 07.

Die sichere Form nimmt `None` als Standard und legt die Liste im Körper an. Das tut `collect`.

## Übung

`shift(20.0)` liefert `20.0`. `shift(20.0, offset=0.5)` liefert `20.5`. Der Offset ist ein Parameter mit Standard 0.

## Lösung

```python
def solution_shift(reading, offset=0.0):
    adjusted = reading + offset
    return adjusted
```

Weiter mit `tag3/12_eingabe_und_formatierung.md`. Die Zusammenfassung des Tages steht in `Tag2_Zusammenfassung.md`.
