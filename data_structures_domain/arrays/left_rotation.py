#!/usr/bin/python

def main():
    n, d = map(int, raw_input().split())
    a = map(int, raw_input().split())
    print ' '.join(map(str, a[d%n:] + a[:d%n]))

if __name__ == '__main__':
    main()
