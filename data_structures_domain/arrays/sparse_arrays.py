#!/usr/bin/python 

def main():
    _dict = {}
    for _ in xrange(input()):
        s = raw_input()
        _dict[s] = _dict[s] + 1 if s in _dict else 1
    for _ in xrange(input()):
        print _dict.get(raw_input(), 0)

if __name__ == '__main__':
    main()
