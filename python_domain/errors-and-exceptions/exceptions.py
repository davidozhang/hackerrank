#!/usr/bin/python

def div(x,y):
    try:
        return int(x)/int(y)
    except ZeroDivisionError as z:
        return 'Error Code: ' + str(z)
    except ValueError as v:
        return 'Error Code: ' + str(v)
        

def main():
    l = []
    for _ in xrange(input()):
        x, y = raw_input().split()
        l.append(div(x,y))
    for i in l:
        print i

if __name__ == '__main__':
    main()
