#!/usr/bin/python

def main():
    for _ in xrange(input()):
        l, p = [], []
        found = False
        big_r, big_c = map(int, raw_input().split())
        for _ in xrange(big_r):
            l.append(raw_input())
        small_r, small_c = map(int, raw_input().split())
        for _ in xrange(small_r):
            p.append(raw_input())
        for i in xrange(big_r):
            if p[0] in l[i]:
                index = 0
                while index < big_c:
                    index = l[i].find(p[0], index)
                    if index == -1:
                        break
                    equal = True
                    for j in xrange(1, small_r):
                        if p[j] != l[i+j][index:index+small_c]:
                            equal = False
                            break
                    if equal:
                        found = True
                        break
                    index += 1
            if found:
                break
        print 'YES' if found else 'NO'
            
if __name__ == '__main__':
    main()
