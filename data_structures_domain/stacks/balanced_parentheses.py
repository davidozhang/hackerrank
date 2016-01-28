#!/usr/bin/python

def main():
    _dict = {'{':'}', '(':')', '[':']'}
    for _ in xrange(input()):
        stack = []
        s = raw_input()
        for i in s:
            top = stack[-1] if len(stack)>0 else None
            if not top or (top in _dict and i != _dict[top]):
                stack.append(i)
            elif top in _dict and i == _dict[top]:
                stack.pop()
        print 'YES' if len(stack) == 0 else 'NO'
            
if __name__ == '__main__':
    main()
