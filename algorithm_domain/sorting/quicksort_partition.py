#!/usr/bin/python
def partition(m, ar):    
    less, equal, greater = [], [], []
    for i in ar:
        if i<m:
            less.append(i)
        elif i == m:
            equal.append(i)
        else:
            greater.append(i)
    return ' '.join(map(str, less + equal + greater))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(m, ar)


