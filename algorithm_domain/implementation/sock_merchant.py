#!/usr/bin/python

def main():
    n = input()
    c = map(int, raw_input().split())
    _dict = {}
    for i in c:
        _dict[i] = _dict[i] + 1 if i in _dict else 1
    print sum(_dict[i]//2 for i in _dict)

if __name__ == '__main__':
    main()
