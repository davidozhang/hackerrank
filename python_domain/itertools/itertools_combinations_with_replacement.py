#!/usr/bin/python
from itertools import combinations_with_replacement

def main():
    s, n = raw_input().split()
    for i in list(combinations_with_replacement(list(sorted(s, key=str.upper)), int(n))):
        print ''.join(i)

if __name__ == '__main__':
    main()
