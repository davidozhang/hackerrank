#!/usr/bin/python

def main():
    counts = map(int, raw_input().split())
    stacks = []
    for _ in xrange(3):
        stacks.append(map(int, raw_input().split())[::-1])
    for i in xrange(3):
        prev_sum = 0
        for j in xrange(counts[i]):
            stacks[i][j] = stacks[i][j]+prev_sum
            prev_sum = stacks[i][j]
    intersection = set(stacks[0]) & set(stacks[1]) & set(stacks[2])
    print max(intersection) if len(intersection) > 0 else 0
        

if __name__ == '__main__':
    main()
