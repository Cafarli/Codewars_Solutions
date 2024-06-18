"""
Task
Your challenge is to write a function named getSlope/get_slope/GetSlope that calculates the slope of the line through two points.

Input
Each point that the function takes in is an array 2 elements long. 
The first number is the x coordinate and the second number is the y coordinate. 
If the line through the two points is vertical or if the same point is given twice, the function should return null/None.
"""


def get_slope(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    if x1 == x2 or p1 == p2:
        return None
    
    slope = (y2 - y1) / (x2 - x1)
    return slope
