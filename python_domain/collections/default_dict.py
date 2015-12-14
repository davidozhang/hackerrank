#!/usr/bin/python
from collections import defaultdict
def main():
    d = defaultdict(list)
    n, m = map(int, raw_input().split())
    for _ in xrange(n):
        d['A'].append(raw_input())
    for _ in xrange(m):
        d['B'].append(raw_input())
    for i in d['B']:
        if i not in d['A']:
            print -1
        else:
            while i in d['A']:
                _ind = d['A'].index(i)
                print _ind+1,
                d['A'][_ind] = ''
            print ''

if __name__ == '__main__':
    main()
