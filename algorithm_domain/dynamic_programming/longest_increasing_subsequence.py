#!/usr/bin/python

def lis(i, n, values, memo):
    if i < 0 or i >= n:
        return 0
    if i in memo:
        return memo[i]
    memo[i] = 1
    _max = float('-inf')
    for j in xrange(i+1, n):
        if values[j] > values[i]:
            _max = max(_max, lis(j, n, values, memo))
    if _max != float('-inf'):
        memo[i] += _max
    return memo[i]

def main():
    n = input()
    values = []
    memo = {}
    for _ in xrange(n):
        values.append(input())
    for i in xrange(n):
        lis(i, n, values, memo)
    print max(memo.values())
    
if __name__ == '__main__':
    main()
