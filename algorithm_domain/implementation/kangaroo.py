#!/usr/bin/python

def main():
    x1, v1, x2, v2 = map(int, raw_input().split())
    
    if (x1 <= x2 and v2 > v1) or (x2 <= x1 and v1 > v2):
        print 'NO'
    else:
        if v1 != v2 and (x2-x1) % (v1-v2) == 0:
            print 'YES'
        else:
            print 'NO'
            
if __name__ == '__main__':
    main()