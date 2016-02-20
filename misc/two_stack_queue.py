#!/usr/bin/python

def main():
	s1, s2 = [], []
	for _ in xrange(input()):
		_in = raw_input().split()
		if _in[0] == 'enqueue':
			s2.append(_in[1])
		elif _in[0] == 'dequeue':
			if len(s1) == 0:
				while len(s2) > 0:
					s1.append(s2.pop())
			if len(s1) > 0:
				print s1.pop()
		elif _in[0] == 'empty':
			print len(s1) == 0 and len(s2) == 0

if __name__ == '__main__':
	main()
