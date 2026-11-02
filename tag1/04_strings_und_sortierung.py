"""String methods, sort, and sorted.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 04_strings_und_sortierung.md.
"""


def tidy_name(label):
    """Return label stripped, lowercase, with hyphens turned into underscores.

    Exercise stub. The task is in the markdown file.
    """
    return None


def ordered_copy(values):
    """Return a new sorted list and leave values unchanged.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_tidy_name(label):
    """Return label stripped, lowercase, with hyphens turned into underscores."""
    return label.strip().lower().replace("-", "_")


def solution_ordered_copy(values):
    """Return a new sorted list and leave values unchanged."""
    return sorted(values)


def check_strings_and_sort():
    """Print ok when the label is tidied and the source list is unchanged."""
    label = tidy_name("  Probe-7  ")
    sample = [21.5, 18.0, 19.2]
    before = [21.5, 18.0, 19.2]
    ordered = ordered_copy(sample)
    label_ok = label == solution_tidy_name("  Probe-7  ")
    order_ok = (
        ordered == solution_ordered_copy(before)
        and sample == before
        and ordered is not sample
    )
    if label_ok and order_ok:
        print("ok")
    else:
        print("label", label)
        print("ordered", ordered, "input", sample)


def main():
    """Show string methods and the difference between sorted and sort."""
    raw_label = "  Bath-01  "
    print("strip", raw_label.strip())
    print("lower", raw_label.strip().lower())
    print("split", "bath;room".split(";"))
    print("replace", "20.1 C".replace(" C", " celsius"))
    print("startswith", "bath".startswith("ba"))

    readings = [20.2, 19.8, 20.0]
    print("sorted copy", sorted(readings))
    print("original after sorted", readings)
    print("sort returns", readings.sort())
    print("original after sort", readings)


if __name__ == "__main__":
    main()
