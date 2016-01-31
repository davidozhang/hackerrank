#!/usr/bin/python
import heapq

def main():
    result, greater = 0, True
    n, k = map(int, raw_input().split())
    l = map(int, raw_input().split())
    heapq.heapify(l)
    while len(l) > 0 and l[0]<k:
        u = heapq.heappop(l)
        if u < k:
            try:
                v = heapq.heappop(l)
                result += 1
                heapq.heappush(l, u + 2*v)
            except IndexError:
                greater = False
                break
        else:
            heapq.heappush(l, u)
    print result if greater else -1

if __name__ == '__main__':
    main()
