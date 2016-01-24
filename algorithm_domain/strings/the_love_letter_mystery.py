#!/usr/bin/python

def main():
    for _ in xrange(input()):
        result = 0
        l = map(ord, raw_input())
        for i in xrange((len(l)+1)//2):
            if l[i] != l[len(l)-1-i]:
                result += abs(l[i] - l[len(l)-1-i])
                if l[i] > l[len(l)-1-i]:
                    l[i] = l[len(l)-1-i]
                elif l[i] < l[len(l)-1-i]:
                    l[len(l)-1-i] = l[i]
        print result
                
                
if __name__ == '__main__':
    main()
