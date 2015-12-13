#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
count = [0, 0, 0]
for i in arr:
    if i > 0: count[0] +=1
    elif i < 0: count[1] +=1
    else: count[2] +=1
for j in count:
    print format(j/n, '.6f')
