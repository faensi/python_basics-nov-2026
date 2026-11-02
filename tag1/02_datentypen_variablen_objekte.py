"""Types, classes, variables, and objects.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 02_datentypen_variablen_objekte.md.
"""


def own_binding():
    """Return your own names, including one name bound to a new value.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_own_binding():
    """Return one valid set of names with celsius bound again."""
    count = 5
    celsius = 18.4
    label = "hall"
    valid = False
    missing = None
    earlier = celsius
    celsius = 19.0
    return label, count, earlier, celsius, valid, missing


def _own_binding_ok(result):
    """Return whether result follows the variable exercise."""
    if not isinstance(result, tuple) or len(result) != 6:
        return False
    label, count, earlier, celsius, valid, missing = result
    if not isinstance(label, str) or label.strip() == "" or label == "bath":
        return False
    if isinstance(count, bool) or not isinstance(count, int) or count == 3:
        return False
    if isinstance(earlier, bool) or not isinstance(earlier, float) or earlier == 20.1:
        return False
    if isinstance(celsius, bool) or not isinstance(celsius, float) or celsius == 20.1:
        return False
    if earlier == celsius:
        return False
    if not isinstance(valid, bool):
        return False
    if missing is not None:
        return False
    return True


def check_own_binding():
    """Print ok when own_binding defines the asked kinds of values."""
    actual = own_binding()
    if not _own_binding_ok(actual):
        print(
            "expected label, count, earlier, celsius, valid, missing; got",
            actual,
        )
        return
    if not _own_binding_ok(solution_own_binding()):
        print("solution does not match the task")
        return
    print("ok")


def main():
    """Show basic types and rebinding of a name."""
    count = 3
    celsius = 20.1
    label = "bath"
    valid = True
    missing = None
    print("count", count, type(count).__name__)
    print("celsius", celsius, type(celsius).__name__)
    print("label", label, type(label).__name__)
    print("valid", valid, type(valid).__name__)
    print("missing", missing, type(missing).__name__)

    # A name refers to an object. Binding the name again leaves the old object.
    earlier = celsius
    celsius = 21.0
    print("earlier", earlier)
    print("celsius", celsius)

    # The same name can refer to an object of another type.
    value = 20
    print("value as number", value, type(value).__name__)
    value = "bath"
    print("value as text", value, type(value).__name__)


if __name__ == "__main__":
    main()
