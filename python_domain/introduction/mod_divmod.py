#!/usr/bin/python
from __future__ import division

def main():
    a, b = input(), input()
    tup = (a//b, a%b)
    print tup[0]
    print tup[1]
    print tup

if __name__ == '__main__':
    main()
