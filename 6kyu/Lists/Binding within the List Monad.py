"""
In this kata, you must implement the Bind function for lists, or arrays. 
In haskell, the function is represented by >>=, but we'll just call it bind.

Essentially, bind should map the array with the function given, and then flatten it one time. 
Don't manipulate the original array; make you function pure: without side-effects, 
so that no variables are edited whilst the function is carried out. In dynamically typed languages,
you should throw an error if the given function does not return a list.

Here's how it should work:

bind( [1,2,3], lambda a: [a+1] )
=> [2,3,4]

bind( [1,2,3], lambda a: [[a]] )
=> [[1],[2],[3]]

bind( [1,2,3], lambda a: a )
=> # ERROR! The returned value is not a list!
"""

def bind(lst,func):
    map_lst = list(map(func, lst))
    if not all(isinstance(item, list) for item in map_lst):
        raise ValueError("The returned value is not a list!")
    flattened = [item for sublist in map_lst for item in sublist]
    return flattened
