# Python-Grundlagen

Kursmaterial für eine Einführung an vier Tagen. Der Kurs richtet sich an Wissenschaftlerinnen, Wissenschaftler, Ingenieurinnen und Ingenieure ohne Vorkenntnisse in Python.

Sie arbeiten in Spyder. Die Umgebung kommt aus Miniforge.

## Umgebung anlegen

Die Paketliste steht in `environment.yml`. Der Name der Umgebung ist `python_grundlagen`, die Python-Version ist 3.13. Der Kanal ist conda-forge.

Wechseln Sie in diesen Ordner `this_course` und legen Sie die Umgebung an:

```bash
conda env create -f environment.yml
conda activate python_grundlagen
```

Eine schon vorhandene Umgebung gleichen Namens bringen Sie so auf den Stand der Datei:

```bash
conda env update -n python_grundlagen -f environment.yml --prune
```

Den Python dieser Umgebung finden Sie mit:

```bash
python -c "import sys; print(sys.executable)"
```

## Spyder

Starten Sie Spyder aus der aktivierten Umgebung:

```bash
conda activate python_grundlagen
spyder
```

Stellen Sie den Interpreter auf diese Umgebung: **Tools**, **Preferences**, **Python interpreter**. Tragen Sie den Pfad ein, den der Befehl oben ausgegeben hat. Starten Sie Spyder danach neu.

Setzen Sie das Arbeitsverzeichnis auf diesen Ordner `this_course`. In Spyder steht der Ordner oben im Fenster und im Dateibaum. Daten lesen die Skripte als `data/readings.csv`, also vom Kursordner aus, nicht vom Tagesordner aus.

- **F5** führt die geöffnete Datei aus.
- **F9** führt die markierte Zeile oder Auswahl in der IPython-Konsole aus.
- Der Variablenexplorer zeigt die Namen nach einem Lauf.
- Wenn alte Namen stören, starten Sie die IPython-Konsole neu und führen Sie die Datei erneut aus.

Eine Eingabe mit `input` erscheint in der IPython-Konsole. Klicken Sie in die Konsole und tippen Sie den Wert dort.

## Wie eine Einheit aufgebaut ist

Jede Einheit hat eine Markdown-Datei und ein Python-Skript mit demselben Namen. Die Erklärung und die Aufgabe stehen auf Deutsch in der Markdown-Datei. Das Skript ist auf Englisch: Namen, Kommentare und Docstrings folgen der üblichen Programmiersprache.

Führen Sie das Skript mit F5 aus. Die Beispiele laufen dabei. Funktionen ohne Vorsilbe sind die Übung und geben am Anfang `None` zurück. Funktionen mit der Vorsilbe `solution_` sind die Lösung und stehen am Ende des Skripts. In der Konsole prüfen Sie Ihre Fassung mit der passenden Funktion `check_...`.

Die Einheit zum Notebook ist die Ausnahme: `tag1/01_ipython_notebook.ipynb`. Wenn Ihre Spyder-Version diese Datei nicht öffnet, starten Sie aus derselben Umgebung `jupyter notebook` und öffnen Sie nur diese eine Datei. Die übrigen Einheiten bleiben Skripte in Spyder.

## Ablauf

Die Übersicht mit allen Einheiten steht in `00_uebersicht.md`. Die Themen folgen `information.md`. Die Reihenfolge im Unterricht ist: Daten, dann Kontrollstrukturen und Funktionen, dann Ein- und Ausgabe und Module, dann eine kurze Objektorientierung mit Testen und Debugging.

Am Ende jedes Tages steht `TagN_Zusammenfassung.md`.
