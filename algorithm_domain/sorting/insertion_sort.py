#!/usr/bin/python

def insertion_sort(l):
	for i in xrange(1, len(l)):
		j = i-1
		while j>=0 and l[i]<l[j]:
			j -= 1
		temp = l[j+1]
		l[j+1] = l[i]
		l[i] = temp
	return l

def main():
	print insertion_sort(# some array)

if __name__ == '__main__':
	main()
