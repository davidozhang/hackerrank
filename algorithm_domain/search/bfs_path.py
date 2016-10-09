#!/usr/bin/python

def bfs(g, u, visited, parent):
    queue = [u]
    while len(queue) > 0:
        u = queue.pop(0)
        for v in g[u]:
            if v not in visited:
                parent[v] = u
                visited.add(v)
                queue.append(v)

def path(u, v, parent):
    result = []
    while v in parent:
        result.append(v)
        v = parent[v]
    if v == u:
        result.append(u)
    return result[::-1]

def main():
    visited = set([1])
    parent = {}
    g = {1: set([2, 3]),
         2: set([1, 3, 4, 5]),
         3: set([2, 5, 7, 8]),
         4: set([2, 5]),
         5: set([2, 3, 4, 6]),
         6: set([5]),
         7: set([3]),
         8: set([3]),
         9: set([10]),
         10: set([9])}
    bfs(g, 1, visited, parent)
    print parent
    print path(1, 6, parent)

if __name__ == '__main__':
    main()
