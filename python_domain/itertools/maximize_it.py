#!/usr/bin/python
from itertools import product

def squared(s):
    return pow(s, 2)

def f(tup, m):
    return sum(map(squared, tup)) % m

def main():
    k, m = map(int, raw_input().split())
    _lists = []
    for i in xrange(k):
        _lists.append(map(int, raw_input().split()[1:]))
    print max([f(i, m) for i in list(product(*_lists))])

if __name__ == '__main__':
    main()
