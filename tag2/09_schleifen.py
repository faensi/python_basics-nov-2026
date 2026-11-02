"""while, for, the index loop, continue, break, else, and pass.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 09_schleifen.md.
"""


def count_until_above(values, limit):
    """Return how many leading values stay at or below limit.

    Exercise stub. The task is in the markdown file.
    Stop at the first value above limit.
    """
    return None


def solution_count_until_above(values, limit):
    """Return how many leading values stay at or below limit."""
    count = 0
    for value in values:
        if value > limit:
            break
        count = count + 1
    return count


def check_count_until_above():
    """Print ok when the count stops at the first value above the limit."""
    sample = [20.0, 20.2, 21.0, 19.0]
    actual = count_until_above(sample, 20.5)
    expected = solution_count_until_above(sample, 20.5)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Show while, for, range, continue, break, else, and pass."""
    readings = [19.0, 20.0, 21.0]

    print("while:")
    index = 0
    while index < len(readings):
        print(index, readings[index])
        index = index + 1

    # This is the Python form of a C or C++ index loop.
    print("range:")
    for index in range(len(readings)):
        print(index, readings[index])

    print("for:")
    for reading in readings:
        print(reading)

    print("continue skips a missing value:")
    series = [20.0, None, 21.0]
    for reading in series:
        if reading is None:
            continue
        print(reading)

    print("break and else:")
    limit = 22.0
    for reading in readings:
        if reading > limit:
            print("stopped at", reading)
            break
    else:
        print("no value above the limit")

    # pass holds a place while a branch is still empty.
    for reading in readings:
        if reading < 0:
            pass
        else:
            print("kept", reading)


if __name__ == "__main__":
    main()
