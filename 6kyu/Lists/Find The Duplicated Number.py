"""
Spin-off of this kata, here you will have to figure out an efficient strategy to solve the problem of 
finding the sole duplicate number among an unsorted array/list of numbers starting from 1 up to n.
"""

def find_dup(arr):
    return list(filter(lambda x: arr.count(x)>1, arr))[0]
