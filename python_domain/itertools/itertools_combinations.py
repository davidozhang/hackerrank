#!/usr/bin/python
from itertools import combinations

def main():
    s, n = raw_input().split()
    for i in xrange(1, int(n)+1):
        for j in list(combinations(list(sorted(s, key=str.upper)), int(i))):
            print ''.join(j)

if __name__ == '__main__':
    main()
