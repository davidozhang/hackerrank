#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n, m, s = map(int, raw_input().split())
        result = (s + (m - 1) % n) % n
        if result == 0:
            result = n
        print result
        
if __name__ == '__main__':
    main()
