"""What Python is, and a first runnable script.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 00_python_ueberblick.md.
"""


def temperature_span(high, low):
    """Return how far high is above low.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_temperature_span(high, low):
    """Return how far high is above low."""
    return high - low


def check_temperature_span():
    """Print ok when temperature_span matches the reference."""
    actual = temperature_span(21.5, 19.5)
    expected = solution_temperature_span(21.5, 19.5)
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


def main():
    """Print a few expressions and the Zen of Python."""
    print("Hello, Python")
    print("sum:", 19.5 + 2.0)
    reading = 20.1
    limit = 20.0
    # Indentation groups the branch. There are no braces.
    if reading > limit:
        print("state: above the limit")
    else:
        print("state: at or below the limit")
    print("Zen of Python:")
    import this


if __name__ == "__main__":
    main()
