"""
Implement the method countIf (count_if in PHP and Python), which accepts a linked list (head) and a predicate function, and returns the number of elements which apply to the given predicate.

For example: Given the list: 1 -> 2 -> 3, and the predicate x => x >= 2, countIf / count_if should return 2, since x >= 2 applies to both 2 and 3.

The linked list is defined as follows:

class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
Note: the list may be null and can hold any type of value.
"""

def count_if(head, func):
    curr_node = head
    result = []
    while curr_node:
        if func(curr_node.data): 
            result.append(curr_node.data)
        curr_node = curr_node.next
    return len(result)
