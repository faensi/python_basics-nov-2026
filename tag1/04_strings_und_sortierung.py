"""String methods, sort, and sorted.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 04_strings_und_sortierung.md.
"""


def clean_label(label):
    """Return label without outer spaces and in lowercase.

    Exercise stub. The task is in the markdown file.
    """
    return None


def sorted_copy(values):
    """Return a new sorted list and leave values unchanged.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_clean_label(label):
    """Return label without outer spaces and in lowercase."""
    return label.strip().lower()


def solution_sorted_copy(values):
    """Return a new sorted list and leave values unchanged."""
    return sorted(values)


def check_strings_and_sort():
    """Print ok when the label is cleaned and the source list is unchanged."""
    label = clean_label("  Bath-01  ")
    sample = [20.2, 19.8, 20.0]
    before = [20.2, 19.8, 20.0]
    ordered = sorted_copy(sample)
    label_ok = label == solution_clean_label("  Bath-01  ")
    order_ok = ordered == solution_sorted_copy(before) and sample == before
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
