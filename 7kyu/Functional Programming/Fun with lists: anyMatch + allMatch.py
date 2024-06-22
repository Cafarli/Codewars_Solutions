"""
Implement two methods anyMatch and allMatch which take the head of a linked list and a predicate function, and return:

anyMatch: whether the predicate is true for any of the list's elements.
allMatch: whether the predicate is true for all of the list's elements.
For example:

Given the list: 1 -> 2 -> 3, and the predicate x => x > 1, anyMatch / any_match should return true (both 2 & 3 are valid for this predicate), 
and allMatch / all_match should return false (1 is not valid for this predicate)

The linked list is defined as follows:

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
Note: the list may be null and can hold any type of value.
"""

from typing import Callable, Any

def any_match(head: Node, pred: Callable[[Any], bool]) -> bool:
    current = head
    while current is not None:
        if pred(current.data):
            return True
        current = current.next
    return False

def all_match(head: Node, pred: Callable[[Any], bool]) -> bool:
    current = head
    while current is not None:
        if not pred(current.data):
            return False
        current = current.next
    return True
