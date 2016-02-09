#!/usr/bin/python

def main():
    n, k, q = map(int, raw_input().split())
    l = map(int, raw_input().split())
    mod = k%n
    left = l[:-mod]
    right = l[-mod:]
    l = right + left
    for _ in xrange(q):
        print l[input()]
if __name__ == '__main__':
    main()
