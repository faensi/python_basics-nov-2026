# Python, Philosophie und Unterschied zu anderen Sprachen

**Tag 1, Einheit 00**
**Skript:** `tag1/00_python_ueberblick.py`

## Ziel

In dieser Einheit kannst du ein kleines Python-Skript in Spyder starten und sagen, worin sich Python von Sprachen wie C, C++ oder Java unterscheidet.

## Ablauf in Spyder

1. Setze das Arbeitsverzeichnis auf den Ordner `python_basics-nov-2026`.
2. Öffne das Skript und führe es mit F5 aus.
3. Lies die Ausgabe in der IPython-Konsole.
4. Ergänze die Übung am Ende des Skripts.
5. Führe das Skript erneut mit F5 aus.

## Was Python ausmacht

Python ist eine interpretierte Sprache: du schreibst den Quelltext, und der Interpreter führt ihn aus. Es gibt keinen getrennten Übersetzungsschritt, den du vor dem ersten Lauf abwarten musst.

Python ist dynamisch typisiert, und du schreibst an den Namen nicht, ob er eine Zahl oder einen Text meint. Der Typ gehört zum Wert und zeigt sich zur Laufzeit. Das vertieft Einheit 02.

Python legt Wert auf lesbaren Text. Blöcke entstehen durch Einrückung, nicht durch geschweifte Klammern. Anweisungen brauchen kein Semikolon am Ende. Dieselbe Einrückungstiefe gehört zum selben Block. Mische keine Tabulatoren und Leerzeichen. In diesem Kurs bestehen Einrückungen aus vier Leerzeichen.

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

Außerdem entfällt die Deklaration der Variablen vor der ersten Nutzung, und du startest das Skript direkt.

## Übung

Schreibe am Ende des Skripts drei eigene Variablen und gib sie aus.

- `sensor` ist ein Text, zum Beispiel der Name eines Orts.
- `celsius` ist eine Temperatur mit Nachkommastelle.
- `count` ist eine Anzahl als ganze Zahl.

Such dir die Werte selbst aus.

## Lösung

```python
sensor = "hall"
celsius = 18.5
count = 4
print(sensor, celsius, count)
```

Weiter mit `tag1/01_ipython_notebook.ipynb`.
