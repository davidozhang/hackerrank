#!/usr/bin/python
def insertionSort(l):    
    last = ar[-1]
    j=len(l)-2
    while j>=0 and last<l[j]:
        temp = last
        l[j+1] = l[j]
        print ' '.join(map(str, l))
        l[j] = last
        j -= 1
    print ' '.join(map(str, l))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
