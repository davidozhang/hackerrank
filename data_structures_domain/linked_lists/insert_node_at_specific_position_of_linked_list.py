"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    counter = 0
    n = Node(data=data)
    if position == 0:
        n.next = head
        head = n
        return head
    traversal = head
    while counter+1 != position and traversal.next:
        counter += 1
        traversal = traversal.next
    temp = traversal.next
    traversal.next = n
    n.next = temp
    return head
