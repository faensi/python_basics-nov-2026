"""Iterables and iterators.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 05_iteratoren.md.
"""


def first_two(values):
    """Return the first two values by asking an iterator twice.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_first_two(values):
    """Return the first two values by asking an iterator twice."""
    iterator = iter(values)
    first = next(iterator)
    second = next(iterator)
    return first, second


def check_first_two():
    """Print ok when first_two matches the reference on a new series."""
    sample = [18.2, 18.6, 19.0, 19.4]
    actual = first_two(sample)
    expected = solution_first_two(sample)
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
