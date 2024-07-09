def topological_sort_dfs(graph):
    def dfs(node, visited, stack):
        visited[node] = True
        for neighbor, _ in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

    n = len(graph)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    return stack[::-1]

def longest_path(graph):
    topo_order = topological_sort_dfs(graph)
    n = len(graph)
    dist = [float('-inf')] * n

    has_incoming_edge = [False] * n
    for node_edges in graph:
        for j, _ in node_edges:
            has_incoming_edge[j] = True
    for i in range(n):
        if not has_incoming_edge[i]:
            dist[i] = 0

    for node in topo_order:
        if dist[node] != float('-inf'):
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight

    return max(dist)

graph = [
    [(1, 3), (2, 6)],
    [(2, 4), (3, 4), (4, 11)],
    [(3, 8)],           
    [(4, -4)],          
    []                  
]

print("The length of the longest path is:", longest_path(graph))
