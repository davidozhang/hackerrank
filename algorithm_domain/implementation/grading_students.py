#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n = input()
        if n < 38 or n % 5 == 0:
            print n
        else:
            m = ((n / 5) + 1) * 5
            print m if m - n < 3 else n
        
if __name__ == '__main__':
    main()
