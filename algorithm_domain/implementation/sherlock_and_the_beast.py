#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n = input()
        if n<3 or n==4:
            print -1
        else:
            numFives = n/3
            while (n-3*numFives)%5 != 0 and numFives>=0:
                numFives -= 1
            print -1 if numFives < 0 else '555'*numFives+'33333'*((n-3*numFives)/5)

if __name__ == '__main__':
    main()
