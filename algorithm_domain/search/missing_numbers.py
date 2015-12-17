#!/usr/bin/python
from collections import Counter

def main():
    n = input()
    a = Counter(map(int, raw_input().split(' ')))
    m = input()
    b = Counter(map(int, raw_input().split(' ')))
    diff = set(list((b - a).elements()))
    print ' '.join(map(str, sorted(diff)))
        
    
if __name__ == '__main__':
    main()
