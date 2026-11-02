# Eingabe und formatierte Ausgabe
#
# Tag 3, Einheit 12
# Skript: `tag3/12_eingabe_und_formatierung.py`
#
# Ziel
#
# Du liest eine Eingabe als Text, wandelst sie in eine Zahl und formatierst eine Zeile auf zwei Wegen: mit dem Prozentoperator und mit der Methode `format`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten. F5 fragt nichts ab.

# `input`
#
# `input` liest eine Zeile von der Tastatur und gibt sie als String zurück. Die Frage erscheint in der IPython-Konsole, nicht im Editor. Wirkt das Programm angehalten, liegt der Fokus oft noch im Editor. Klicke in die Konsole und tippe den Wert dort.
#
# In Python 2 hieß die Funktion für eine Textzeile `raw_input`. In Python 3 heißt sie `input`. `raw_input` gibt es hier nicht.
#
# Die beiden Zeilen mit `input` stehen als Kommentar, damit F5 nicht auf die Tastatur wartet. Markiere sie in Spyder, nimm die Kommentarzeichen am Zeilenanfang weg und führe sie mit F9 aus. Im Notebook nimmst du die Kommentarzeichen weg und führst nur diese Zelle aus.

# text = input("Temperature in C: ")
# number = float(text.strip())
# print(number)

# Zwei Formatierungen
#
# Dieselbe Zeile, eine Nachkommastelle:
#
#     "%s: %.1f C" % (sensor, celsius)
#     "{}: {:.1f} C".format(sensor, celsius)
#
# `%s` und `{}` stehen für den Sensornamen, `%.1f` und `{:.1f}` für die Temperatur mit einer Nachkommastelle. Für den Sensor `bath` und 20,1 Grad Celsius entsteht der Text `bath: 20.1 C`.
#
# Im Python-Text bleibt der Punkt das Dezimalzeichen. Im deutschen Satz schreibst du das Komma.
#
# Eine neuere Schreibweise sind f-Strings, etwa `f"{sensor}: {celsius:.1f} C"`. Diese Einheit bleibt beim Prozentoperator und bei `format`.

sensor = "bath"
celsius = 20.1
percent_line = "%s: %.1f C" % (sensor, celsius)
format_line = "{}: {:.1f} C".format(sensor, celsius)
print("percent:", percent_line)
print("format:", format_line)
print("same text:", percent_line == format_line)

# Übung
#
# Baue für den Sensor `bath` und die Temperatur 20,0 zwei gleiche Zeilen. Die eine entsteht mit dem Prozentoperator, die andere mit `format`. Beide Texte sind `bath: 20.0 C`.
#
# Aus dem Text ` 20.5 ` machst du die Zahl `20.5`. Entferne die äußeren Leerzeichen und rufe `float` auf.

# gegeben:
sensor = "bath"
celsius = 20.0
text = " 20.5 "

# lösung ab hier:
percent_line =
format_line =
number =
print("exercise", percent_line)
print("exercise", format_line)
print("exercise", number)

# Lösung

sensor = "bath"
celsius = 20.0
percent_line = "%s: %.1f C" % (sensor, celsius)
format_line = "{}: {:.1f} C".format(sensor, celsius)
text = " 20.5 "
number = float(text.strip())
print("solution", percent_line)
print("solution", format_line)
print("solution", number)

# Weiter mit `tag3/13_dateien.ipynb`.
