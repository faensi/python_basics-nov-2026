"""Defining and calling functions.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 10_funktionen.md.
"""


def mean(values):
    """Return the arithmetic mean of a non-empty series.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_mean(values):
    """Return the arithmetic mean of a non-empty series."""
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def check_mean():
    """Print ok when mean matches the reference."""
    sample = [20.0, 21.0, 22.0]
    actual = mean(sample)
    expected = solution_mean(sample)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def announce(sensor):
    """Print a label and return None, because there is no return."""
    print("sensor", sensor)


def main():
    """Show a call, a return value, and a function that returns None."""
    readings = [20.0, 21.0, 22.0]
    total = sum(readings)
    average = total / len(readings)
    print("inline mean", average)
    result = announce("bath")
    print("announce returns", result)


if __name__ == "__main__":
    main()
