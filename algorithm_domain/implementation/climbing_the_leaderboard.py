#!/usr/bin/python

def bs(scores, l, r, val):
    while l <= r:
        mid = l + (r - l)/2
        if val > scores[mid]:
            r = mid - 1
        elif val == scores[mid]:
            return mid + 1
        else:
            l = mid + 1
    return l + 1

def main():
    n = input()
    scores = map(int, raw_input().split())
    m = input()
    alice = map(int, raw_input().split())
    scores_deduped = []
    prev = None
    for i in scores:
        if prev is None or i != prev:
            scores_deduped.append(i)
            prev = i
    r = len(scores_deduped) - 1
    for j in alice:
        print bs(scores_deduped, 0, r, j)
    
if __name__ == '__main__':
    main()
