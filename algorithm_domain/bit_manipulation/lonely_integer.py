#!/usr/bin/python

def main():
    n = input()
    l = map(int, raw_input().split())
    print reduce((lambda x, y: x^y), l)


if __name__ == '__main__':
    main()
