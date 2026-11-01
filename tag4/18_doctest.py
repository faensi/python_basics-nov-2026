"""Systematic checks with the doctest module.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 18_doctest.md.

From this_course you can also run:

    python -m doctest tag4/18_doctest.py
"""


def mean(values):
    """Return the arithmetic mean of a non-empty series.

    >>> mean([20.0, 22.0])
    21.0
    >>> mean([20.0])
    20.0
    >>> mean([])
    Traceback (most recent call last):
    ...
    ValueError: values must not be empty
    """
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def format_deviation(reading, reference):
    """Return the signed deviation with one decimal place.

    >>> format_deviation(21.0, 20.0)
    '+1.0'
    >>> format_deviation(19.0, 20.0)
    '-1.0'
    >>> format_deviation(20.0, 20.0)
    '+0.0'
    """
    difference = round(reading - reference, 1)
    return "{:+.1f}".format(difference)


def within_tolerance(reading, reference, tolerance):
    """Return True when the absolute deviation stays within tolerance.

    >>> within_tolerance(20.4, 20.0, 0.5)
    True
    >>> within_tolerance(20.5, 20.0, 0.5)
    True
    >>> within_tolerance(20.6, 20.0, 0.5)
    False
    """
    if tolerance < 0:
        raise ValueError("tolerance must not be negative")
    return abs(reading - reference) <= tolerance


def main():
    """Run the docstring examples in this module."""
    import doctest

    failures, tests = doctest.testmod(verbose=False)
    print("doctest: {0} tests, {1} failures".format(tests, failures))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
