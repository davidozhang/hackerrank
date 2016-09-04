#!/usr/bin/python

def main():
    s = raw_input()
    i = 0
    counter = 0
    while i<len(s):
        if s[i] != 'S':
            counter += 1
        if s[i+1] != 'O':
            counter += 1
        if s[i+2] != 'S':
            counter += 1
        i += 3
    print counter
    
if __name__ == '__main__':
    main()