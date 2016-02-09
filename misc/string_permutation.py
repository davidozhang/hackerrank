#!/usr/bin/python

all = set()

def permute(s, step):
	if step == len(s):
		all.add(''.join(s))
	for i in range(step, len(s)):
		s_copy = list(s)
		s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
		permute(s_copy, step+1)
def main():
	s = list(raw_input())
	permute(s, 0)
	print sorted(all)

if __name__ == '__main__':
	main()
