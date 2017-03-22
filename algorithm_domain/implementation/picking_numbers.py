#!/usr/bin/python
        
def main():
    _dict = {}
    _max = 1
    n = input()
    l = map(int, raw_input().split())
    for i in l:
        _dict[i] = 1 if i not in _dict else _dict[i] + 1
    for j in _dict:
        _max = max(_max, _dict[j] + _dict.get(j-1, 0), _dict[j] + _dict.get(j+1, 0))
    print _max

if __name__ == '__main__':
    main()
