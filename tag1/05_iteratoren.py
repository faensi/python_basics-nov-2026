"""Iterables and iterators.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 05_iteratoren.md.
"""


def first_value(values):
    """Return the first value by asking an iterator once.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_first_value(values):
    """Return the first value by asking an iterator once."""
    iterator = iter(values)
    return next(iterator)


def check_first_value():
    """Print ok when first_value matches the reference."""
    sample = [19.8, 20.1, 19.9]
    actual = first_value(sample)
    expected = solution_first_value(sample)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Show iter and next, then one for-loop that uses the same protocol."""
    readings = [19.8, 20.1, 19.9]
    print("list is iterable", hasattr(readings, "__iter__"))
    iterator = iter(readings)
    print("iterator type", type(iterator).__name__)
    print("next", next(iterator))
    print("next", next(iterator))
    print("next", next(iterator))

    # A for-loop asks for an iterator and then for the next value.
    # The loop syntax itself is taught on day 2.
    print("via for:")
    for reading in readings:
        print(reading)


if __name__ == "__main__":
    main()
