#!/usr/bin/python

def main():
    for _ in xrange(input()):
        s1 = set(list(raw_input()))
        s2 = set(list(raw_input()))
        print 'YES' if len(s1.intersection(s2)) > 0 else 'NO'
 
if __name__ == '__main__':
    main()
