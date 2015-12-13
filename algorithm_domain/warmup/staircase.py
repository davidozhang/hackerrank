#!/bin/python

import sys


n = int(raw_input().strip())
for i in range(n):
    print ('#'*(i+1)).rjust(n, ' ')
