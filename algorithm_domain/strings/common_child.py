#!/usr/bin/python
from itertools import repeat
'''
Top-down DP implementation that times out on some test cases
def lcs(a, b, i, n, j, m, memo):
    if i >= n or j >= m: 
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if a[i] == b[j]:
        memo[(i, j)] = 1 + lcs(a, b, i+1, n, j+1, m, memo)
    else:
        memo[(i, j)] = max(lcs(a, b, i+1, n, j, m, memo), lcs(a, b, i, n, j+1, m, memo))
    return memo[(i, j)]
'''

'''
Bottom-up DP implementation
'''
def common_child(a, b, n, m):
    cc = [[0]*(n+1) for _ in repeat(None, m+1)]
    for i in reversed(xrange(1, n+1)):
        for j in reversed(xrange(1, m+1)):
            if a[i-1] == b[j-1]:
                cc[i-1][j-1] = cc[i][j] + 1
            else:
                cc[i-1][j-1] = max(cc[i][j-1], cc[i-1][j])
    return cc[0][0]

def main():
    a = raw_input()
    b = raw_input()
    memo = {}
    print common_child(a, b, len(a), len(b))

if __name__ == '__main__':
    main()
