#!/usr/bin/python

def main():
	stack = []
	volume = 0
	l = map(int, raw_input().split())
	for i in xrange(0, len(l)-1):
		if len(stack) == 0 or l[i]>stack[-1]:
			stack.append(l[i])
		elif l[i]<=stack[-1]:
			if l[i+1] <= l[i]:
				volume += stack[-1]-l[i]
			else:
				volume += min(l[i+1], stack[-1])-l[i]
				stack.append(l[i+1])
	print volume
if __name__ == '__main__':
	main()
