#!/usr/bin/python

def main():
	result = []
	l = map(int, raw_input().split())
	s = set(l)
	used = set()
	for i in l:
		if -i in s and i not in used and -i not in used:
			result.append((i, -i))
			used.update([i, -i])
	print result

if __name__ == '__main__':
	main()
