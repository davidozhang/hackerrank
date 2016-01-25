#!/usr/bin/python

def main():
    stack = []
    for _ in xrange(input()):
        l = raw_input().split()
        if l[0] == 'push':
            stack.append([l[1], 0])
        elif l[0] == 'pop' and len(stack)>0:
            u = stack.pop()
            if len(stack) > 0:
                stack[-1][1] += u[1]
        elif l[0] == 'inc':
            stack[int(l[1])-1][1] += int(l[2])
        print str(sum(map(int, stack[-1]))) if len(stack) > 0 else str([])

if __name__ == '__main__':
    main()
