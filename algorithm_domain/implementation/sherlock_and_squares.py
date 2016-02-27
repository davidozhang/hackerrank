#!/usr/bin/python
import math

def main():
    for _ in xrange(input()):
        result = 0
        a, b = map(int, raw_input().split())
        base = math.ceil(math.sqrt(a))
        while base**2 <= b:
            result += 1
            base += 1
        print result
            
if __name__ == '__main__':
    main()
