"""Conversions, shared references, in-place methods, copy, and deepcopy.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 07_konvertierung_referenzen_kopien.md.
"""

import copy

number = int("20")
text = str(number)
print("int to str", text, type(text).__name__)
print("str to float", float("20.5"))
print("float to int truncates", int(20.9))
reading_map = {"bath": 20.1, "room": 21.5}
as_pairs = list(reading_map.items())
restored = dict(as_pairs)
print("pairs", sorted(as_pairs))
print("restored", sorted(restored.items()))

first = [20.2, 19.8, 20.0]
second = first
second.append(21.0)
print("shared list", first)

print("sorted leaves the source", sorted(first), first)
print("list.sort returns", first.sort())
print("source after sort", first)

groups = [["bath", 20.1], ["room", 21.5]]
alias = groups
shallow = copy.copy(groups)
deep = copy.deepcopy(groups)
alias[0][1] = 25.0
alias.append(["probe", 18.0])
print("alias", alias)
print("shallow shares inner lists", shallow)
print("deep stays independent", deep)

# Exercise: turn the text into a decimal, sort a shallow copy of numbers,
# and keep a deep copy of log.
text_celsius = "18.6"
numbers = [22.0, 17.5, 19.5]
log = [["hall", 19.2], ["lab", 22.0]]
