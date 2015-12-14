#!/usr/bin/python
from itertools import groupby

def main():
    groups = [(len(list(g)),int(k)) for k, g in groupby(raw_input())]
    for i in groups:
        print i,

if __name__ == '__main__':
    main()
