"""Types, classes, variables, and objects.

Run this file in Spyder with F5.
Set the Spyder working directory to the python_basics-nov-2026 folder.
The lesson and the exercise are in 02_datentypen_variablen_objekte.md.
"""

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

# Exercise: add your own names here. Do not reuse 3, 20.1, or "bath".
