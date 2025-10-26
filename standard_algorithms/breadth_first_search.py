from collections import deque

def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


# example

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

breadth_first_search(graph, 'A')