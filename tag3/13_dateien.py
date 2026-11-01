"""Read and write text files.

Run this file in Spyder with F5.
Set the Spyder working directory to the this_course folder.
The lesson and the exercise are in 13_dateien.md.
"""


def load_celsius(path, sensor):
    """Return the Celsius values of one sensor from a CSV file.

    Exercise stub. The task is in the markdown file.
    The first line of the file is a header.
    """
    return None


def write_report(path, lines):
    """Write each line plus a newline to path.

    Exercise stub. The task is in the markdown file.
    """
    return None


def solution_load_celsius(path, sensor):
    """Return the Celsius values of one sensor from a CSV file."""
    selected = []
    with open(path, encoding="utf-8") as handle:
        handle.readline()
        for line in handle:
            if not line.strip():
                continue
            _timestamp, name, celsius = line.strip().split(",")
            if name == sensor:
                selected.append(float(celsius))
    return selected


def solution_write_report(path, lines):
    """Write each line plus a newline to path."""
    with open(path, "w", encoding="utf-8") as handle:
        for line in lines:
            handle.write(line + "\n")


def read_notes(path):
    """Return the full text of a UTF-8 file."""
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def check_files():
    """Print ok when the bath series and a small report match."""
    loaded = load_celsius("data/readings.csv", "bath")
    expected = solution_load_celsius("data/readings.csv", "bath")
    write_report("data/report.txt", ["bath: 20.1 C"])
    with open("data/report.txt", encoding="utf-8") as handle:
        report = handle.read()
    if loaded == expected and report == "bath: 20.1 C\n":
        print("ok")
    else:
        print("loaded", loaded)
        print("report", report)


def main():
    """Read the sample notes and write a short report for the bath sensor."""
    print(read_notes("data/notes.txt"))
    bath = solution_load_celsius("data/readings.csv", "bath")
    lines = []
    for celsius in bath:
        lines.append("bath: {:.1f} C".format(celsius))
    solution_write_report("data/report.txt", lines)
    print("wrote data/report.txt")
    print(read_notes("data/report.txt"))


if __name__ == "__main__":
    main()
