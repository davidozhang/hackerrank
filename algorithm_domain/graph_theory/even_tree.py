#!/usr/bin/python

def even_tree(g, n):
    visited = set([1])
    result = 0
    count = {i: 1 for i in xrange(1, n+1)}
    explore(g, visited, count, 1)
    for i in xrange(2, n+1):
        if count[i]%2 == 0:
            result += 1
    return result
    
def explore(g, visited, count, u):
    for v in g[u]:
        if v not in visited:
            visited.add(v)
            explore(g, visited, count, v)
            count[u] += count[v]

def main():
    n, m = map(int, raw_input().split())
    g = {i: [] for i in xrange(1, n+1)}
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        g[u].append(v)
        g[v].append(u)
    print even_tree(g, n)

if __name__ == '__main__':
    main()
