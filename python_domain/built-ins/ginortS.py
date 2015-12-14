#!/usr/bin/python

def main():
    t = list(raw_input())
    t.sort()
    s = reduce(lambda a, b: a+b, t)
    print reduce(lambda a, b: a+b, sorted(s, key=lambda x: (x.islower(), x.isupper(), x.isdigit() and int(x)%2==1), reverse=True))

if __name__ == '__main__':
    main()
