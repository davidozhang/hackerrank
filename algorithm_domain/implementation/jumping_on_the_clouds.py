#!/usr/bin/python

def main():
    n = input()
    c = map(int, raw_input().split())
    counter = 0
    i = 0
    while i+2 < n:
        if c[i+2] == 0:
            i += 2
        elif c[i+2] == 1:
            i += 1
        counter += 1
    if i == n-2:
        counter += 1
    print counter
    
if __name__ == '__main__':
    main()