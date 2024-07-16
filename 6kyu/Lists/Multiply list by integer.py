"""
Task:
Given a list of integers l, return the list with each value multiplied by integer n.

Restrictions:
The code must not:

contain *.
use eval() or exec()
contain for
modify l
"""

from operator import mul
def multiply(n, l):
    return list(map(lambda x: mul(x,n), l))
