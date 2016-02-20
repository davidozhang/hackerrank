#!/usr/bin/python

def factorial(memo, n):
	if n in memo:
		return memo[n]
	else:
		f = n*factorial(memo, n-1)
		memo[n] = f
		return f

def main():
	memo = {}
	memo[1] = 1
	memo[2] = 2
	print factorial(memo, input())

if __name__ == '__main__':
	main()
