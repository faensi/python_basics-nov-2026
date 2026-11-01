# Python, Philosophie und Unterschied zu anderen Sprachen

**Tag 1, Einheit 00**  
**Skript:** `tag1/00_python_ueberblick.py`

## Ziel

Sie können ein kleines Python-Skript in Spyder starten und sagen, worin sich Python von Sprachen wie C, C++ oder Java unterscheidet.

## Ablauf in Spyder

1. Setzen Sie das Arbeitsverzeichnis auf den Ordner `this_course`.
2. Öffnen Sie das Skript und führen Sie es mit F5 aus.
3. Lesen Sie die Ausgabe in der IPython-Konsole.
4. Ergänzen Sie die Funktion `temperature_span`.
5. Rufen Sie in der Konsole `check_temperature_span()` auf.

## Was Python ausmacht

Python ist eine interpretierte Sprache. Sie schreiben den Quelltext, und der Interpreter führt ihn aus. Es gibt keinen getrennten Übersetzungsschritt, den Sie vor dem ersten Lauf abwarten müssen.

Python ist dynamisch typisiert. Sie schreiben an den Namen nicht, ob er eine Zahl oder einen Text meint. Der Typ gehört zum Wert und zeigt sich zur Laufzeit. Das vertieft Einheit 02.

Python legt Wert auf lesbaren Text. Blöcke entstehen durch Einrückung, nicht durch geschweifte Klammern. Anweisungen brauchen kein Semikolon am Ende. Dieselbe Einrückungstiefe gehört zum selben Block. Mischen Sie keine Tabulatoren und Leerzeichen. In diesem Kurs bestehen Einrückungen aus vier Leerzeichen.

Zur Sprache gehört ein kurzer Text über guten Python-Stil, der Zen of Python. Das Skript gibt ihn mit `import this` aus. Der Text ist Englisch und bleibt unverändert. Zwei Leitlinien daraus reichen für den Anfang: lesbarer Text zählt, und einfach ist besser als verschachtelt.

## Unterschied zu C, C++ und Java

In C sieht eine Verzweigung ungefähr so aus:

```c
if (reading > limit) {
    printf("above\n");
} else {
    printf("at or below\n");
}
```

In Python fällt die Klammer weg, und der Block rückt ein:

```python
if reading > limit:
    print("above")
else:
    print("at or below")
```

Außerdem entfällt die Deklaration der Variablen vor der ersten Nutzung, und Sie starten das Skript direkt.

## Übung

Eine Temperaturspanne ist der Abstand zwischen dem höheren und dem niedrigeren Wert. Ergänzen Sie `temperature_span`. Für 21,5 und 19,5 Grad Celsius ist das Ergebnis 2,0.

## Lösung

```python
def solution_temperature_span(high, low):
    return high - low
```

Die Funktion steht am Ende des Skripts. `check_temperature_span()` vergleicht Ihre Fassung damit.

Weiter mit `tag1/01_ipython_notebook.ipynb`.
