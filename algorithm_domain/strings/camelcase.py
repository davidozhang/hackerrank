#!/usr/bin/python

def main():
    number = 1
    s = raw_input()
    for i in s:
        if i.isupper():
            number += 1
    print number

if __name__ == '__main__':
    main()
