#!/usr/bin/python

def main():
    n, d = map(int, raw_input().split())
    a = map(int, raw_input().split())
    count = 0
    s = set()
    
    for i in xrange(n):
        s.add(a[i])
    
    for j in xrange(n):
        if a[j]+d in s and a[j]+d*2 in s:
            count += 1
    print count        
    
if __name__ == '__main__':
    main()
