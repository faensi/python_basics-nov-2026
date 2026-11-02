"""Conversions, shared references, in-place methods, copy, and deepcopy.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 07_konvertierung_referenzen_kopien.md.
"""

import copy


def celsius_from_text(text):
    """Return text as a floating-point temperature.

    Exercise stub. The task is in the markdown file.
    """
    return None


def sorted_snapshot(values):
    """Return a sorted shallow copy and leave values unchanged.

    Exercise stub. The task is in the markdown file.
    """
    return None


def independent_groups(groups):
    """Return a deep copy of a nested list.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_celsius_from_text(text):
    """Return text as a floating-point temperature."""
    return float(text)


def solution_sorted_snapshot(values):
    """Return a sorted shallow copy and leave values unchanged."""
    snapshot = copy.copy(values)
    snapshot.sort()
    return snapshot


def solution_independent_groups(groups):
    """Return a deep copy of a nested list."""
    return copy.deepcopy(groups)


def check_copies():
    """Print ok when conversion and both copies match the task."""
    number = celsius_from_text("18.6")
    number_ok = number == solution_celsius_from_text("18.6") and isinstance(number, float)
    numbers = [22.0, 17.5, 19.5]
    numbers_before = [22.0, 17.5, 19.5]
    actual_numbers = sorted_snapshot(numbers)
    expected_numbers = solution_sorted_snapshot([22.0, 17.5, 19.5])
    numbers_ok = (
        actual_numbers == expected_numbers
        and numbers == numbers_before
        and actual_numbers is not numbers
    )
    groups = [["hall", 19.2], ["lab", 22.0]]
    actual_groups = independent_groups(groups)
    groups[0][1] = 25.0
    groups.append(["store", 17.0])
    expected_groups = [["hall", 19.2], ["lab", 22.0]]
    groups_ok = actual_groups == expected_groups
    if number_ok and numbers_ok and groups_ok:
        print("ok")
    else:
        print("number expected", 18.6, "got", number)
        print("numbers expected", expected_numbers, "got", actual_numbers)
        print("groups expected", expected_groups, "got", actual_groups)


def main():
    """Show conversion, aliasing, in-place methods, and copies."""
    # --- conversions ---
    number = int("20")
    text = str(number)
    print("int to str", text, type(text).__name__)
    print("str to float", float("20.5"))
    print("float to int truncates", int(20.9))
    reading_map = {"bath": 20.1, "room": 21.5}
    as_pairs = list(reading_map.items())
    restored = dict(as_pairs)
    print("pairs", sorted(as_pairs))
    print("restored", sorted(restored.items()))

    # --- shared references ---
    first = [20.2, 19.8, 20.0]
    second = first
    second.append(21.0)
    print("shared list", first)

    # --- in-place methods ---
    print("sorted leaves the source", sorted(first), first)
    print("list.sort returns", first.sort())
    print("source after sort", first)

    # --- copy and deepcopy ---
    groups = [["bath", 20.1], ["room", 21.5]]
    alias = groups
    shallow = copy.copy(groups)
    deep = copy.deepcopy(groups)
    alias[0][1] = 25.0
    alias.append(["probe", 18.0])
    print("alias", alias)
    print("shallow shares inner lists", shallow)
    print("deep stays independent", deep)


if __name__ == "__main__":
    main()
