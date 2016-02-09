#!/usr/bin/python

component_size = 1

def explore(g, visited, u):
    for v in g[u]:
        if v not in visited:
            global component_size
            component_size += 1
            visited.add(v)
            explore(g, visited, v)
    return

def main():
    global component_size
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    l = []
    m, n = input(), input()
    g = {(i, j): set() for i in xrange(m) for j in xrange(n)}
    for _ in xrange(m):
        l.append(map(int, raw_input().split()))
    for i in xrange(m):
        for j in xrange(n):
            if l[i][j] == 0:
                continue
            for k in offsets:
                if i+k[0]<0 or i+k[0]>=m or j+k[1]<0 or j+k[1]>=n:
                    continue
                if l[i+k[0]][j+k[1]] == 1:
                    g[(i, j)].add((i+k[0], j+k[1]))
                    g[(i+k[0], j+k[1])].add((i, j))
    max_component = 0
    visited = set()
    for i in xrange(m):
        for j in xrange(n):
            visited.add((i, j))
            explore(g, visited, (i, j))
            max_component = max(max_component, component_size)
            component_size = 1
    print max_component
        
if __name__ == '__main__':
    main()
