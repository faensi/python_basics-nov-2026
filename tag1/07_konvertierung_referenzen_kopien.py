"""Conversions, shared references, in-place methods, copy, and deepcopy.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 07_konvertierung_referenzen_kopien.md.
"""

import copy


def sorted_snapshot(values):
    """Return a sorted copy of a flat list and leave values unchanged.

    Exercise stub. The task is in the markdown file.
    """
    return None


def independent_groups(groups):
    """Return a deep copy of a nested list.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_sorted_snapshot(values):
    """Return a sorted copy of a flat list and leave values unchanged."""
    snapshot = copy.copy(values)
    snapshot.sort()
    return snapshot


def solution_independent_groups(groups):
    """Return a deep copy of a nested list."""
    return copy.deepcopy(groups)


def check_copies():
    """Print ok when both copies are independent of later edits."""
    numbers = [20.0, 19.0, 21.0]
    numbers_before = [20.0, 19.0, 21.0]
    actual_numbers = sorted_snapshot(numbers)
    expected_numbers = solution_sorted_snapshot([20.0, 19.0, 21.0])
    groups = [["bath", 20.1], ["room", 21.5]]
    actual_groups = independent_groups(groups)
    groups[0][1] = 25.0
    expected_groups = [["bath", 20.1], ["room", 21.5]]
    numbers_ok = actual_numbers == expected_numbers and numbers == numbers_before
    groups_ok = actual_groups == expected_groups
    if numbers_ok and groups_ok:
        print("ok")
    else:
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
