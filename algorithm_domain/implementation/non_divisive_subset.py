#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    s = map(int, raw_input().split())
    _dict = {}
    counter = 0
    for i in xrange(len(s)):
        s[i] %= k
        if s[i] in _dict:
            _dict[s[i]] += 1
        else:
            _dict[s[i]] = 1
    for j in _dict:
        if k-j in _dict:
            if _dict[j] > _dict[k-j]:
                _dict[k-j] = 0
            else:
                _dict[j] = 0
    if 0 in _dict and _dict[0] > 1:
        _dict[0] = 1
    print sum(_dict.values())

if __name__ == '__main__':
    main()
