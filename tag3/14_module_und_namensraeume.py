"""Imports, namespaces, scopes, and help text.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 14_module_und_namensraeume.md.
"""

import csv
import math
import math as m
from math import fabs


def spread(low, high):
    """Return the absolute difference of two readings.

    Exercise stub. The task is in the markdown file.
    Use the math module.
    """
    return None


def solution_spread(low, high):
    """Return the absolute difference of two readings."""
    return math.fabs(high - low)


def check_spread():
    """Print ok when spread matches the reference."""
    actual = spread(19.5, 21.0)
    expected = solution_spread(19.5, 21.0)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def load_celsius(path, sensor):
    """Return Celsius values for sensor using the csv module."""
    selected = []
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["sensor"] == sensor:
                selected.append(float(row["celsius"]))
    return selected


def first_above(values, limit):
    """Return 'above' or 'inside'. Assignment to status stays local."""
    status = "inside"
    for value in values:
        if value > limit:
            status = "above"
            break
    return status


def main():
    """Show three import forms, a local name, and a csv load."""
    print("math.fabs", math.fabs(-0.4))
    print("m.fabs", m.fabs(-0.4))
    print("fabs", fabs(-0.4))
    print("doc", math.fabs.__doc__.splitlines()[0])

    limit = 21.0
    print("limit outside", limit)
    print("status", first_above([20.0, 21.4], limit))
    print("limit still", limit)

    bath = load_celsius("data/readings.csv", "bath")
    print("bath count", len(bath))
    print("bath spread", math.fabs(max(bath) - min(bath)))


if __name__ == "__main__":
    main()
