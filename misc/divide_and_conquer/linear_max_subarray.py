#!/usr/bin/python

def max_subarray(l):
	best = 0
	currentBest = 0
	for i in xrange(len(l)):
		currentBest = max(currentBest+l[i], 0)
		best = max(best, currentBest)
	return best

def main():
	l = map(int, raw_input().split())
	print max_subarray(l)

if __name__ == '__main__':
	main()