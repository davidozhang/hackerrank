#!/usr/bin/python

def max_subarray(l, left, right):
	if left == right:
		return l[left]
	else:
		middle = (left+right)/2
		l1 = max_subarray(l, left, middle)
		l2 = max_subarray(l, middle+1, right)
		return max(l1, l2, max_crossing(l, left, middle, right))

def max_crossing(l, left, middle, right):
		left_sum, right_sum = None, None
		left_temp = middle
		while left_temp>=left:
			if not left_sum:
				left_sum = l[left_temp]
			else:
				left_sum = max(left_sum, left_sum+l[left_temp])
			left_temp -= 1

		right_temp = middle+1
		while right_temp<=right:
			if not right_sum:
				right_sum = l[right_temp]
			else:
				right_sum = max(right_sum, right_sum+l[right_temp])
			right_temp += 1

		return left_sum + right_sum

def main():
	l = map(int, raw_input().split())
	print max_subarray(l, 0, len(l)-1)

if __name__ == '__main__':
	main()