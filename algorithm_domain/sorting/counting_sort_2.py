#!/usr/bin/python

def main():
    _dict = {i: 0 for i in xrange(100)}
    n = input()
    for i in map(int, raw_input().split()):
        _dict[i] += 1
    for j in xrange(100):
        for _ in xrange(_dict[j]):
            print str(j),

if __name__ == '__main__':
    main()
