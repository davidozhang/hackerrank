#!/usr/bin/python
import math

def main():
    n = input()
    l = sorted(map(int, raw_input().split()))
    _min = None
    result = []
    for i in xrange(len(l)-1):
        diff = abs(l[i]-l[i+1])
        if diff < _min or not _min:
            _min  = diff
    for j in xrange(len(l)-1):
        diff = abs(l[j]-l[j+1])
        if diff == _min:
            result.append(l[j])
            result.append(l[j+1])
    print ' '.join(map(str, result))

if __name__ == '__main__':
    main()
