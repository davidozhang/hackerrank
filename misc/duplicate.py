#!/usr/bin/python

def main():
	dict = {}
	input = raw_input('Enter a string')
	output = ''
	for i in input:
		if i not in dict:
			output += i
		dict[i] = 1

	print output
if __name__=='__main__':
	main()