#!/usr/bin/python
def main():
    for i in range(input()):
        funny = True
        s = raw_input()
        rev = s[::-1]
        for i in xrange(len(s)-1):
            if abs(ord(s[i+1])-ord(s[i])) != abs(ord(rev[i+1])-ord(rev[i])):
                funny = False
        print 'Funny' if funny else 'Not Funny'
    
if __name__ == '__main__':
    main()
