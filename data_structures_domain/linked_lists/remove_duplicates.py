def RemoveDuplicates(head):
    if not head:
        return None
    new_next = head.next
    while new_next is not None and new_next.data == head.data:
        new_next = new_next.next
    head.next = RemoveDuplicates(new_next)
    return head
