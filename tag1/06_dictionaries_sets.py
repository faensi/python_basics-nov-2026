"""Dictionaries, sets, and frozensets.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 06_dictionaries_sets.md.
"""


def unique_sensors(names):
    """Return the distinct names as a frozenset.

    Exercise stub. The task is in the markdown file.
    """
    return None


def lookup_reading(readings, sensor):
    """Return the value stored for sensor.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_unique_sensors(names):
    """Return the distinct names as a frozenset."""
    return frozenset(names)


def solution_lookup_reading(readings, sensor):
    """Return the value stored for sensor."""
    return readings[sensor]


def check_mappings():
    """Print ok when both exercise functions match the reference."""
    names = ["bath", "room", "bath"]
    readings = {"bath": 20.1, "room": 21.5}
    actual_names = unique_sensors(names)
    expected_names = solution_unique_sensors(names)
    actual_reading = lookup_reading(readings, "bath")
    expected_reading = solution_lookup_reading(readings, "bath")
    if actual_names == expected_names and actual_reading == expected_reading:
        print("ok")
    else:
        print("names expected", expected_names, "got", actual_names)
        print("reading expected", expected_reading, "got", actual_reading)


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
