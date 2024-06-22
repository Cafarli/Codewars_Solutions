"""
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. Specifically, this means 
the language supports passing functions as arguments to other functions,returning them as the values from other functions, and assigning them to variables or 
storing them in data structures.

First-class functions are a necessity for the functional programming style, in which the use of higher-order functions is a standard practice. 
A simple example of a higher-ordered function is the map function, which takes, as its arguments, a function and a list, and returns the list formed 
by applying the function to each member of the list. For a language to support map, it must support passing a function as an argument. 
See more on https://en.wikipedia.org/wiki/First-class_function

Your task is to rewrite your own map function which takes :

an array
a predicate function func which returns true (boolean) with even arguments
For example :

map([1,2,3,4],func)

produces

[ false, true, false, true ]  
The code also has to perform input validation, return :

'given argument is not a function' if func is not a function
'array should contain only numbers' if any elements are not numbers
"""

def func(n):
    print(n)
    return int(n)%2==0

def map(arr, func):
    if not callable(func):
        return 'given argument is not a function'
    if len(arr) != len([v for v in arr if isinstance(v, (int, float)) or (isinstance(v, str) and v.isdigit())]):
        return 'array should contain only numbers'    
    return [func(v) for v in arr]
