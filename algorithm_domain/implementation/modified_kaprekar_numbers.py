#!/usr/bin/python

def main():
    result = []
    p, q = input(), input()
    for i in xrange(p, q+1):
        sq = str(i**2)
        for j in xrange(len(sq)):
            a, b = int(sq[:j] or 0), int(sq[j:])
            if b and a+b == i:
                result.append(str(i))
    print ' '.join(result)

if __name__ == '__main__':
    main()
