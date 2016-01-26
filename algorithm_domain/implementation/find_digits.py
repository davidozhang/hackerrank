#!/usr/bin/python

def main():
    for _ in xrange(input()):
        result = 0
        n = raw_input()
        l = map(int, n)
        n_int = int(n)
        for i in l:
            if i!=0 and n_int%i==0:
                result += 1
        print result
        
if __name__ == '__main__':
    main()
