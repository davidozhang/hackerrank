#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n = int(raw_input())
        arr = map(int, raw_input().strip().split(' '))
        found = False
        _left, _right = 0, sum(arr)
        for i in xrange(n):
            if i>=1:
                _left += arr[i-1]
            _right -= arr[i]
            if _left == _right:
                found = True
                break
        print 'YES' if found else 'NO'

if __name__ == '__main__':
    main()
