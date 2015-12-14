#!/usr/bin/python
from collections import Counter

def main():
    n, result = input(), 0
    c = Counter(map(int, raw_input().split()))
    for _ in xrange(input()):
        size, amount = map(int, raw_input().split())
        if c[size] > 0:
            result += amount
            c[size] -= 1
    print result
    
if __name__ == '__main__':
    main()
