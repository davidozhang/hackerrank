#!/usr/bin/python

def main():
    l = []
    n = input()
    result = [1]*n
    for _ in xrange(n):
        l.append(int(raw_input()))
    for i in xrange(1, n):
        if l[i] > l[i-1]:
            result[i] = result[i-1] + 1
    for j in xrange(n-1):
        if l[n-2-j] > l[n-1-j]:
            result[n-2-j] = max(result[n-2-j], result[n-1-j]+1)
    print sum(result)

if __name__ == '__main__':
    main()
