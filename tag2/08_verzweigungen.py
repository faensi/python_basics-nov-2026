"""Branches with if, elif, and else.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 08_verzweigungen.md.
"""


def status(reading, reference, tolerance):
    """Return inside, high, or low for one reading.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_status(reading, reference, tolerance):
    """Return inside, high, or low for one reading."""
    difference = abs(reading - reference)
    if difference <= tolerance:
        return "inside"
    if reading > reference:
        return "high"
    return "low"


def check_status():
    """Print ok when three calibration cases match the reference."""
    inside = status(20.2, 20.0, 0.5)
    high = status(21.0, 20.0, 0.5)
    low = status(19.0, 20.0, 0.5)
    expected = ("inside", "high", "low")
    actual = (inside, high, low)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Show a three-way branch and combined comparisons."""
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
    print("difference", difference)


if __name__ == "__main__":
    main()
