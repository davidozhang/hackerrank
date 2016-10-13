#!/usr/bin/python

def lcss(arr):
	max_so_far = 0
	max_ending_here = 0
	for i in arr:
		max_ending_here += i
		max_ending_here = max(max_ending_here, 0)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def main():
	arr = [-2, -3, 4, -1, -2, 1, 5, -3]
	print lcss(arr)

if __name__ == '__main__':
	main()
