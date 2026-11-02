# Python-Grundlagen

Kursmaterial für eine Einführung an vier Tagen. Der Kurs richtet sich an Wissenschaftlerinnen, Wissenschaftler, Ingenieurinnen und Ingenieure ohne Vorkenntnisse in Python.

In diesem Kurs arbeitest du in Spyder. Die Umgebung kommt aus Miniforge.

## Kursordner holen

Die Installation von Git und der Abruf des Kursordners über HTTPS stehen in `git_holen.md`.

## Umgebung anlegen

Die Paketliste steht in `environment.yml`. Der Name der Umgebung ist `python_grundlagen`, die Python-Version ist 3.13. Der Kanal ist conda-forge.

Wechsle in diesen Ordner `python_basics-nov-2026` und lege die Umgebung an:

```bash
conda env create -f environment.yml
conda activate python_grundlagen
```

Eine schon vorhandene Umgebung gleichen Namens bringst du so auf den Stand der Datei:

```bash
conda env update -n python_grundlagen -f environment.yml --prune
```

Den Python dieser Umgebung findest du mit:

```bash
python -c "import sys; print(sys.executable)"
```

## Spyder

Starte Spyder aus der aktivierten Umgebung:

```bash
conda activate python_grundlagen
spyder
```

Stelle den Interpreter auf diese Umgebung: **Tools**, **Preferences**, **Python interpreter**. Trage den Pfad ein, den der Befehl oben ausgegeben hat. Starte Spyder danach neu.

Setze das Arbeitsverzeichnis auf diesen Ordner `python_basics-nov-2026`. In Spyder steht der Ordner oben im Fenster und im Dateibaum. Daten lesen die Skripte als `data/readings.csv`, also vom Kursordner aus, nicht vom Tagesordner aus.

- **F5** führt die geöffnete Datei aus.
- **F9** führt die markierte Zeile oder Auswahl in der IPython-Konsole aus.
- Der Variablenexplorer zeigt die Namen nach einem Lauf.
- Wenn alte Namen stören, starte die IPython-Konsole neu und führe die Datei erneut aus.

Eine Eingabe mit `input` erscheint in der IPython-Konsole. Klicke in die Konsole und tippe den Wert dort.

## Wie eine Einheit aufgebaut ist

Jede Einheit gibt es zweimal, mit demselben Namen: als Notebook und als Python-Skript. Die Erklärung steht auf Deutsch. Im Notebook sind das Textzellen, im Skript dieselben Abschnitte als Kommentarzeilen. Namen, Docstrings und die kurzen Hinweise direkt am Code bleiben Englisch.

Die Übung steht vor der Lösung. `# gegeben:` markiert die Vorgaben, `# lösung ab hier:` die Lücken. Die Übung ist so noch kein fertiges Programm. Die Lösung darunter ist für sich ausführbar. Im Notebook startest du dafür nur die Lösungszelle. Funktionen kommen erst dort vor, wo die Einheit Funktionen, Module, Klassen oder Tests behandelt.

In Spyder öffnest du das Skript und startest es mit F5. Das Notebook öffnest du, wenn du die Textzellen sehen willst. Wenn Spyder die Notebook-Datei nicht öffnet, starte aus derselben Umgebung `jupyter notebook`.

## Ablauf

Die Übersicht mit allen Einheiten steht in `00_uebersicht.md`. Die Themen folgen `information.md`. Die Reihenfolge im Unterricht ist: Daten, dann Kontrollstrukturen und Funktionen, dann Ein- und Ausgabe und Module, dann eine kurze Objektorientierung mit Testen und Debugging.

Am Ende jedes Tages steht `TagN_Zusammenfassung.md`.
