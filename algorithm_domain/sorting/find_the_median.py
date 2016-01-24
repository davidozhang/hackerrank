#!/usr/bin/python

def main():
    n = input()
    l = map(int, raw_input().split())
    print sorted(l)[len(l)/2]

if __name__ == '__main__':
    main()
