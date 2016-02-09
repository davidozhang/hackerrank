#!/usr/bin/python

def solve(_dict, lst):
	length=len(lst)
	end=length-1
	while end>=length/2:
		for i in range(end):
			if lst[i]<lst[end]:
				return _dict[lst[i]], _dict[lst[end]]
			end-=1
	return -1, -1

def main():
	_dict, n={}, int(raw_input())
	for i in range(n):
		_dict[i]=int(raw_input())
	print solve(_dict, sorted(_dict, key=_dict.get))
	
if __name__=='__main__':
	main()