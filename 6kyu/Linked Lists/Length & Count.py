"""
Linked Lists - Length & Count

Implement length to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
I've decided to bundle these two functions within the same Kata since they are both very similar.
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    l = 0
    curr = node
    
    while curr is not None:
        l += 1
        curr = curr.next
    return l
def count(node, data):
    cnt = 0
    curr = node
    
    while curr is not None:
        if curr.data==data:
            cnt+=1
        curr = curr.next
    return cnt
        
