#!/usr/bin/python

all = set()
def permute(c, s):
	if len(s) == 0:
		all.add(c)
	for i in xrange(len(s)):
		permute(c+s[i], s[:i]+s[i+1:])

def main():
	s = raw_input()
	permute('', s)
	print sorted(all)

if __name__ == '__main__':
	main()
