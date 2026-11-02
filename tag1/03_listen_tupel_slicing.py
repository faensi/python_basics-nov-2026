"""Lists, tuples, and slicing.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 03_listen_tupel_slicing.md.
"""


def own_readings():
    """Return your own list and a tuple of its first and last values.

    Exercise stub. The task is in the markdown file.
    """
    return None


def second_and_third(values):
    """Return the second and third values as a new list.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_own_readings():
    """Return one valid list and the tuple of its ends."""
    readings = [18.0, 18.5, 17.9, 19.2]
    readings.append(18.8)
    ends = (readings[0], readings[-1])
    return readings, ends


def solution_second_and_third(values):
    """Return the second and third values as a new list."""
    return values[1:3]


def _own_readings_ok(result):
    """Return whether result is a long enough own list plus its ends."""
    lesson = [19.8, 20.1, 19.9, 20.0, 20.2]
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    readings, ends = result
    if not isinstance(readings, list) or len(readings) < 5:
        return False
    if readings[:5] == lesson:
        return False
    for item in readings:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return False
    if not isinstance(ends, tuple) or ends != (readings[0], readings[-1]):
        return False
    return True


def check_slices():
    """Print ok when the list is your own and the slice matches."""
    built = own_readings()
    if not _own_readings_ok(built):
        print("expected your list and a tuple of its ends; got", built)
        return
    if not _own_readings_ok(solution_own_readings()):
        print("solution does not match the task")
        return
    sample = [18.0, 18.4, 19.1, 17.6]
    actual = second_and_third(sample)
    expected = solution_second_and_third(sample)
    if actual != expected:
        print("second and third expected", expected, "got", actual)
        return
    print("ok")


def main():
    """Show list and tuple indexing and slicing."""
    readings = [19.8, 20.1, 19.9, 20.0, 20.2]
    # A tuple keeps a short fixed record. It has no append.
    start_end = (19.8, 20.2)
    start, end = start_end
    print("start", start, "end", end)

    readings.append(20.3)
    print("after append", readings)
    print("first", readings[0])
    print("last", readings[-1])
    print("slice 1:4", readings[1:4])
    print("prefix", readings[:3])
    print("suffix", readings[-2:])
    print("every second", readings[::2])
    # A slice is a new list. The source list stays as it is.
    prefix = readings[:3]
    prefix.append(0.0)
    print("prefix after its own append", prefix)
    print("readings unchanged by that append", readings)


if __name__ == "__main__":
    main()
