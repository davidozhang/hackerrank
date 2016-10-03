#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n = input()
        a = map(int, raw_input().split())
        left = 0
        right = sum(a)
        exists = False
        for i in a:
            right -= i
            if left == right:
                exists = True
                break
            left += i
        print 'YES' if exists else 'NO'

if __name__ == '__main__':
    main()
