#!/usr/bin/python
import heapq

def merge(k, n, arrs):
    print heapq.heapify(zip(*arrs)[0])


def main():
    arrs = []
    k = 3
    n = 4
    arrs.append([1,3,5,7])
    arrs.append([2,4,6,8])
    arrs.append([0,9,10,11])
    merge(k, n, arrs)

if __name__ == '__main__':
    main()