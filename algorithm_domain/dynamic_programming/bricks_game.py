#!/usr/bin/python

'''
Recursive implementation that times out
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
'''

'''
Bottom-up implementation that passes everything. Woot woot!
'''
def bricks_game(bricks, n):
    matrix = [0]*(n+6)
    for i in reversed(xrange(1, n+1)):
        matrix[i-1] = max(
            bricks[i-1] + min(matrix[i+1], matrix[i+2], matrix[i+3]),
            sum(bricks[i-1:i+1]) + min(matrix[i+2], matrix[i+3], matrix[i+4]),
            sum(bricks[i-1:i+2]) + min(matrix[i+3], matrix[i+4], matrix[i+5])
        )
    return matrix[0]

def main():
    for _ in xrange(input()):
        n = input()
        bricks = map(int, raw_input().split())
        print bricks_game(bricks, n)

if __name__ == '__main__':
    main()
