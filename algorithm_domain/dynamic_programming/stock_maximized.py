#!/usr/bin/python

def main():
    for _ in xrange(input()):
        profit = 0
        n = input()
        l = map(int, raw_input().split())
        _max = None
        for i in xrange(len(l)-1, -1, -1):
            if l[i]>_max or not _max:
                _max = l[i]
            profit += _max - l[i]
        print profit

if __name__ == '__main__':
    main()
