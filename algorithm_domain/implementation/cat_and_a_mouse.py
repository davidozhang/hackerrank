#!/usr/bin/python

def main():
    for _ in xrange(input()):
        a, b, c = map(int, raw_input().split())
        a = abs(c-a)
        b = abs(c-b)
        _min = min(a, b)
        if _min == a and _min == b:
            print 'Mouse C'
        elif _min == a:
            print 'Cat A'
        else:
            print 'Cat B'
        
if __name__ == '__main__':
    main()
