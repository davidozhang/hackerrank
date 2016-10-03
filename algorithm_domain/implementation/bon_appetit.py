#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    c = map(int, raw_input().split())
    b = input()
    print 'Bon Appetit' if b == (sum(c)-c[k])/2 else b-(sum(c)-c[k])/2

if __name__ == '__main__':
    main()
