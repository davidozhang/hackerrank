#!/usr/bin/python

def main():
    result = 0
    n, m = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    a = set(map(int, raw_input().split()))
    b = set(map(int, raw_input().split()))
    for i in arr:
        if i in a:
            result += 1
        elif i in b:
            result -= 1
    print result
    
if __name__ == '__main__':
    main()
