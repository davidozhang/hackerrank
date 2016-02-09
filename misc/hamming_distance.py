#!/usr/bin/python

def hamming_distance(a,b):
	result = 0
	for i in zip(a, b):
		result += i[0]^i[1]
	return result

def main():
	a = (1,0,0,1,0,0)
	b = (0,1,0,1,0,1)
	print hamming_distance(a,b)

if __name__ == '__main__':
	main()
