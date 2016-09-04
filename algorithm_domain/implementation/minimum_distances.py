#!/usr/bin/python

def main():
    n = input()
    a = map(int, raw_input().split())
    _min = 1000
    _dict = {}
    for i in xrange(n):
        if a[i] in _dict:
            _dict[a[i]].append(i)
        else:
            _dict[a[i]] = [i]
    for i in _dict:
        if len(_dict[i]) > 1:
            s = sorted(_dict[i])
            for i in xrange(1, len(s)):
                _min = min(_min, abs(s[i-1]-s[i]))
    print -1 if _min == 1000 else _min
        
if __name__ == '__main__':
    main()
