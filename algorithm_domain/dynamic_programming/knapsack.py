#!/usr/bin/python

def main():
    for _ in xrange(input()):
        _max = 0
        n, k = map(int, raw_input().split())
        s = set(map(int, raw_input().split()))
        for i in sorted(s):
            if k%i==0:
                _max = k
                break
            else:
                rem = k%i
                diff = 0
                while rem>0 and rem not in s:
                    rem -= 1
                    diff += 1
                _max = max(_max, k-diff) if rem in s else max(_max, i*(k/i))
                 
        print _max
                
if __name__ == '__main__':
    main()
