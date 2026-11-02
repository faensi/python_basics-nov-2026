# IPython und das Notebook
#
# Tag 1, Einheit 01
# Skript: `tag1/01_ipython_notebook.py`
#
# Ziel
#
# Du unterscheidest die IPython-Konsole in Spyder von einem Notebook und weißt, dass ein laufender Kernel sich Namen merkt.
#
# Im Notebook führst du die Zellen von oben nach unten aus. In Spyder öffnest du das Skript und startest es mit F5. Arbeitsverzeichnis ist `python_basics-nov-2026`. Wenn Spyder die Notebook-Datei nicht öffnet, aktiviere die Umgebung `python_grundlagen` und starte `jupyter notebook`.

# IPython
#
# IPython ist eine interaktive Shell. Du schreibst einen Ausdruck und siehst das Ergebnis sofort. Die Konsole in Spyder ist eine IPython-Konsole.
#
# - F5 führt ein geöffnetes Skript aus.
# - F9 führt die markierte Zeile oder Auswahl in der Konsole aus.
#
# Ein Notebook-Kernel ist derselbe Gedanke: ein laufender Python-Prozess, der sich Namen merkt. Starte den Kernel neu, wenn alte Namen stören. In Spyder startest du dafür die IPython-Konsole neu.

# Zellen
#
# Ein Notebook speichert Text und Code in Zellen.
#
# - Eine Textzelle enthält die Erklärung, so wie dieser Abschnitt.
# - Eine Code-Zelle enthält Python.
#
# Es zählt die Reihenfolge, in der du die Zellen ausführst, nicht nur die Reihenfolge auf der Seite. Eine Zelle kann einen Namen aus einer früheren Zelle benutzen. Fehlt der Name, war die frühere Zelle noch nicht ausgeführt.
#
# Die letzte Zeile einer Zelle zeigt ihren Wert auch ohne `print`. Darum steht `reading` nach den Druckzeilen noch einmal allein. Das gilt im Notebook und in der IPython-Konsole. Das Skript zeigt diese Zeile nicht noch einmal an. Markiere dort `reading` und drücke F9, dann siehst du den Wert in der Konsole.

print("Hello from a notebook cell")
print(19.5 + 1.5)
reading = 20.1
reading

# Eine kurze Messreihe
#
# Die Liste hält fünf Temperaturen in Grad Celsius. Der Index beginnt bei 0. `readings[0]` ist der erste Wert.

readings = [19.8, 20.1, 19.9, 20.0, 20.2]
print("count", len(readings))
print("first", readings[0])

# Übung
#
# Lege eine eigene Liste `own` mit drei Temperaturen an. Die Zahlen `19.8`, `20.1`, `19.9`, `20.0` und `20.2` übernimmst du nicht. Gib aus, wie viele Werte die Liste hat, und gib den ersten Wert aus.

# lösung ab hier:
own =
print("exercise", len(own), own[0])

# Lösung
#
# Andere drei Temperaturen mit Nachkommastelle sind ebenfalls richtig.

own = [18.0, 18.5, 19.0]
print("solution", len(own), own[0])

# Weiter mit `tag1/02_datentypen_variablen_objekte.ipynb`.
