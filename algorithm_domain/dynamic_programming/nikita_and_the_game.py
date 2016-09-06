#!/usr/bin/python

def max_score(a, l, r):
    pivot = None
    if l >= r:
        return 0
    left_sum = 0
    right_sum = sum(a[l:r+1])
    for i in xrange(l, r+1):
        left_sum += a[i]
        right_sum -= a[i]
        if left_sum == right_sum:
            pivot = i
            break
    if pivot is None:
        return 0
    else:
        return 1 + max(max_score(a, l, pivot), max_score(a, pivot+1, r))

def main():
    for _ in xrange(input()):
        n = input()
        a = map(int, raw_input().split())
        if sum(a) == 0:
            print n-1
        else:
            print max_score(a, 0, n-1)

if __name__ == '__main__':
    main()
