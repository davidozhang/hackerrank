#!/bin/python

import sys


n = int(raw_input().strip())
a = []
sum_1, sum_2 = 0, 0
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
for b, c in enumerate(zip(*a)):
    sum_1 += c[b]
    sum_2 += c[n-1-b]
print abs(sum_1 - sum_2)
