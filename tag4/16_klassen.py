# Kurze Einführung in Klassen
#
# Tag 4, Einheit 16
# Skript: `tag4/16_klassen.py`
#
# Ziel
#
# Du schreibst eine eigene Klasse, legst Daten auf `self` ab, erzeugst Instanzen
# und rufst Methoden auf.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen
# von oben nach unten.
#
# Das ist eine kurze Einführung. Vererbung, besondere Methodennamen über
# `__init__` hinaus und Entwurfsmuster gehören nicht zu diesem Kurs.

# Klasse und Instanz
#
# Am Tag 1 war `float` die Klasse der Temperaturzahl. `Reading` ist eine Klasse,
# die du selbst schreibst. Ein Aufruf erzeugt eine Instanz.

text = "bath"
print(type(text).__name__)
print(type(20.1).__name__)

# Eine minimale Klasse

class Reading:
    pass

print(Reading)
print(Reading.__name__)

bath = Reading()
print(type(bath).__name__)

# `__init__` und `self`
#
# `__init__` richtet eine neue Instanz ein. `self` ist diese Instanz.

class Reading:
    """One temperature reading from a named sensor."""

    def __init__(self, sensor, celsius):
        self.sensor = sensor
        self.celsius = celsius

bath = Reading("bath", 20.1)
print(bath.sensor)
print(bath.celsius)

# Zwei Instanzen bleiben getrennt

bath = Reading("bath", 20.1)
room = Reading("room", 21.5)
print("bath", bath.sensor, bath.celsius)
print("room", room.sensor, room.celsius)
room.celsius = 21.6
print("bath still", bath.celsius)
print("room now", room.celsius)

# Methoden
#
# Beim Aufruf `bath.kelvin()` übergibt Python `bath` als `self`.

class Reading:
    """One temperature reading from a named sensor."""

    def __init__(self, sensor, celsius):
        self.sensor = sensor
        self.celsius = celsius

    def deviation(self, reference):
        """Return this reading minus the reference value."""
        return self.celsius - reference

    def kelvin(self):
        """Return this reading converted to kelvin."""
        return self.celsius + 273.15

bath = Reading("bath", 20.1)
room = Reading("room", 21.5)
print("class", Reading.__name__)
print("instance class", type(bath).__name__)
print("bath sensor", bath.sensor)
print("room sensor", room.sensor)
print("bath deviation", round(bath.deviation(20.0), 1))
print("bath kelvin", bath.kelvin())
room.celsius = 21.6
print("bath celsius still", bath.celsius)
print("room celsius", room.celsius)

# Übung 1
#
# Schreibe die Klasse `Sensor` mit `__init__(self, name)`. Lege den Namen auf
# `self.name` ab. Erzeuge eine Instanz `bath` mit dem Namen `"bath"` und gib
# `bath.name` aus.

# gegeben:
sensor_name = "bath"

# lösung ab hier:
class Sensor:
    def __init__(self, name):
        

bath =
print("exercise 1", bath.name)

# Lösung 1

class Sensor:
    def __init__(self, name):
        self.name = name

bath = Sensor("bath")
print("solution 1", bath.name)

# Übung 2
#
# Ergänze in `Reading` die Methode `label(self)`. Sie gibt einen Text der Form
# `"bath: 20.1 C"` zurück. Nutze `self.sensor`, `self.celsius` und `format`.
#
# `Reading("bath", 20.1).label()` ist `"bath: 20.1 C"`.

# gegeben:
class Reading:
    """One temperature reading from a named sensor."""

    def __init__(self, sensor, celsius):
        self.sensor = sensor
        self.celsius = celsius

    # lösung ab hier:
    def label(self):
        


print("exercise 2", Reading("bath", 20.1).label())

# Lösung 2

class Reading:
    """One temperature reading from a named sensor."""

    def __init__(self, sensor, celsius):
        self.sensor = sensor
        self.celsius = celsius

    def label(self):
        return "{}: {} C".format(self.sensor, self.celsius)

print("solution 2", Reading("bath", 20.1).label())
print("solution 2", Reading("room", 21.5).label())

# Weiter mit `tag4/17_debugging.ipynb`.
