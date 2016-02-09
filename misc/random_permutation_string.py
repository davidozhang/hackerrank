#!/usr/bin/python
import random
from itertools import permutations

def main():
	s = raw_input().split()
	for i in xrange(len(s)):
		if len(s[i]) <= 2:
			continue
		p = list(permutations(s[i][1:-1]))
		s[i] = s[i][0] + ''.join(p[random.randint(0, len(p))]) + s[i][-1]
	print ' '.join(s)

if __name__ == '__main__':
	main()
