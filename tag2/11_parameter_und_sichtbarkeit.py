"""Positional parameters, keyword parameters, and local versus global names.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 11_parameter_und_sichtbarkeit.md.
"""


def shift(reading, offset=0.0):
    """Return reading plus offset.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_shift(reading, offset=0.0):
    """Return reading plus offset."""
    adjusted = reading + offset
    return adjusted


def clip(reading, low, high):
    """Return reading limited to the closed interval from low to high."""
    if reading < low:
        return low
    if reading > high:
        return high
    return reading


def collect(reading, series=None):
    """Append reading to a new list when series is omitted."""
    if series is None:
        series = []
    series.append(reading)
    return series


def check_shift():
    """Print ok when shift uses the default and an explicit offset."""
    default = shift(20.0)
    moved = shift(20.0, offset=0.5)
    if default == solution_shift(20.0) and moved == solution_shift(20.0, offset=0.5):
        print("ok")
    else:
        print("expected", 20.0, "and", 20.5, "got", default, "and", moved)


step = 0


def shadow():
    """Bind a local name and leave the global step unchanged."""
    step = 5
    return step


def advance():
    """Add one to the global step and return the new value."""
    global step
    step = step + 1
    return step


def buggy_collect(reading, series=[]):
    """Append to one shared list. Do not use a list as a default."""
    series.append(reading)
    return series


def main():
    """Show call styles, shadowing, global, and a mutable default to avoid."""
    global step
    step = 0
    print("positional", clip(22.0, 19.0, 21.0))
    print("keyword", clip(22.0, low=19.0, high=21.0))
    print("local step", shadow())
    print("global step still", step)
    print("after advance", advance())
    print("global step now", step)
    # A new list is created on each call because None is the default.
    print("first collect", collect(20.0))
    print("second collect", collect(21.0))
    print("buggy first", buggy_collect(20.0))
    print("buggy second", buggy_collect(21.0))


if __name__ == "__main__":
    main()
