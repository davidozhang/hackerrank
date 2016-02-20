#!/usr/bin/python

def fib(memo, n):
	if n == 1:
		return memo[1]
	elif n == 2:
		return memo[2]
	else:
		f = fib(memo, n-1) + fib(memo, n-2)
		memo[n] = f
		return f

def main():
	memo = {}
	memo[1] = 1
	memo[2] = 1
	print fib(memo, 5)

if __name__=='__main__':
	main()
