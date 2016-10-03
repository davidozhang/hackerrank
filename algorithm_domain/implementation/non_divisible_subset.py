#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    s = map(int, raw_input().split())
    _dict = {}
    for i in xrange(len(s)):
        s[i] %= k
        _dict[s[i]] = _dict[s[i]] + 1 if s[i] in _dict else 1
    for j in _dict:
        if k-j in _dict:
            _max = max(_dict[j], _dict[k-j])
            if _dict[j] == _max:
                _dict[k-j] = 0
            else:
                _dict[j] = 0
    if k % 2 == 0 and k/2 in _dict:
        _dict[k/2] = 1
    if 0 in _dict:
        _dict[0] = 1
    print sum(_dict[j] for j in _dict)

if __name__ == '__main__':
    main()
