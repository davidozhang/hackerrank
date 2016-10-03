#!/usr/bin/python

def main():
    stack = []
    _max = float('-inf')
    for _ in xrange(input()):
        query = map(int, raw_input().split())
        if query[0] == 1:
            _max = max(_max, query[1])
            stack.append((query[1], _max))
        elif query[0] == 2:
            top = stack.pop()
            _max = float('-inf') if len(stack) == 0 else stack[-1][1]
        elif query[0] == 3:
            print stack[-1][1]

if __name__ == '__main__':
    main()
