#!/usr/bin/python
from collections import Counter

def main():
    for _ in xrange(input()):
        result = 0
        s = raw_input()
        if len(s) %2 != 0:
            result = -1
        else:
            result = sum((Counter(s[0:len(s)/2])-Counter(s[len(s)/2:])).values())
        print result

if __name__ == '__main__':
    main()
