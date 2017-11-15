#/usr/bin/python

def main():
    for _ in xrange(input()):
        n, m = map(int, raw_input().split())
        graph = {i: set() for i in xrange(1, n+1)}
        parent = {}
        visited = set()
        for _ in xrange(m):
            u, v = map(int, raw_input().split())
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            queue = [start]
            visited.add(start)

            while len(queue) > 0:
                u = queue.pop(0)
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)
                        parent[v] = u

        def get_distance(node):
            distance = 0
            if node not in visited:
                return -1
            while node in parent:
                distance += 6
                node = parent[node]
            return distance

        start = input()
        bfs(start)
        print ' '.join(str(get_distance(node)) for node in xrange(1, n+1) if node != start)

if __name__ == '__main__':
    main()
