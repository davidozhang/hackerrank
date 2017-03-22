#!/usr/bin/python

def main():
    n = input()
    l = map(int, raw_input().split())
    greatest = l[0]
    least = l[0]
    best = 0
    worst = 0
    
    for i in l:
        if i > greatest:
            best += 1
            greatest = i
        elif i < least:
            worst += 1
            least = i
    print best, worst
    
if __name__ == '__main__':
    main()
