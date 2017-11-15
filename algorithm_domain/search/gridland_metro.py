#!/usr/bin/python

def main():
    n, m, k = map(int, raw_input().split())
    visited = set()
    posts = [m for _ in xrange(n)]
    for _ in xrange(k):
        r, c1, c2 = map(int, raw_input().split())
        for col in xrange(c1-1, c2):
            if (r-1, col) not in visited:
                posts[r-1] -= 1
                visited.add((r-1, col))
    print sum(posts)

if __name__ == '__main__':
    main()
