#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    w = map(ord, list(raw_input()))
    diffs = 0
    indices = []
    for i in xrange(n):
        if i > n-i-1:
            break
        if w[i] != w[n-i-1] or w[i] == w[n-i-1]:
            indices.append((i, n-i-1))
            diffs += 1
    if diffs > k:
        print -1
    else:
        for i, j in indices:
            if k <= 0:
                break
            if i == j:
                k -= 1
                w[i] = ord('9')
            if k >= 2:
                if max(w[i], w[j]) == ord('9'):
                    k -= 1
                else:
                    k -= 2
                w[i] = ord('9')
                w[j] = ord('9')
            else:
                _max = max(w[i], w[j])
                if w[i] == _max:
                    w[j] = _max
                else:
                    w[i] = _max
        print ''.join(map(chr, w))

if __name__ == '__main__':
    main()
