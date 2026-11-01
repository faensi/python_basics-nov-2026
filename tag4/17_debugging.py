"""A small wrong result to inspect in the Spyder debugger.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 17_debugging.md.

mean_without_ends is wrong on purpose. The reference is
solution_mean_without_ends.
"""


def mean_without_ends(values):
    """Return the mean of every value except the last one.

    The slice below is intentionally wrong.
    """
    chosen = values[1:]
    return sum(chosen) / len(chosen)


def solution_mean_without_ends(values):
    """Return the mean of every value except the last one."""
    chosen = values[:-1]
    return sum(chosen) / len(chosen)


def check_mean_without_ends():
    """Print ok when the buggy function has been corrected."""
    sample = [1.0, 2.0, 3.0, 4.0]
    actual = mean_without_ends(sample)
    expected = solution_mean_without_ends(sample)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Print the wrong mean and the expected mean."""
    sample = [1.0, 2.0, 3.0, 4.0]
    print("sample", sample)
    print("buggy result", mean_without_ends(sample))
    print("expected", solution_mean_without_ends(sample))
    print("Set a breakpoint on the return line of mean_without_ends.")


if __name__ == "__main__":
    main()
