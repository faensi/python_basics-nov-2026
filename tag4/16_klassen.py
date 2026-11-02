"""A short introduction to classes.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 16_klassen.md.
"""


class Reading:
    """One temperature reading from a named sensor."""

    def __init__(self, sensor, celsius):
        """Store the sensor name and the Celsius value on this instance."""
        self.sensor = sensor
        self.celsius = celsius

    def deviation(self, reference):
        """Return this reading minus the reference value."""
        return self.celsius - reference

    def kelvin(self):
        """Return this reading converted to kelvin."""
        return self.celsius + 273.15

    def is_within(self, reference, tolerance):
        """Return True when this reading stays inside tolerance.

        Exercise stub. The task is in the markdown file.
        """
        return None


def solution_is_within(reading, reference, tolerance):
    """Return True when reading stays inside tolerance of reference."""
    return abs(reading.deviation(reference)) <= tolerance


def check_is_within():
    """Print ok when Reading.is_within matches the reference."""
    reading = Reading("bath", 20.4)
    actual = reading.is_within(20.0, 0.5)
    expected = solution_is_within(reading, 20.0, 0.5)
    outside = Reading("bath", 21.0).is_within(20.0, 0.5)
    outside_expected = solution_is_within(Reading("bath", 21.0), 20.0, 0.5)
    if actual == expected and outside == outside_expected:
        print("ok")
    else:
        print("expected", expected, outside_expected, "got", actual, outside)


def main():
    """Create two instances and call the methods from the lesson."""
    bath = Reading("bath", 20.1)
    room = Reading("room", 21.5)
    print("class", Reading.__name__)
    print("instance class", type(bath).__name__)
    print("bath sensor", bath.sensor)
    print("room sensor", room.sensor)
    print("bath deviation", bath.deviation(20.0))
    print("bath kelvin", bath.kelvin())
    room.celsius = 21.6
    print("bath celsius still", bath.celsius)
    print("room celsius", room.celsius)


if __name__ == "__main__":
    main()
