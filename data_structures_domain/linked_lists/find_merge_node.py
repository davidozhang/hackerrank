def FindMergeNode(headA, headB):
    curA = headA
    curB = headB
    while curA != curB:
        curA = curA.next if curA is not None else headB
        curB = curB.next if curB is not None else headA
    return curA.data
