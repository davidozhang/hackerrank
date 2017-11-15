#!/usr/bin/python
def main():
    n, m = map(int, raw_input().split())
    g = {i: set() for i in xrange(1, n+1)}
    count = [1 for _ in xrange(n)]
    visited = set()
    for _ in xrange(m):
        u, v = map(int, raw_input().split())
        g[u].add(v)
        g[v].add(u)
    visited.add(1)

    def explore(u):
        for v in g[u]:
            if v not in visited:
                visited.add(v)
                explore(v)
                count[u-1] += count[v-1]

    explore(1)
    result = 0
    for num in count[1:]:
        result += 1 if num % 2 == 0 else 0
    print result

if __name__ == '__main__':
    main()

'''
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
'''
