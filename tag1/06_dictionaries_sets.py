"""Dictionaries, sets, and frozensets.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 06_dictionaries_sets.md.
"""


def own_map():
    """Return your own reading dict and one value stored in it.

    Exercise stub. The task is in the markdown file.
    """
    return None


def places_once(names):
    """Return the distinct names as a frozenset.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_own_map():
    """Return one valid reading dict and the value added last."""
    readings = {"hall": 19.2, "lab": 22.0, "office": 21.1}
    readings["store"] = 17.5
    stored = readings["store"]
    return readings, stored


def solution_places_once(names):
    """Return the distinct names as a frozenset."""
    return frozenset(names)


def _own_map_ok(result):
    """Return whether result is an own dict plus one of its values."""
    lesson_names = {"bath", "room", "probe"}
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    readings, stored = result
    if not isinstance(readings, dict) or len(readings) < 4:
        return False
    for key, value in readings.items():
        if not isinstance(key, str) or key in lesson_names:
            return False
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False
    if isinstance(stored, bool) or not isinstance(stored, (int, float)):
        return False
    return stored in readings.values()


def check_mappings():
    """Print ok when the dict is your own and the names form a frozenset."""
    actual_map = own_map()
    if not _own_map_ok(actual_map):
        print("expected your dict and one stored value; got", actual_map)
        return
    if not _own_map_ok(solution_own_map()):
        print("solution does not match the task")
        return
    names = ["hall", "lab", "hall", "store"]
    actual_names = places_once(names)
    expected_names = solution_places_once(names)
    if type(actual_names) is not frozenset or actual_names != expected_names:
        print("names expected", expected_names, "got", actual_names)
        return
    print("ok")


def main():
    """Show dict lookup and set membership."""
    readings = {"bath": 20.1, "room": 21.5}
    readings["probe"] = 18.7
    print("bath", readings["bath"])
    print("keys", sorted(readings))
    print("values", sorted(readings.values()))
    print("items", sorted(readings.items()))

    names = ["bath", "room", "bath", "bath"]
    unique = set(names)
    frozen = frozenset(names)
    # Set order is not part of the result, so print a sorted list.
    print("unique", sorted(unique))
    print("bath in frozen", "bath" in frozen)
    print("equal contents", unique == set(frozen))


if __name__ == "__main__":
    main()
