#!/usr/bin/python

def main():
    for _ in xrange(input()):
        base = 1
        for i in xrange(1, input()+1):
            if i % 2 != 0:
                base *= 2
            else:
                base += 1
        print base
        
if __name__ == '__main__':
    main()
