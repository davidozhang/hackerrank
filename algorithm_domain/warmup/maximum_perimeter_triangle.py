#!/usr/bin/python

def main():
    n = input()
    l = sorted(map(int, raw_input().split()))[::-1]
    i = 0
    found = False
    for i in range(n-2):
        if l[i] < l[i+1] + l[i+2]:
            found = True
            break
    if not found:
        print -1
    else:
        print l[i+2], l[i+1], l[i]

if __name__ == '__main__':
    main()
