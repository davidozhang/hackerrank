"""
 Check if linked list has cycle
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return 0 if no cycle else return 1
"""

def HasCycle(head):
    return HasCycleHelper(head, head.next)

def HasCycleHelper(start, head):
    if not head:
        return 0
    elif head == start:
        return 1
    else:
        return HasCycleHelper(head.next)
