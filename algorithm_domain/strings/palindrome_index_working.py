#!/usr/bin/py
 
def is_palindrome(s):
    return s == s[::-1]
 
def palindrome_index(s):
    if is_palindrome(s):
        return -1
    else:  
        for i in xrange((len(s)+1)//2):
            if s[i] != s[len(s)-i-1]:
                return i if is_palindrome(s[:i]+s[i+1:]) else len(s)-i-1

def main():
    t = input()
    for _ in xrange(t):
        s = raw_input()
        print palindrome_index(s)

if __name__ == '__main__':
    main()
