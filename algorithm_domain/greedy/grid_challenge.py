#!/usr/bin/python

def main():
    for _ in xrange(input()):
        l = []
        result = True
        for _ in xrange(input()):
            l.append(list(sorted(raw_input())))
        for i in zip(*l):
            if list(i) != sorted(i):
                result = False
                break
        print 'YES' if result else 'NO'

if __name__ == '__main__':
    main()
