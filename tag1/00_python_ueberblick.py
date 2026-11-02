"""What Python is, and a first runnable script.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 00_python_ueberblick.md.
"""

def own_values():
    """Return your own text, decimal temperature, and whole-number count.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_own_values():
    """Return one valid text, decimal temperature, and whole-number count."""
    sensor = "hall"
    celsius = 18.5
    count = 4
    return sensor, celsius, count


def _own_values_ok(result):
    """Return whether result is a non-empty text, a float, and an int."""
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    sensor, celsius, count = result
    if not isinstance(sensor, str) or sensor.strip() == "":
        return False
    if isinstance(celsius, bool) or not isinstance(celsius, float):
        return False
    if isinstance(count, bool) or not isinstance(count, int):
        return False
    return True


def check_own_values():
    """Print ok when own_values returns text, float, and int."""
    actual = own_values()
    if not _own_values_ok(actual):
        print("expected a text, a decimal number, and a whole number; got", actual)
        return
    if not _own_values_ok(solution_own_values()):
        print("solution does not match the task")
        return
    print("ok")


def main():
    """Print a few expressions and the Zen of Python."""
    print("Hello, Python")
    print("sum:", 19.5 + 2.0)
    print("sum:", "19.5" + "2.0")
    reading = 20.1
    limit = 20.0
    # Indentation groups the branch. There are no braces.
    if reading > limit:
        print("state: above the limit")
    else:
        print("state: at or below the limit")
    print("Zen of Python:")
    
if __name__ == "__main__":
    main()
