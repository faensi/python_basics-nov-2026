"""Types, classes, variables, and objects.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 02_datentypen_variablen_objekte.md.
"""


def describe(value):
    """Return the type name of value.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_describe(value):
    """Return the type name of value."""
    return type(value).__name__


def check_describe():
    """Print ok when describe matches the reference on five values."""
    actual = [
        describe(20.1),
        describe(3),
        describe("bath"),
        describe(True),
        describe(None),
    ]
    expected = ["float", "int", "str", "bool", "NoneType"]
    if actual == expected:
        print("ok")
    else:
        print("expected", expected, "got", actual)


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
