"""Lists, tuples, and slicing.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 03_listen_tupel_slicing.md.
"""


def middle_readings(values):
    """Return every value except the first and the last.

    Exercise stub. The task is in the markdown file.
    """
    return None


def last_three(values):
    """Return the last three values.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_middle_readings(values):
    """Return every value except the first and the last."""
    return values[1:-1]


def solution_last_three(values):
    """Return the last three values."""
    return values[-3:]


def check_slices():
    """Print ok when both exercise functions match the reference."""
    sample = [19.8, 20.1, 19.9, 20.0, 20.2]
    actual_middle = middle_readings(sample)
    expected_middle = solution_middle_readings(sample)
    actual_tail = last_three(sample)
    expected_tail = solution_last_three(sample)
    if actual_middle == expected_middle and actual_tail == expected_tail:
        print("ok")
    else:
        print("middle expected", expected_middle, "got", actual_middle)
        print("last three expected", expected_tail, "got", actual_tail)


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
