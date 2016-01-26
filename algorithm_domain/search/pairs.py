#!/usr/bin/python

def main():
    result = 0
    n, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    s = set(l)
    for i in l:
        if i+k in s:
            result += 1
    print result
    
if __name__ == '__main__':
    main()
