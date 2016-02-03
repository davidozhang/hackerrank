#!/usr/bin/python

def main():
	_dict = {0:0, 1:0, 2:0}
	_val = {0:[], 1:[], 2:[]}
	l = map(int, raw_input().split())
	for i in l:
		_dict[i] += 1
	for j in xrange(3):
		for k in xrange(_dict[j]):
			print j,

if __name__ == '__main__':
	main()
