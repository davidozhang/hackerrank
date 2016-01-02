#!/usr/bin/python

def main():
    for _ in xrange(input()):
        n, k = map(int, raw_input().split())
        a, b = map(int, raw_input().split()), map(int, raw_input().split())
        c, d = True, True
        for i, j in zip(sorted(a), sorted(b, reverse=True)):
            if i + j < k:
                c = False
                break
        for e, f in zip(sorted(a, reverse=True), sorted(b)):
            if e + f < k:
                d = False
                break
        print 'YES' if c or d else 'NO'
        
if __name__ == '__main__':
    main()
