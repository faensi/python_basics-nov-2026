"""Iterables and iterators.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 05_iteratoren.md.
"""

readings = [19.8, 20.1, 19.9]
print("list is iterable", hasattr(readings, "__iter__"))
iterator = iter(readings)
print("iterator type", type(iterator).__name__)
print("next", next(iterator))
print("next", next(iterator))
print("next", next(iterator))

# A for-loop asks for an iterator and then for the next value.
# The loop syntax itself is taught on day 2.
print("via for:")
for reading in readings:
    print(reading)

# Exercise: take the first two values of series with iter and next.
series = [18.2, 18.6, 19.0, 19.4]
