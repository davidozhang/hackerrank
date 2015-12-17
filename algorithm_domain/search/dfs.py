#!/usr/bin/python

'''
Sample learning code of Depth First Search - Not actually part of any challenge
'''

def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)	# Add only unvisited adjacent vertices
	return visited

if __name__ == '__main__':
	graph = {'A': set(['B', 'C']),
		 'B': set(['A', 'D', 'E']),
		 'C': set(['A', 'F']),
		 'D': set(['B']),
  		 'E': set(['B', 'F']),
		 'F': set(['C', 'E'])}
	print dfs(graph, 'A')
