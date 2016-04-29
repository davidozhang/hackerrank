#!/usr/bin/python
import sys
s = set()
a, b, n = 0, 0, 0

def recurse(memo, steps, value):
    global s, a, b, n
    if steps == n:
        s.add(value)
        return
    if steps>n or (steps, value) in memo:
        return
    recurse(memo, steps+1, value+a)
    memo[(steps+1, value+a)] = True
    recurse(memo, steps+1, value+b)
    memo[(steps+1, value+b)] = True

def main():
    sys.setrecursionlimit(100000)
    for _ in xrange(input()):
        global s, a, b, n
        memo = {}
        s = set()
        n = input()
        a = input()
        b = input()
        recurse(memo, 1, 0)
        print ' '.join(map(str, sorted(s)))

if __name__ == '__main__':
    main()
