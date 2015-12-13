#!/usr/bin/python
from __future__ import division
def main():
    n = input()
    nums = set(map(int, raw_input().split()))
    print sum(nums)/len(nums)

if __name__ == '__main__':
    main()
