#!/usr/bin/python

def is_palindrome(a):
    return a == a[::-1]

def main():
    for _ in xrange(input()):
        memo = {}
        s = raw_input()
        index = -1
        left, right = '', s
        if not is_palindrome(s):
            for i in xrange(len(s)):
                left += s[i-1] if i>0 else ''
                right = right[1:]
                comb = left + right
                if comb in memo and memo[comb] == False:
                    continue
                else:
                    f = is_palindrome(comb)
                    if f:
                        index = i
                        break
                    memo[comb] = f
                    
        print index
        
if __name__ == '__main__':
    main()
