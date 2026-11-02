"""String methods, sort, and sorted.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 04_strings_und_sortierung.md.
"""

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

# Exercise: tidy probe, and make a sorted copy of series.
probe = "  Probe-7  "
series = [21.5, 18.0, 19.2]
