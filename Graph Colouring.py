# Graph Coloring for Australia Map using Backtracking

states = [
    "Western Australia",
    "Northern Territory",
    "South Australia",
    "Queensland",
    "New South Wales",
    "Victoria",
    "Tasmania"
]

# Adjacency Matrix for Australia Map
graph = [
    [0,1,1,0,0,0,0],  # WA
    [1,0,1,1,0,0,0],  # NT
    [1,1,0,1,1,1,0],  # SA
    [0,1,1,0,1,0,0],  # Q
    [0,0,1,1,0,1,0],  # NSW
    [0,0,1,0,1,0,0],  # V
    [0,0,0,0,0,0,0]   # T
]

m = 3   # Number of colors
n = len(states)
colors = [0] * n

def is_safe(v, c):
    for i in range(n):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(v):
    if v == n:
        return True

    for c in range(1, m + 1):
        if is_safe(v, c):
            colors[v] = c
            if graph_coloring(v + 1):
                return True
            colors[v] = 0
    return False


if graph_coloring(0):
    print("Australia Map Coloring Solution:\n")
    for i in range(n):
        print(states[i], "-> Color", colors[i])
else:
    print("No valid coloring possible")
