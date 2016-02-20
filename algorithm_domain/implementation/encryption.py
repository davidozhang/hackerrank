#!/usr/bin/python
import math

def main():
    l = []
    s = ''.join(raw_input().split())
    col = int(math.ceil(math.sqrt(len(s))))
    temp = ''
    for i in xrange(len(s)):
        if len(temp)<col:
            temp += s[i]
        else:
            l.append(temp)
            temp = s[i]
    if len(temp) > 0:
        temp += ' '*(col-len(temp))
        l.append(temp)
    print ' '.join([''.join(x).strip() for x in zip(*l)])

if __name__ == '__main__':
    main()
