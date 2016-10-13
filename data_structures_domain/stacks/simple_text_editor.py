#!/usr/bin/python

def main():
    s = ''
    stack = []
    for _ in xrange(input()):
        operation = raw_input().split()
        if int(operation[0]) == 1:
            stack.append(s)
            s += operation[1]
        elif int(operation[0]) == 2:
            k = int(operation[1])
            stack.append(s)
            s = s[:len(s)-k]
        elif int(operation[0]) == 3:
            k = int(operation[1])
            print s[k-1]
        elif int(operation[0]) == 4:
            s = stack.pop()
        
if __name__ == '__main__':
    main()
