#!/usr/bin/python

def bubble_sort(l):
	for i in xrange(len(l)):
		for j in xrange(i, len(l)):
			if l[i] > l[j]:
				temp = l[j]
				l[j] = l[i]
				l[i] = temp
	return l

def main():
	print bubble_sort(# some array)

if __name__ == '__main__':
	main()
