#!/usr/bin/python

def main():
    a = input()
    set_1 = set(map(int, raw_input().split()))
    b = input()
    set_2 = set(map(int, raw_input().split()))
    print len(set_1 | set_2)
    
if __name__ == '__main__':
    main()
