# Verzweigungen
#
# Tag 2, Einheit 08
# Skript: `tag2/08_verzweigungen.py`
#
# Ziel
#
# Du schreibst eine Verzweigung mit `if`, `elif` und `else` und verknüpfst Vergleiche mit `and`.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.

# Form
#
# Nach dem Doppelpunkt kommt ein eingerückter Block. `elif` prüft den nächsten Fall nur, wenn die bisherigen Bedingungen falsch waren. `else` fängt den Rest.
#
# Vergleiche sind `<`, `<=`, `>`, `>=`, `==` und `!=`. `=` bleibt die Zuweisung und ist kein Vergleich. `and`, `or` und `not` verknüpfen Bedingungen.
#
# `abs` liefert den Betrag einer Zahl. `abs(reading - reference)` ist der Abstand der Anzeige vom Referenzwert, ohne Vorzeichen.

reading = 20.4
reference = 20.0
tolerance = 0.5
difference = abs(reading - reference)
if difference <= tolerance and reading >= reference:
    print("state: inside, on the high side")
elif reading < reference:
    print("state: below the reference")
else:
    print("state: above the tolerance")
print("difference", round(difference, 1))

# Übung
#
# Lege in `state` einen von drei Texten ab.
#
# Eine Anzeige ist `"inside"`, wenn der Betrag der Abweichung vom Referenzwert höchstens die Toleranz ist. `"high"` und `"low"` gelten nur außerhalb der Toleranz. Liegt die Anzeige dann über dem Referenzwert, ist das Ergebnis `"high"`, sonst `"low"`.
#
# Für `reading = 20.2`, `reference = 20.0` und `tolerance = 0.5` ist das Ergebnis `"inside"`. Dieselben Grenzen liefern für 21,0 den Text `"high"` und für 19,0 den Text `"low"`. Schreibe die Verzweigung einmal. Die Lösung unten probiert alle drei Anzeigen.

# gegeben:
reading = 20.2
reference = 20.0
tolerance = 0.5
difference = abs(reading - reference)

# lösung ab hier:
if :
    state =
elif :
    state =
else:
    state =
print("exercise", state)

# Lösung

reference = 20.0
tolerance = 0.5
reading = 20.2
difference = abs(reading - reference)
if difference <= tolerance:
    state = "inside"
elif reading > reference:
    state = "high"
else:
    state = "low"
print("solution", reading, state)
reading = 21.0
difference = abs(reading - reference)
if difference <= tolerance:
    state = "inside"
elif reading > reference:
    state = "high"
else:
    state = "low"
print("solution", reading, state)
reading = 19.0
difference = abs(reading - reference)
if difference <= tolerance:
    state = "inside"
elif reading > reference:
    state = "high"
else:
    state = "low"
print("solution", reading, state)

# Weiter mit `tag2/09_schleifen.ipynb`.
