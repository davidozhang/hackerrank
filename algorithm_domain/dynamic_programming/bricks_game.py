#!/usr/bin/python

def bricks(n, b, i, memo):
    if i >= n:
        return 0
    if i in memo:
        return memo[i]
    memo[i] = max(
        b[i] + min(bricks(n, b, i+2, memo), bricks(n, b, i+3, memo), bricks(n, b, i+4, memo)),
        sum(b[i:i+2]) + min(bricks(n, b, i+3, memo), bricks(n, b, i+4, memo), bricks(n, b, i+5, memo)),
        sum(b[i:i+3]) + min(bricks(n, b, i+4, memo), bricks(n, b, i+5, memo), bricks(n, b, i+6, memo))
    )
    return memo[i]

def main():
    for _ in xrange(input()):
        n = input()
        b = map(int, raw_input().split())
        memo = {}
        print bricks(n, b, 0, memo)

if __name__ == '__main__':
    main()