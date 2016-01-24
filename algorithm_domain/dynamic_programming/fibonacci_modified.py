#!/usr/bin/python

def fib_mod(memo, n):
    if n in memo:
        return memo[n]
    else:
        f = fib_mod(memo, n-1)**2 + fib_mod(memo, n-2)
        memo[n] = f
        return f

def main():
    memo = {}
    a, b, n = map(int, raw_input().split())
    memo[1] = a
    memo[2] = b
    print fib_mod(memo, n)

if __name__ == '__main__':
    main()
