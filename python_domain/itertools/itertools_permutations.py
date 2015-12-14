#!/usr/bin/python
from itertools import permutations

def main():
    s, n = raw_input().split()
    for i in list(permutations(list(sorted(s, key=str.upper)), int(n))):
        print ''.join(i)

if __name__ == '__main__':
    main()
