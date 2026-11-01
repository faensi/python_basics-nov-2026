# Kursübersicht

Vier Tage, ein Arbeitsverzeichnis: der Ordner `this_course`. Die Skripte liegen in `tag1` bis `tag4`. Daten liegen in `data/`.

Die Nummern laufen über die Tage durch. Öffnen Sie zu jeder Nummer zuerst die Markdown-Datei, dann das Skript.

## Tag 1: Überblick und Datenstrukturen

| Einheit | Datei | Inhalt |
| --- | --- | --- |
| 00 | `tag1/00_python_ueberblick` | Python, Lesbarkeit, Unterschied zu Sprachen mit geschweiften Klammern |
| 01 | `tag1/01_ipython_notebook.ipynb` | IPython und das Notebook |
| 02 | `tag1/02_datentypen_variablen_objekte` | Datentypen, Klassen, Variablen, Objekte |
| 03 | `tag1/03_listen_tupel_slicing` | Listen, Tupel, Slicing |
| 04 | `tag1/04_strings_und_sortierung` | Strings, Stringfunktionen, `sort` und `sorted` |
| 05 | `tag1/05_iteratoren` | Iteratoren und iterierbare Objekte |
| 06 | `tag1/06_dictionaries_sets` | Dictionaries, Sets, Frozensets |
| 07 | `tag1/07_konvertierung_referenzen_kopien` | Umwandlung, Referenz, In-Place-Methoden, `copy`, `deepcopy` |

Zusammenfassung: `tag1/Tag1_Zusammenfassung.md`

## Tag 2: Kontrollstrukturen und Funktionen

| Einheit | Datei | Inhalt |
| --- | --- | --- |
| 08 | `tag2/08_verzweigungen` | `if`, `elif`, `else` |
| 09 | `tag2/09_schleifen` | `while`, `for`, Indexschleife, `continue`, `break`, `else`, `pass` |
| 10 | `tag2/10_funktionen` | Definition, Aufruf, Rückgabewert |
| 11 | `tag2/11_parameter_und_sichtbarkeit` | Positionsparameter, Schlüsselwortparameter, lokal und global |

Zusammenfassung: `tag2/Tag2_Zusammenfassung.md`

## Tag 3: Ein- und Ausgabe und Module

| Einheit | Datei | Inhalt |
| --- | --- | --- |
| 12 | `tag3/12_eingabe_und_formatierung` | `input`, früheres `raw_input`, Prozentformat, `format` |
| 13 | `tag3/13_dateien` | Textdateien lesen und schreiben |
| 14 | `tag3/14_module_und_namensraeume` | Standardmodule, Import, Namensräume, Gültigkeitsbereiche, `help` |
| 15 | `tag3/15_eigene_module` | Eigenes Modul `measurement.py`, Docstring |

Zusammenfassung: `tag3/Tag3_Zusammenfassung.md`

## Tag 4: Klassen, Debugging und Tests

| Einheit | Datei | Inhalt |
| --- | --- | --- |
| 16 | `tag4/16_klassen` | Kurze Einführung: Klasse, Instanz, Methode |
| 17 | `tag4/17_debugging` | Haltepunkt und Einzelschritt in Spyder |
| 18 | `tag4/18_doctest` | Systematisches Testen und `doctest` |
| 19 | `tag4/19_unittest` | `unittest` |

Zusammenfassung: `tag4/Tag4_Zusammenfassung.md`

## Daten

- `data/readings.csv`: kurze Messreihe zweier Sensoren, Bad und Raum
- `data/calibration.csv`: Referenzwert und Anzeige
- `data/notes.txt`: kleines Probenprotokoll

Einheit 13 schreibt zusätzlich `data/report.txt`. Diese Datei ist ein Ergebnis, keine Vorlage.

## Arbeitsweise

1. Arbeitsverzeichnis auf `this_course` setzen.
2. Markdown-Datei der Einheit lesen.
3. Skript mit F5 ausführen.
4. Übung im Skript ergänzen.
5. `check_...()` in der IPython-Konsole aufrufen.
6. Lösung mit der Funktion `solution_...` am Ende des Skripts vergleichen.
