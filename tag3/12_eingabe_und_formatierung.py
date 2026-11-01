"""input, percent formatting, and str.format.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 12_eingabe_und_formatierung.md.

demo_input waits for the keyboard. Call it from the IPython console.
F5 does not call it.
"""


def format_line(sensor, celsius):
    """Return a line such as 'bath: 20.0 C' using percent formatting.

    Exercise stub. The task is in the markdown file.
    """
    return None


def format_line_method(sensor, celsius):
    """Return the same line using the format method.

    Exercise stub. The task is in the markdown file.
    """
    return None


def parse_reading(text):
    """Return the float stored in text.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_format_line(sensor, celsius):
    """Return a line such as 'bath: 20.0 C' using percent formatting."""
    return "%s: %.1f C" % (sensor, celsius)


def solution_format_line_method(sensor, celsius):
    """Return the same line using the format method."""
    return "{}: {:.1f} C".format(sensor, celsius)


def solution_parse_reading(text):
    """Return the float stored in text."""
    return float(text.strip())


def check_formatting():
    """Print ok when both lines and the parsed number match."""
    line = format_line("bath", 20.0)
    method_line = format_line_method("bath", 20.0)
    number = parse_reading(" 20.5 ")
    lines_ok = line == solution_format_line("bath", 20.0)
    method_ok = method_line == solution_format_line_method("bath", 20.0)
    number_ok = number == solution_parse_reading(" 20.5 ")
    if lines_ok and method_ok and number_ok:
        print("ok")
    else:
        print("percent", line)
        print("format", method_line)
        print("number", number)


def demo_input():
    """Read one temperature from the IPython console and print it."""
    text = input("Temperature in C: ")
    print(solution_parse_reading(text))


def main():
    """Show percent formatting and the format method."""
    sensor = "bath"
    celsius = 20.1
    percent_line = "%s: %.1f C" % (sensor, celsius)
    format_line_text = "{}: {:.1f} C".format(sensor, celsius)
    print("percent:", percent_line)
    print("format:", format_line_text)
    print("same text:", percent_line == format_line_text)
    print("Call demo_input() in the console when you want to type a value.")


if __name__ == "__main__":
    main()
