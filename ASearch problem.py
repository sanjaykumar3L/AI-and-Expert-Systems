from heapq import heappush, heappop

def astar(graph, start, goal, h):
    pq = []
    heappush(pq, (0, start))
    g = {start: 0}
    parent = {start: None}

    while pq:
        f, node = heappop(pq)

        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g[goal]

        for neighbor, cost in graph[node]:
            new_g = g[node] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h[neighbor]
                parent[neighbor] = node
                heappush(pq, (f, neighbor))

    return None, None


# --------------------------
# TEST CASE (Required part)
# --------------------------

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 5,
    'G': 0
}

path, cost = astar(graph, 'A', 'G', heuristic)

print("Path Found:", path)
print("Total Cost:", cost)
