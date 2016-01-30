""":
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    # Iterative
    '''newHead = None
    traversal = head
    while traversal != None:
        temp = traversal.next
        traversal.next = newHead
        newHead = traversal
        traversal = temp
    return newHead'''
    
    # Recursive
    if head is None or head.next is None:
        return head

    tail = head.next
    head.next = None
    newhead = Reverse(tail)
    tail.next = head
    return newhead
