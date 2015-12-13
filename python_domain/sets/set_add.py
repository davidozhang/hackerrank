#!/usr/bin/python

def main():
    _set = set()
    for i in xrange(input()):
        _set.add(raw_input())
    print len(_set)

if __name__ == '__main__':
    main()
