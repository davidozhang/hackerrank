#!/usr/bin/python

def sort(list):
	less = []
	equal = []
	greater = []

	if len(list)>1:
		pivot = list[0]

		for i in list:
			if i<pivot:
				less.append(i)
			elif i==pivot:
				equal.append(i)
			elif i>pivot:
				greater.append(i)
		return sort(less)+equal+sort(greater) 
	else:
		return list

def main():
	input = map(int, raw_input().split())
	print sort(input)

if __name__=='__main__':
	main()