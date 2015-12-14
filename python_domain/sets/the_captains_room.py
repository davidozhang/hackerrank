#!/usr/bin/python
import sys
from collections import Counter
def main():
    n = input()
    c = Counter(map(int, raw_input().split()))
    print c.most_common()[-1][0]

if __name__ == '__main__':
    main()
