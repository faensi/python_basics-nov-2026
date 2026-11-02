"""Helpers for a short series of temperature readings.

Imported by tag3/15_eigene_module.py.
"""


def mean(values):
    """Return the arithmetic mean of a non-empty series of numbers."""
    return sum(values) / len(values)


def deviation(reading, reference):
    """Return the reading minus the reference value."""
    return reading - reference


def within_tolerance(reading, reference, tolerance):
    """Return True when reading stays within tolerance of reference."""
    return abs(deviation(reading, reference)) <= tolerance


def celsius_to_kelvin(celsius):
    """Convert a Celsius temperature to kelvin."""
    return celsius + 273.15
