"""Helpers for a short series of temperature readings.

The lesson that uses this module is 15_eigene_module.md.
"""


def mean(values):
    """Return the arithmetic mean of a non-empty series of numbers."""
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def deviation(reading, reference):
    """Return the reading minus the reference value."""
    return reading - reference


def within_tolerance(reading, reference, tolerance):
    """Return True when reading stays within tolerance of reference."""
    if tolerance < 0:
        raise ValueError("tolerance must not be negative")
    return abs(deviation(reading, reference)) <= tolerance


def celsius_to_kelvin(celsius):
    """Convert a Celsius temperature to kelvin."""
    return celsius + 273.15


if __name__ == "__main__":
    sample = [20.0, 21.0, 22.0]
    print("mean", mean(sample))
    print("kelvin", celsius_to_kelvin(20.0))
