#!/usr/bin/python

def main():
	result = 0
	l = map(int, raw_input().split())
	left, right = [], []
	left_max = l[0]
	right_max = l[-1]
	for i in xrange(len(l)):
		if l[i]>left_max:
			left_max = l[i]
		left.append(left_max)
	for i in xrange(len(l)):
		if l[len(l)-1-i]>right_max:
			right_max = l[len(l)-1-i]
		right.insert(0, right_max)
	for j in xrange(len(l)):
		result += min(left[j], right[j]) - l[j]
	print result

if __name__ == '__main__':
	main()
