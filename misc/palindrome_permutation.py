#!/usr/bin/python

def main():
	_dict = {}
	s = raw_input()
	odd_count = 0
	for i in s:
		_dict[i] = 1 if i not in _dict else _dict[i]+1
	for j in _dict.keys():
		if _dict[j]%2 != 0:
			odd_count += 1
	if odd_count == 0 or odd_count == 1:
		print True
	else:
		print False

if __name__ == '__main__':
	main()
