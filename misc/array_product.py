#!/usr/bin/python

def main():
	result = [1]
	left_product, right_product = 1, 1
	l = map(int, raw_input().split())
	for i in xrange(1, len(l)):
		left_product *= l[i-1]
		result.append(left_product)
	for j in xrange(len(l)-2, -1, -1):
		right_product *= l[j+1]
		result[j] *= right_product
	print result

if __name__ == '__main__':
	main()
