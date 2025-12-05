from collections import deque

# Jug capacities
capA = 4
capB = 3
target = 2

# Initial state
start = (0, 0)

visited = set()
queue = deque()

# Start BFS with path included
queue.append([start])
visited.add(start)

solution = None

while queue:
    path = queue.popleft()
    (a, b) = path[-1]

    # Check if goal reached
    if a == target or b == target:
        solution = path
        break

    # All possible next states
    next_states = [
        (capA, b),                                          # Fill A
        (a, capB),                                          # Fill B
        (0, b),                                             # Empty A
        (a, 0),                                             # Empty B
        (a - min(a, capB - b), b + min(a, capB - b)),       # Pour A -> B
        (a + min(b, capA - a), b - min(b, capA - a))        # Pour B -> A
    ]

    for s in next_states:
        if s not in visited:
            visited.add(s)
            queue.append(path + [s])

# Print solution
print("Solution Steps:")
for step in solution:
    print(step)

