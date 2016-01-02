#!/usr/bin/python
from operator import itemgetter

def main():
    lst, result = [], ''
    for i in xrange(input()):
        t, d = map(int, raw_input().split())
        lst.append((i+1, t+d))
    for j in sorted(lst, key=itemgetter(1, 0)):
        result += str(j[0]) + ' '
    print result.strip()
        
if __name__ == '__main__':
    main()
