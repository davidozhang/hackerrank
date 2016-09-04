#!/usr/bin/python

def next_permutation(l):
    _len = len(l)
    pivot = -1
    suffix = []
    for i in xrange(_len-1):
        suffix.append(l[_len-i-1])
        if l[_len-i-2] < l[_len-i-1]:
            pivot = _len-i-2
            break
    if pivot == -1:
        return 'no answer'
    else:
        for i in xrange(len(suffix)):
            if suffix[i] > l[pivot]:
                temp = l[pivot]
                l[pivot] = suffix[i]
                l[_len-i-1] = temp
                suffix[i] = temp
                break
        l[pivot+1:] = sorted(suffix)
        return ''.join(map(chr, l))

def main():
    for _ in xrange(input()):
        ords = map(ord, raw_input())
        print next_permutation(ords)
        
if __name__ == '__main__':
    main()
