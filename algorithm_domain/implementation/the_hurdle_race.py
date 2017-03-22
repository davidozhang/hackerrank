#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    _max = max(l)
    if k > _max:
        print 0
    else:
        print _max - k

if __name__ == '__main__':
    main()
