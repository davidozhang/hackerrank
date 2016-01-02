#!/usr/bin/python

def main():
    s = set()
    n = input()
    lst = sorted(map(int, raw_input().split()))
    result = 0
    
    for i in lst:
        if i not in s:
            result += 1
            s.update(range(i, i+5))
    print result

if __name__ == '__main__':
    main()
