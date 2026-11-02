# Python, Philosophie und Unterschied zu anderen Sprachen
#
# Tag 1, Einheit 00
# Skript: `tag1/00_python_ueberblick.py`
#
# Ziel
#
# Du startest ein kleines Python-Programm und kannst sagen, worin sich Python von C, C++ oder Java unterscheidet.
#
# Zwei Dateien, derselbe Inhalt
#
# Jede Einheit gibt es als Notebook und als Skript. Im Notebook steht die Erklärung in Textzellen und der Code in Codezellen. Im Skript steht dieselbe Erklärung als Kommentar. Arbeitsverzeichnis ist der Ordner `python_basics-nov-2026`. Das Skript startest du in Spyder mit F5. Im Notebook führst du die Zellen von oben nach unten aus. Die Übung steht vor der Lösung.

# Was Python ausmacht
#
# Python ist eine interpretierte Sprache. Du schreibst den Quelltext, und der Interpreter führt ihn aus. Es gibt keinen getrennten Übersetzungsschritt vor dem ersten Lauf.
#
# Python ist dynamisch typisiert. Du schreibst an den Namen nicht, ob er eine Zahl oder einen Text meint. Der Typ gehört zum Wert.
#
# Blöcke entstehen durch Einrückung, nicht durch geschweifte Klammern. Anweisungen brauchen kein Semikolon am Ende. Dieselbe Einrückungstiefe gehört zum selben Block. In diesem Kurs bestehen Einrückungen aus vier Leerzeichen.
#
# Zur Sprache gehört ein kurzer englischer Text über guten Stil, der Zen of Python. Das Programm gibt ihn mit `import this` aus. Zwei Leitlinien reichen für den Anfang: lesbarer Text zählt, und einfach ist besser als verschachtelt.

print("Hello, Python")
print("sum:", 19.5 + 2.0)
reading = 20.1
limit = 20.0
# Indentation groups the branch. There are no braces.
if reading > limit:
    print("state: above the limit")
else:
    print("state: at or below the limit")
print("Zen of Python:")
import this

# Unterschied zu C, C++ und Java
#
# In C sieht eine Verzweigung ungefähr so aus:
#
#     if (reading > limit) {
#         printf("above\n");
#     } else {
#         printf("at or below\n");
#     }
#
# In Python fällt die Klammer weg, und der Block rückt ein. Die nächste Zelle ist dieselbe Verzweigung. Außerdem entfällt die Deklaration der Variablen vor der ersten Nutzung.

# Übung
#
# Lege drei eigene Namen an und gib sie aus. Übernimm nicht die Werte `20.1` und `20.0` aus der Zelle weiter oben.
#
# - `sensor` ist ein Text, zum Beispiel ein Ort.
# - `celsius` ist eine Temperatur mit Nachkommastelle.
# - `count` ist eine Anzahl als ganze Zahl.

# lösung ab hier:
sensor =
celsius =
count =
print("exercise", sensor, celsius, count)

# Lösung
#
# Andere Orte, andere Temperaturen und andere Anzahlen sind ebenfalls richtig.

sensor = "hall"
celsius = 18.5
count = 4
print("solution", sensor, celsius, count)

# Weiter mit `tag1/01_ipython_notebook.ipynb`.
