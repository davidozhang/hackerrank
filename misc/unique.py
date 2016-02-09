#!/usr/bin/python

def main():
	dict = {}
	input = raw_input('Enter a string: ')
	unique = True

	for i in input:
		if i in dict:
			unique = False
			print 'Not unique'
			break
		dict[i] = 1

	if unique:
		print 'Unique'

if __name__=='__main__':
	main()