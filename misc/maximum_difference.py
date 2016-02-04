#!/usr/bin/python

def main():
	l = map(int, raw_input().split())
	min_left = l[0]
	diff = 0
	for i in l:
		min_left = min(min_left, i)
		diff = max(diff, i-min_left)
	print diff

if __name__ == '__main__':
	main()
