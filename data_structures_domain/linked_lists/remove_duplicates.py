"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    traverse = head
    while traverse and traverse.next:
        next = traverse.next
        while next and next.data == traverse.data:
            next = next.next
        traverse.next = next
        traverse = next
    return head
