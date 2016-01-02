#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n = input()
        print (2**32 - 1) ^ n

if __name__ == '__main__':
    main()
