#!/usr/bin/python
from itertools import groupby

def main():
	result = ''
	s = raw_input()
	for i, j in groupby(s):
		result += i + str(len(list(j)))
	print s if len(result)>=len(s) else result

if __name__ == '__main__':
	main()
