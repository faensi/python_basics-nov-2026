"""Dictionaries, sets, and frozensets.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 06_dictionaries_sets.md.
"""

readings = {"bath": 20.1, "room": 21.5}
readings["probe"] = 18.7
print("bath", readings["bath"])
print("keys", sorted(readings))
print("values", sorted(readings.values()))
print("items", sorted(readings.items()))

names = ["bath", "room", "bath", "bath"]
unique = set(names)
frozen = frozenset(names)
# Set order is not part of the result, so print a sorted list.
print("unique", sorted(unique))
print("bath in frozen", "bath" in frozen)
print("equal contents", unique == set(frozen))

# Exercise: your own dictionary, then the distinct names in places.
places = ["hall", "lab", "hall", "store"]
