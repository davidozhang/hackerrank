#!/usr/bin/python

def main():
    for _ in xrange(input()):
        m, n = input(), input()
        l = map(int, raw_input().split(' '))
        for i, j in enumerate(l):
            try:
                k = l.index(m-j, i+1)
                print str(i+1) + ' ' + str(k+1)
                break
            except:
                continue
                
if __name__ == '__main__':
    main()
