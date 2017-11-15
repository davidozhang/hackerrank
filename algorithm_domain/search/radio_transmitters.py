#!/usr/bin/python

def main():
    n, r = map(int, raw_input().split())
    l = sorted(map(int, raw_input().split()))
    i = 0
    _len = len(l)
    _count = 0
    while i < _len:
        proposed_pos = l[i] + r
        while i < _len and l[i] <= proposed_pos:
            i += 1
        i -= 1
        _count += 1
        actual_pos = l[i] + r
        while i < _len and l[i] <= actual_pos:
            i += 1
    print _count

if __name__ == '__main__':
    main()
