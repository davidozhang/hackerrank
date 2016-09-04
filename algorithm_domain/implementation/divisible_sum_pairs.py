#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    counter = 0
    _dict = {}
    
    for i in xrange(len(a)):
        rem = a[i]%k
        if rem in _dict:
            _dict[rem].append(i)
            _dict[rem] = sorted(_dict[rem])
        else:
            _dict[rem] = [i]

    for j in xrange(len(a)):
        rem = a[j]%k
        if rem > 0:
            diff = k-rem
        else:
            diff = 0
        if diff in _dict:
            _len = len(_dict[diff])
            for m in xrange(_len):
                if _dict[diff][m] > j:
                    counter += _len - m
                    break
    print counter
    
if __name__ == '__main__':
    main()
