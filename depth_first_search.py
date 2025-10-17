# iterative way uses stack
def dfs_iterative(graph, node):
    visited = set()
    stack = [node]

    while stack:
        ref = stack.pop()
        if ref not in visited:
            print(ref)  # optional: show traversal
            visited.add(ref)
            stack.extend(reversed(graph[ref]))
    return visited

# recursive way
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node)  # optional: show traversal
        visited.add(node)
        for nbr in graph[node]:
            dfs_recursive(graph, nbr, visited)
    return visited



