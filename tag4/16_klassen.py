# Kurze Einführung in Klassen
#
# Tag 4, Einheit 16
# Skript: `tag4/16_klassen.py`
#
# Ziel
#
# Du definierst eine Klasse mit Konstruktor und einer Methode, erzeugst zwei Instanzen und hältst deren Daten auseinander.
#
# Arbeitsverzeichnis: `python_basics-nov-2026`. Skript mit F5, oder die Zellen von oben nach unten.
#
# Das ist eine kurze Einführung. Vererbung, besondere Methodennamen über `__init__` hinaus und Entwurfsmuster gehören nicht zu diesem Kurs.

# Klasse und Instanz
#
# Am Tag 1 war `float` die Klasse der Temperaturzahl. `Reading` ist eine Klasse, die du selbst schreibst. Ein Aufruf `Reading("bath", 20.1)` erzeugt eine Instanz. `bath` und `room` sind zwei Instanzen.
#
# `__init__` richtet eine neue Instanz ein. `self` ist diese Instanz. `self.sensor` und `self.celsius` gehören zu ihr, nicht zur Klasse insgesamt.
#
# Wenn du danach `room.celsius = 21.6` setzt, steht `bath.celsius` noch auf 20,1. Die Zuweisung hat nur `room` getroffen.

# Methode
#
# `deviation` und `kelvin` sind Methoden. Der Aufruf `bath.deviation(20.0)` übergibt `bath` als `self`. `kelvin` addiert 273,15. Für 20,1 Grad Celsius ist das 293,25.

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

# Übung
#
# Ergänze in der Klasse die Methode `is_within(self, reference, tolerance)`. Sie gibt `True` zurück, wenn der Betrag der Abweichung höchstens die Toleranz ist. Nutze `self.deviation`.
#
# `Reading("bath", 20.4).is_within(20.0, 0.5)` ist `True`. `Reading("bath", 21.0).is_within(20.0, 0.5)` ist `False`.
#
# Die Methoden davor sind vorgegeben. Schreibe nur den Körper von `is_within`.

# gegeben:
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

    # lösung ab hier:
    def is_within(self, reference, tolerance):
        difference =
        return difference <= tolerance


print("exercise", Reading("bath", 20.4).is_within(20.0, 0.5))

# Lösung

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

    def is_within(self, reference, tolerance):
        return abs(self.deviation(reference)) <= tolerance

print("solution", Reading("bath", 20.4).is_within(20.0, 0.5))
print("solution", Reading("bath", 21.0).is_within(20.0, 0.5))

# Weiter mit `tag4/17_debugging.ipynb`.
