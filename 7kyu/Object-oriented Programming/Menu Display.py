"""
Task
Create a class that imitates a select screen. The cursor can move to left or right!

In the display method, return a string representation of the list, but with square brackets around the currently selected element. Also, create the methods to_the_right and to_the_left which moves the cursor.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])

menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_left()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_left()
menu.display() ➞ "[1, [2], 3]"
Notes
The cursor should wrap back round to the start once it reaches the end.
"""

class Menu:
    def __init__(self, elems):
        self.elems = elems
        self.pos = 0
    
    def to_the_right(self):
        self.pos = (self.pos + 1)%len(self.elems)
        
    def to_the_left(self):
        self.pos = (self.pos - 1)%len(self.elems)
        
    def display(self):
        return "[" + ", ".join([f"['{x}']" if i == self.pos else f"'{x}'" for i, x in enumerate(self.elems)]) + "]"
