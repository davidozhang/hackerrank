#!/usr/bin/python

def main():
    s = list(raw_input())
    count = {}
    even, odd = 0, 0
    for i in s:
        count[i] = count.get(i, 0) + 1
    for j in count.values():
        if j % 2 != 0:
            odd += 1
        else:
            even += 1
    print 'YES' if even > 0 and (odd == 0 or odd == 1) else 'NO'
    
    
if __name__ == '__main__':
    main()
