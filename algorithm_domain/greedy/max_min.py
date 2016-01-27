#!/usr/bin/python

def min_unfairness(k, arr):
    _min = None
    sorted_arr = sorted(arr)
    for i in xrange(len(sorted_arr)-k+1):
        val = sorted_arr[i+k-1] - sorted_arr[i]
        if val < _min or not _min:
            _min = val
    return _min

def main():
    n, k = input(), input()
    l = []
    for _ in xrange(n):
        l.append(input())
    print min_unfairness(k, l)

if __name__ == '__main__':
    main()
