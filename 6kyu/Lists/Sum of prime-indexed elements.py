"""
In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

The first element of the array is at index 0.
"""

def total(arr):
    def is_prime(x):
        if x==0 or x==1:
            return False
        for i in range(2, x//2+1):
            if x%i==0:
                return False
        return True
    summ = 0
    for i,v in enumerate(arr):
        if is_prime(i):
            summ += v
    return summ
