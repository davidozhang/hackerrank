#!/usr/bin/python

def bfs(g, s):
    visited = set([s])
    queue = [s]

    while len(queue)>0:
        u = queue.pop(0)
        for i in g[u]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return visited
    
def main():
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
    print bfs(g, 1)

if __name__ == '__main__':
    main()       
