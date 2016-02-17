#!/usr/bin/python

def main():
    for _ in xrange(input()):
        g = {}
        for _ in xrange(input()):
            start, finish = map(int, raw_input().split())
            g[start] = finish
        for _ in xrange(input()):
            start, finish = map(int, raw_input().split())
            g[start] = finish
        queue = [1]
        parent = {}
        visited = set([1])
        while len(queue)>0 and 100 not in visited:
            u = queue.pop(0)
            if u in g:
                if g[u] in visited:
                    continue
                visited.add(g[u])
                queue.append(g[u])
                parent[g[u]] = u
            else:
                for dice in xrange(1, 7):
                    if u+dice in visited:
                        continue
                    visited.add(u+dice)
                    parent[u+dice] = u
                    if u+dice in g:
                        visited.add(g[u+dice])
                        queue.append(g[u+dice])
                        parent[g[u+dice]] = u
                    else:
                        queue.append(u+dice)
        if 100 not in visited:
            print -1
        else:
            result = 0
            temp = 100
            while temp != 1:
                #print temp
                temp = parent[temp]
                result += 1
            print result

if __name__ == '__main__':
    main()
