#!/usr/bin/python
import heapq

def main():
    def lookup(x, y):
        return (x, y) if x < y else (y, x)

    for _ in xrange(input()):
        n, m = map(int, raw_input().split())
        g = {i: set() for i in xrange(1, n+1)}
        edges = {}
        costs = {}
        visited = set()
        for _ in xrange(m):
            x, y, r = map(int, raw_input().split())
            key = lookup(x, y)
            if key in edges:
              edges[key] = min(edges[key], r)
            else:
              edges[key] = r

        for key in edges:
          g[key[0]].add((edges[key], key[1]))
          g[key[1]].add((edges[key], key[0]))

        s = input()
        q = [(0, s)]

        def djikstra(u):
            while q:
                cost, v = heapq.heappop(q)
                costs[v] = min(costs[v] if v in costs else float('inf'), cost)
                if v not in visited:
                    visited.add(v)

                    for c, w in g[v]:
                        if w not in visited:
                            heapq.heappush(q, (cost+c, w))
        djikstra(s)

        for i in xrange(1, n+1):
          if i not in costs:
            costs[i] = -1
        costs.pop(s)
        print ' '.join(map(str, costs.values()))

if __name__ == '__main__':
    main()
