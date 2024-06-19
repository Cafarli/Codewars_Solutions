"""
Write a function that takes as its parameters one or more numbers which are the diameters of circles.

The function should return the total area of all the circles, rounded to the nearest integer in a string that says
"We have this much circle: xyz".

You don't know how many circles you will be given, but you can assume it will be at least one.

So:

sum_circles(2) == "We have this much circle: 3"
sum_circles(2, 3, 4) == "We have this much circle: 23"
Translations and comments (and upvotes!) welcome!
"""

import math
def sum_circles(*args):
    return f"We have this much circle: {round(sum([((x/2)**2)*math.pi for x in args]))}"
