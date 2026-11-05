# Kursübersicht

Vier Tage, ein Arbeitsverzeichnis: der Ordner `python_basics-nov-2026`. Die Einheiten liegen in `tag1` bis `tag4`. Daten liegen in `data/`.

Die Nummern laufen über die Tage durch. Jede Einheit gibt es zweimal: als Notebook `.ipynb` und als Skript `.py` mit demselben Namen. Im Notebook steht die Erklärung in Textzellen. Im Skript steht dieselbe Erklärung als Kommentar. Die Übung steht vor der Lösung.

## Tag 1: Überblick und Datenstrukturen

| Einheit | Datei                                       | Inhalt                                                                |
| ------- | ------------------------------------------- | --------------------------------------------------------------------- |
| 00      | `tag1/00_python_ueberblick`               | Python, Lesbarkeit, Unterschied zu Sprachen mit geschweiften Klammern |
| 01      | `tag1/01_ipython_notebook.ipynb`          | IPython und das Notebook                                              |
| 02      | `tag1/02_datentypen_variablen_objekte`    | Datentypen, Klassen, Variablen, Objekte                               |
| 03      | `tag1/03_listen_tupel_slicing`            | Listen, Tupel, Slicing                                                |
| 04      | `tag1/04_strings_und_sortierung`          | Strings, Stringfunktionen, `sort` und `sorted`                    |
| 05      | `tag1/05_iteratoren`                      | Iteratoren und iterierbare Objekte                                    |
| 06      | `tag1/06_dictionaries_sets`               | Dictionaries, Sets, Frozensets                                        |
| 07      | `tag1/07_konvertierung_referenzen_kopien` | Umwandlung, Referenz, In-Place-Methoden, `copy`, `deepcopy`       |

Zusammenfassung: `tag1/Tag1_Zusammenfassung.md`

## Tag 2: Kontrollstrukturen und Funktionen

| Einheit | Datei                                  | Inhalt                                                                         |
| ------- | -------------------------------------- | ------------------------------------------------------------------------------ |
| 08      | `tag2/08_verzweigungen`              | `if`, `elif`, `else`                                                     |
| 09      | `tag2/09_schleifen`                  | `while`, `for`, Indexschleife, `continue`, `break`, `else`, `pass` |
| 10      | `tag2/10_funktionen`                 | Definition, Aufruf, Rückgabewert                                              |
| 11      | `tag2/11_parameter_und_sichtbarkeit` | Positionsparameter, Schlüsselwortparameter, lokal und global                  |

Zusammenfassung: `tag2/Tag2_Zusammenfassung.md`

## Tag 3: Ein- und Ausgabe und Module

| Einheit | Datei                                | Inhalt                                                               |
| ------- | ------------------------------------ | -------------------------------------------------------------------- |
| 12      | `tag3/12_eingabe_und_formatierung` | `input`, früheres `raw_input`, Prozentformat, `format`        |
| 13      | `tag3/13_dateien`                  | Textdateien lesen und schreiben                                      |
| 14      | `tag3/14_module_und_namensraeume`  | Standardmodule, Import, Namensräume, Gültigkeitsbereiche, `help` |
| 15      | `tag3/15_eigene_module`            | Eigenes Modul `measurement.py`, Docstring                          |

Zusatz ohne Einheitsnummer:

- `tag3/csv_pandas_numpy.ipynb` — CSV mit pandas und numpy
- `tag3/matplotlib_csv.ipynb` — Visualisierung aus CSV mit matplotlib
- `tag3/live_diagramm.ipynb` — Array als Live-Diagramm
- `tag3/hdf5_h5py.ipynb` — HDF5-Dateien mit h5py
- `tag3/spectral_eval_file.ipynb` — Klasse `SpectralEvalFile` für spektrale Auswertungsdateien

Zusammenfassung: `tag3/Tag3_Zusammenfassung.md`

## Tag 4: Klassen, Debugging und Tests

| Einheit | Datei                 | Inhalt                                      |
| ------- | --------------------- | ------------------------------------------- |
| 16      | `tag4/16_klassen`   | Kurze Einführung: Klasse, Instanz, Methode |
| 17      | `tag4/17_debugging` | Debugging: Traceback, `print`, `try` / `except` |
| 18      | `tag4/18_doctest`   | Systematisches Testen und `doctest`       |
| 19      | `tag4/19_unittest`  | `unittest`                                |

Zusammenfassung: `tag4/Tag4_Zusammenfassung.md`

## Daten

- `data/readings.csv`: Messreihe zweier Sensoren, Bad und Raum (je 250 Werte)
- `data/calibration.csv`: Referenzwert und Anzeige (200 Werte)
- `data/notes.txt`: Probenprotokoll mit vielen Zeitzeilen
- `data/pump_pressure.csv`: Druckreihe Einlass und Auslass (je 300 Werte)
- `data/gauge_check.csv`: Referenzdruck und Anzeige (180 Werte)
- `data/flow_series.h5`: Durchfluss Einlass und Auslass (je 500 Werte)
- `data/data-x1.txt`: spektrale Auswertungsdatei mit Info-Block und Messreihe

Einheit 13 schreibt zusätzlich `data/report.txt`. Diese Datei ist ein Ergebnis, keine Vorlage.

## Arbeitsweise

1. Arbeitsverzeichnis auf `python_basics-nov-2026` setzen.
2. Notebook der Einheit öffnen, oder das Skript mit demselben Namen.
3. Die Beispielzellen von oben nach unten ausführen. In Spyder die Beispiele mit F5 starten, sobald die Lücken in der Übung geschlossen sind.
4. Die Übung steht vor der Lösung. `# gegeben:` markiert die Vorgaben. Ab `# lösung ab hier:` schreibst du. Die Lücken sind absichtlich kein fertiges Programm.
5. Die Lösung am Ende ist für sich ausführbar. Im Notebook startest du dafür nur diese Zelle.
