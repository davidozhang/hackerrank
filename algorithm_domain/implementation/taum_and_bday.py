#!/usr/bin/python

def main():
    for _ in xrange(input()):
        b, w = map(int, raw_input().split())
        x, y, z = map(int, raw_input().split())
        print min(b*x + w*y, b*(y+z) + w*y, b*x + w*(x+z))

if __name__ == '__main__':
    main()
