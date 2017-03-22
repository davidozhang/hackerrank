#!/usr/bin/python

def main():
    l = sorted(map(int, raw_input().split()))
    print sum(l[:-1]), sum(l[1:])

if __name__ == '__main__':
    main()
