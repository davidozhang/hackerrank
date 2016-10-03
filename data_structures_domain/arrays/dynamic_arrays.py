#!/usr/bin/python

def main():
    n, q = map(int, raw_input().split())
    seq_list = [[] for _ in xrange(n)]
    last_ans = 0
    for _ in xrange(q):
        query = map(int, raw_input().split())
        index = (query[1] ^ last_ans) % n
        if query[0] == 1:
            seq_list[index].append(query[2])
        elif query[0] == 2:
            last_ans = seq_list[index][query[2] % len(seq_list[index])]
            print last_ans

if __name__ == '__main__':
    main()
