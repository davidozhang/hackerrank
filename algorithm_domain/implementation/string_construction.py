#!/usr/bin/python

def main():
    for _ in xrange(input()):
        s = list(raw_input())
        print len(set(s))
                
if __name__ == '__main__':
    main()
