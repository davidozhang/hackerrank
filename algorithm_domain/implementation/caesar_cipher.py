#!/usr/bin/python

def main():
    n = input()
    s = map(ord, raw_input())
    k = input()
    for i in xrange(len(s)): 
        if s[i]<=47:
            continue
        if 65 <= s[i] <= 90:
            s[i] = 65 + (s[i] - 65 + k%26) % 26
        elif 97 <= s[i] <= 122:
            s[i] = 97 + (s[i] - 97 + k%26) % 26
    print ''.join(map(chr, s))

if __name__ == '__main__':
    main()
