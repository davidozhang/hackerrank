#!/usr/bin/python

def main():
    l, s = input(), raw_input()
    counter = 0
    i = 0
    j = 2
    while j < l:
        if s[i:j+1] == '010':
            counter += 1
            i += 3
            j += 3
        else:
            i += 1
            j += 1
    print counter
    
if __name__ == '__main__':
    main()