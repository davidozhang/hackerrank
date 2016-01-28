#!/usr/bin/python

def main():
    _max = -99999
    l = [map(int, raw_input().split()) for _ in xrange(6)]
    for i in xrange(4):
        for j in xrange(4):
            _max = max(_max, sum(l[i][j:j+3]) + l[i+1][j+1] + sum(l[i+2][j:j+3]))
    print _max
    
if __name__ == '__main__':
    main()
