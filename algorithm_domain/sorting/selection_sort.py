#!/usr/bin/python

def selection_sort(l):
	for i in xrange(len(l)):
		min_index = i
		for j in xrange(i, len(l)):
			if l[j]<l[min_index]:
				min_index = j
		temp = l[i]
		l[i] = l[min_index]
		l[min_index] = temp
	return l

def main():
	print selection_sort(# some array)

if __name__ == '__main__':
	main()
