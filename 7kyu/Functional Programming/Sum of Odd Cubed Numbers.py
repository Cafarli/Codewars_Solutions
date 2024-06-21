"""
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.
"""
def cube_odd(arr):
    return None if any([type(x)!=int for x in arr]) else sum([x**3 for x in arr if x%2!=0])
