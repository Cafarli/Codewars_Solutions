"""
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

# Use the `next' attribute to get the following node
node.next
Notes:

do NOT mutate the nodes!
in some cases there may be only a loop, with no dangling piece
"""
def loop_size(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_length = 1
            current_node = slow.next

            while current_node != slow:
                loop_length += 1
                current_node = current_node.next

            return loop_length

    return 0
