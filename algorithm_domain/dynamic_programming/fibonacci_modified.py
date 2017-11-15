#!/usr/bin/python

def main():
    memo = {}
    t1, t2, n = map(int, raw_input().split())
    memo[1] = t1
    memo[2] = t2

    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-2) + fib(n-1)**2
        return memo[n]
    print fib(n)

if __name__ == '__main__':
    main()

'''
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

Second try: September 5

#!/usr/bin/python

def fib(n, memo):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-2, memo) + (fib(n-1, memo))**2
    return memo[n]

def main():
    t1, t2, n = map(int, raw_input().split())
    memo = {}
    memo[1] = t1
    memo[2] = t2
    print fib(n, memo)

if __name__ == '__main__':
    main()
'''
