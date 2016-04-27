#!/usr/bin/python
import sys

def main():
    l, offset = [], [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = input()
    for _ in xrange(n):
        l.append(map(int, list(raw_input())))
    for i in xrange(1, n-1):
        for j in xrange(1, n-1):
            greater = True
            for k in offset:
                if l[i+k[0]][j+k[1]] == 'X' or l[i+k[0]][j+k[1]] >= l[i][j]:
                    greater = False
                    break
            if greater:
                l[i][j] = 'X'
    for i in xrange(n):
        for j in xrange(n):
            sys.stdout.write(str(l[i][j]))
        sys.stdout.write('\n')
    sys.stdout.flush()

if __name__ == '__main__':
    main()
