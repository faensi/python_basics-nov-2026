"""Lists, tuples, and slicing.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 03_listen_tupel_slicing.md.
"""

readings = [19.8, 20.1, 19.9, 20.0, 20.2]
# A tuple keeps a short fixed record. It has no append.
start_end = (19.8, 20.2)
start, end = start_end
print("start", start, "end", end)

readings.append(20.3)
print("after append", readings)
print("first", readings[0])
print("last", readings[-1])
print("slice 1:4", readings[1:4])
print("prefix", readings[:3])
print("suffix", readings[-2:])
print("every second", readings[::2])
# A slice is a new list. The source list stays as it is.
prefix = readings[:3]
prefix.append(0.0)
print("prefix after its own append", prefix)
print("readings unchanged by that append", readings)

# Exercise: your own list, one append, a tuple of the ends,
# and the second and third values of sample.
sample = [18.0, 18.4, 19.1, 17.6]
