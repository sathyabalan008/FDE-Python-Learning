# Topic 01: Introduction to Python Programming
#Exercise 01: Dynamic Typing

x = 5

print("x is", type(x).__name__)

x = "five"

print("x is", type(x).__name__)

# Exercise 02: Python Readability

features = ["Simple","Free","Portable"]

for feature in features:
    print("Feature:", feature)

#Exercise 03: Big Integers
print(2 ** 100)

# Exercise 04: Batteries Included

import math
print("sqrt(16) =", math.sqrt(16))
