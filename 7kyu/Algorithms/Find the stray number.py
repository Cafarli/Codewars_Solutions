"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""

# First solution
def stray(arr):
    uniq = list(set(arr))
    return uniq[0] if arr.count(uniq[0])==1 else uniq[1]

# Second solution
def stray(arr):
    return min(arr, key=arr.count) 
