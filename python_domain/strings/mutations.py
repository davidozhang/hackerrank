#!/usr/bin/python

def main():
    s = list(raw_input())
    i, c = raw_input().split(' ')
    s[int(i)] = c
    print ''.join(s)

if __name__ == '__main__':
    main()

