#!/usr/bin/python

def d(memo, l, m, i, j):
    if j==0:
        return 1
    if i>=m or j<0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    value = d(memo, l, m, i, j-l[i]) + d(memo, l, m, i+1, j)
    memo[(i, j)] = value
    return value

def main():
    memo = {}
    n, m = map(int, raw_input().split())
    l = map(int, raw_input().split())
    print d(memo, sorted(l), m, 0, n)
    
if __name__ == '__main__':
    main()
