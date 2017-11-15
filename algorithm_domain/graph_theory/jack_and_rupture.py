#!/usr/bin/python

def main():
  n, e = map(int, raw_input().split())
  g = {i: set() for i in xrange(1, n+1)}
  visited = set([1])
  q = [(0, 1)]
  costs = {}
  cum_costs = {}
  for _ in xrange(e):
    s1, s2, c = map(int, raw_input().split())
    g[s1].add((c, s2))
    g[s2].add((c, s1))

  def bfs():
    while q:
      cost, u = q.pop(0)
      for c, v in g[u]:
        if v not in visited:
          visited.add(v)
          if u in costs:
            costs[v] = c - costs[u] if c > cum_costs[u] else 0
            cum_costs[v] = max(costs[u], c)
          else:
            costs[v] = c
            cum_costs[v] = c
          q.append((costs[v], v))
        elif v in costs:
          if c < cum_costs[u]:
            costs[v] = 0
            cum_costs[v] = min(cum_costs[v], cum_costs[u])
          else:
            diff = c - costs[u]
            costs[v] = min(costs[v], diff if diff > 0 else float('inf'))
            cum_costs[v] = min(cum_costs[v], cum_costs[u] + c)

  bfs()
  if n not in visited:
    print 'NO PATH EXISTS'
  else:
    print cum_costs[n]

if __name__ == '__main__':
  main()
 
