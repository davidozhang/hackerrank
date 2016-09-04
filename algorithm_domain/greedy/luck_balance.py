#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    important, non_important = [], []
    for _ in xrange(n):
        l, t = map(int, raw_input().split())
        if t == 1:
            important.append(l)
        else:
            non_important.append(l)
    sorted_important = sorted(important)[::-1]
    print sum(sorted_important[:k] + non_important) - sum(sorted_important[k:])
    
if __name__ == '__main__':
    main()