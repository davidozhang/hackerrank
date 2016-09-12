#!/usr/bin/python
import sys

def knapsack(n, a, i, j, memo):
    if i >= n:
        return 0
    if j < 0:
        return -float('inf')
    if (i, j) in memo:
        return memo[(i, j)]
    memo[(i, j)] = max(a[i] + knapsack(n, a, i, j-a[i], memo), knapsack(n, a, i+1, j, memo))
    return memo[(i, j)]

def main():
    sys.setrecursionlimit(100000)
    for _ in xrange(input()):
        n, k = map(int, raw_input().split())
        a = sorted(map(int, raw_input().split()))
        memo = {}
        print knapsack(n, a, 0, k, memo)

if __name__=='__main__':
    main()