#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n, c, m = map(int, raw_input().split())
        chocolates = n/c
        result = chocolates
        while chocolates >= m:
            result += 1
            chocolates = chocolates - m + 1;
        print result
            

if __name__ == '__main__':
    main()
