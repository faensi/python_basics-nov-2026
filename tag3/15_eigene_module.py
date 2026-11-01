"""Import a module that lives next to this script.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 15_eigene_module.md.
"""

import measurement


def summary(values, reference, tolerance):
    """Return the mean and whether that mean is inside the tolerance.

    Exercise stub. The task is in the markdown file.
    Use measurement.mean and measurement.within_tolerance.
    """
    return None


def solution_summary(values, reference, tolerance):
    """Return the mean and whether that mean is inside the tolerance."""
    average = measurement.mean(values)
    return {
        "mean": average,
        "within": measurement.within_tolerance(average, reference, tolerance),
    }


def check_summary():
    """Print ok when summary matches the reference."""
    sample = [20.0, 21.0, 22.0]
    actual = summary(sample, 21.0, 0.5)
    expected = solution_summary(sample, 21.0, 0.5)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Call the course module and show its docstring."""
    readings = [20.0, 21.0, 22.0]
    print("mean", measurement.mean(readings))
    print("deviation", measurement.deviation(21.4, 21.0))
    print("within", measurement.within_tolerance(21.4, 21.0, 0.5))
    print("kelvin", measurement.celsius_to_kelvin(20.0))
    print("doc:", measurement.mean.__doc__)


if __name__ == "__main__":
    main()
