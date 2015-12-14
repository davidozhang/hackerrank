#!/usr/bin/python

def main():
    l = []
    n, x = map(int, raw_input().split())
    for _ in xrange(x):
        l.append(map(float, raw_input().split()))
    for i in zip(*l):
        print sum(i)/len(i)

if __name__ == '__main__':
    main()
