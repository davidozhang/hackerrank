#!/usr/bin/python
import math

def main():
    for _ in xrange(input()):
        _dict = {}
        n = input()
        l = map(int, raw_input().split())
        for i in l:
            _dict[i] = 1 if i not in _dict else _dict[i]+1
        _sum = 0
        for k in _dict.keys():
            if _dict[k] >= 2:
                _sum += _dict[k] * (_dict[k] - 1)
        print _sum

if __name__ == '__main__':
    main()
