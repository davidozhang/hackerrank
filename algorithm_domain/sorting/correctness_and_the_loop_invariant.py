def insertion_sort(l):    
    for i in xrange(1, len(l)):
        j = i
        val = l[i]
        while j>0 and val<l[j-1]:
            l[j] = l[j-1]
            j -= 1
        l[j] = val
    return l


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
