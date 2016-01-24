#!/usr/bin/python

def shortest_path(parent, visited, s, v):
    if v not in visited:
        return -1
    result = 0
    while v in parent:
        result += 6
        v = parent[v]
    return result

def bfs(s, g):
    visited = set([s])
    queue = [s]
    parent = {}

    while len(queue) > 0:
        u = queue.pop(0)
        for i in g[u]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
                parent[i] = u

    for i in sorted(g.keys()):
        if i != s:
            print shortest_path(parent, visited, s, i),
    print ''

def main():
    for _ in xrange(input()):
        n, edges = map(int, raw_input().split())
        g = {i: [] for i in xrange(1, n+1)}
        for _ in xrange(edges):
            a, b = map(int, raw_input().split())
            g[a].append(b)
            g[b].append(a)
        s = input()
        bfs(s, g)
    
if __name__ == '__main__':
    main()
