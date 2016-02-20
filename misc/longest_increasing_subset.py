#!/usr/bin/python

def main():
	_max, _count = 0, 0
	left, right = 1, 0
	l = map(int, raw_input().split())
	for i in xrange(1, len(l)):
		_count += 1
		if l[i-1] > l[i]:
			_max = max(_max, _count)
			left = right
			right = i-1
			_count = 0
	print l[left:right+1]
	
if __name__ == '__main__':
	main()
