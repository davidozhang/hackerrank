#!/usr/bin/python

def max_points(m, n, i, s, p):
    if i >= n:
        return p
    return max(max_points(m, n, i+1, s, p+s*m[i]), max_points(m, n, i+1, s+1, p))

def main():
    for _ in xrange(input()):
        n = input()
        m = sorted(map(int, raw_input().split()))
        s = 1
        p = 0
        print max_points(m, n, 0, s, p)

if __name__ == '__main__':
    main()