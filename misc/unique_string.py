#!/usr/bin/python

def main():
	s = raw_input()
	print 'YES' if len(set(s)) == len(s) else 'NO'

if __name__ == '__main__':
	main()
