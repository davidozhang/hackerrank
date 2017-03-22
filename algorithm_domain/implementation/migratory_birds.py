#!/usr/bin/python

def main():
    s = set()
    _dict = {}
    _maxCount = 0
    n = input()
    l = map(int, raw_input().split())
    for i in l:
        _dict[i] = 1 if i not in _dict else _dict[i] + 1
        if _dict[i] > _maxCount:
            _maxCount = _dict[i]
    for j in _dict:
        if _dict[j] == _maxCount:
            s.add(j)
    print min(s)

if __name__ == '__main__':
    main()
