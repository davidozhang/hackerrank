def Reverse(head):
    newHead = None
    traversal = head
    while traversal is not None:
        temp_next = traversal.next
        traversal.next = newHead
        traversal.prev = None
        newHead = traversal
        traversal = temp_next
    return newHead
