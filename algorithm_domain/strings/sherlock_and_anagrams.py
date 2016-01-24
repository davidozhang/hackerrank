#!/usr/bin/python
import math
from itertools import groupby

def substrings(s):
    for k in xrange(1, len(s)+1):
        for i in xrange(len(s)-k+1):
            yield ''.join(sorted(s[i:i+k]))

def main():
    for _ in xrange(input()):
        s = raw_input()
        counter = 0
        for i, j in groupby(sorted(substrings(s))):
            n = len(list(j))
            if n > 2:
                counter += math.factorial(n) / (2 * math.factorial(n-2))
            elif n == 2:
                counter += 1
        print counter
        
if __name__ == '__main__':
    main()
