#!/usr/bin/python

count = 0

def inv(l, left, right):
	if left == right:
		return
	else:
		middle = (left+right)/2
		inv(l, left, middle)
		inv(l, middle+1, right)
		inv_merge(l, left, middle, right)

def inv_merge(l, left, middle, right):
	l3 = []
	i = left
	j = middle + 1
	while i <= middle and j <= right:
		if l[i] <= l[j]:
			l3.append(l[i])
			i += 1
		elif l[j] < l[i]:
			global count
			l3.append(l[j])
			count += middle-left+1
			j += 1

	while i <= middle:
		l3.append(l[i])
		i += 1

	while j <= right:
		l3.append(l[j])
		j += 1

	l[left:right+1] = l3

def main():
	l = map(int, raw_input().split())
	inv(l, 0, len(l)-1)
	print count
if __name__ == '__main__':
	main()