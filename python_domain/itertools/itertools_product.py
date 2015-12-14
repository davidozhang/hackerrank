#!/usr/bin/python
from itertools import product

def main():
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    for i in list(product(a, b)):
        print str(i),
    
if __name__ == '__main__':
    main()
