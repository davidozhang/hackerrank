#Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    la, lb = [], []
    while headA:
        la.append(headA.data)
        headA = headA.next
    while headB:
        lb.append(headB.data)
        headB = headB.next
    return 1 if la == lb else 0
