#!/usr/bin/python
from itertools import groupby

def remove_pairs(s):
    if len(s) == 0:
        return s
    t = ''
    for i, j in groupby(s):
        if len(list(j)) %2 != 0:
            t += i
    if s == t:
        return t
    return remove_pairs(t)

def main():
    s = raw_input()
    t = remove_pairs(s)
    print 'Empty String' if len(t) == 0 else t

if __name__ == '__main__':
    main()