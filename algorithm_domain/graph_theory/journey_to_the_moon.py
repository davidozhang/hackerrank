#!/usr/bin/python
import sys
from math import factorial

def choose(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

def explore(g, visited, u):
    count = 1
    visited.add(u)
    for v in g[u]:
        if v not in visited:
            visited.add(v)
            count += explore(g, visited, v)
    return count

def main():
    sys.setrecursionlimit(100000)
    n, i = map(int, raw_input().split())
    g = {i: set() for i in xrange(n)}
    result = n*(n-1)/2
    subgraphs = {}
    visited = set()
    for _ in xrange(i):
        a, b = map(int, raw_input().split())
        g[a].add(b)
        g[b].add(a)
    for j in xrange(n):
        if j not in visited:
            size = explore(g, visited, j)
            subgraphs[size] = subgraphs[size] + 1 if size in subgraphs else 1
    for k in subgraphs:
        if k >= 2:
            result -= subgraphs[k] * choose(k, 2)
    print result

if __name__ == '__main__':
    main()
