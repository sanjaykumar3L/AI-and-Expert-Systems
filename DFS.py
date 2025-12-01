# Graph represented as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(neighbour)

# Start DFS from node 'A'
dfs('A')
