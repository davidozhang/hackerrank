def main():
	l = raw_input().split()
	tracker = (None, 0)
	for i in l:
		if tracker[0] == None:
			tracker = (i, 1)
		elif i == tracker[0]:
			tracker = (i, tracker[1]+1)
		else:
			tracker = (tracker[0], tracker[1]-1)
			if tracker[1] == 0:
				tracker = (None, 0)
	print tracker[0]

if __name__ == '__main__':
	main()