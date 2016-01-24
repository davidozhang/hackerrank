#!/usr/bin/python

def main():
    _count = {i: 0 for i in xrange(100)}
    _value = {i: [] for i in xrange(100)}
    accum = 0
    for _ in xrange(input()):
        key, val = raw_input().split()
        _count[int(key)] += 1
        _value[int(key)].append(val)
    for j in xrange(100):
        accum += _count[j]
        print accum,

if __name__ == '__main__':
    main()
