#!/usr/bin/python

def main():
    n = input()
    l = map(int, raw_input().split())
    s = sorted(l)
    left, right = None, None
    for i in xrange(len(l)):
        if l[i] != s[i]:
            left = i
            break
    for j in xrange(len(l)):
        ind = len(l)-1-j
        if l[ind] != s[ind]:
            right = ind
            break
    swap = l[left+1:right] == s[left+1:right]
    reverse = l[left:right+1][::-1] == s[left:right+1]
    if swap or reverse:  # swap
        print 'yes'
        if swap:
            print 'swap ' + str(left+1) + ' ' + str(right+1)
        elif reverse:
            print 'reverse ' + str(left+1) + ' ' + str(right+1)
    else:
        print 'no'
    
if __name__ == '__main__':
    main()
