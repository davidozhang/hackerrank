#!/usr/bin/python

def main():
    l = []
    n, m = map(int, raw_input().split())
    for _ in xrange(n):
        l.append(map(int, raw_input().split()))
    k = input()
    s = sorted([(i, j) for i, j in enumerate(zip(*l)[k])], key=lambda x: x[1])
    for i in [t[0] for t in s]:
        print ' '.join(map(str, l[i]))
    
if __name__ == '__main__':
    main()
