#!/usr/bin/python

def main():
	l = []
	stop = None
	for i in raw_input().split():
		l.append(list(i))
	for i, j in enumerate(zip(*l)):
		stop = i
		if len(set(j)) > 1:
			break
	print ''.join(l[0][:stop+1])

if __name__ == '__main__':
	main()
