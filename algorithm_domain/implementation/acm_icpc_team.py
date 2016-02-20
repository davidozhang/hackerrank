#!/usr/bin/python

def main():
    l = []
    _dict = {}
    _max = 0
    n, m = map(int, raw_input().split())
    for _ in xrange(n):
        l.append(raw_input())
    for i in xrange(n-1):
        for j in xrange(i, n):
            count = bin(int(l[i],2) | int(l[j],2)).count('1')
            _dict[count] = 1 if count not in _dict else _dict[count]+1
            _max = max(_max, count)
    print _max
    print _dict[_max]
                
if __name__ == '__main__':
    main()
