#!/usr/bin/python

def main():
    for _ in xrange(input()):
        s = raw_input()
        count = 0
        for i in xrange(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
        print count
            
if __name__ == '__main__':
    main()
