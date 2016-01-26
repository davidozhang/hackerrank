#!/usr/bin/python
from itertools import groupby

def main():
    n = input()
    l = sorted(map(int, raw_input().split()))
    for i, j in groupby(l):
        print n
        n -= len(list(j))

if __name__ == '__main__':
    main()
