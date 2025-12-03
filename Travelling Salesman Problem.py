import itertools
import sys

# Cities
cities = ['A', 'B', 'C', 'D']

# Distance Matrix (given distances between cities)
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cities)
start = 0
min_cost = sys.maxsize
best_path = None

# Generate all possible routes
for perm in itertools.permutations(range(1, n)):
    cost = 0
    k = start

    for i in perm:
        cost += distance[k][i]
        k = i

    cost += distance[k][start]  # return to starting city

    if cost < min_cost:
        min_cost = cost
        best_path = (start,) + perm + (start,)

# Print result
print("Shortest Path:")
for i in best_path:
    print(cities[i], end=" -> ")
print("END")

print("Minimum Cost:", min_cost)
