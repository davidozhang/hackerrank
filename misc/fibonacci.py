#!/usr/bin/python

def fib(n):
	if n==0 or n==1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def main():
	input = raw_input('Input: ')
	print fib(input)

if __name__=='__main__':
	main()