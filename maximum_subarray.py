#!/usr/bin/python

def func(l):
    current_sum = 0
    non_contiguous_sum = 0
    current_index = -1
    best_sum = 0
    best_start_index = -1
    best_end_index = -1
    first_max = sorted(l, reverse=True)[0]
    if first_max < 0:
        return (first_max, first_max)
    for i in xrange(len(l)):
        val = current_sum + l[i]
        if l[i] > 0:
            non_contiguous_sum += l[i]
        if val > 0:
            if current_sum == 0:
                current_index =i
            current_sum = val
        else:
            current_sum = 0
       
        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i
    return (sum(l[best_start_index:best_end_index+1]), non_contiguous_sum)

def main():
    for _ in xrange(input()):
        n = input()
        l = map(int, raw_input().split(' '))
        result = func(l)
        print str(result[0]) + ' ' + str(result[1])

if __name__ == '__main__':
    main()
