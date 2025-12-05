# Mini-Max for Perfect Binary Tree

def minimax(values, depth, index, max_turn):
    if depth == 0:
        return values[index]

    left  = minimax(values, depth - 1, 2 * index,     not max_turn)
    right = minimax(values, depth - 1, 2 * index + 1, not max_turn)

    if max_turn:
        return max(left, right)
    else:
        return min(left, right)


# -----------------------
# Example: perfect tree
# depth = 2 → 4 leaves
# -----------------------

values = [3, 5, 2, 9]   # leaf values
depth = 2               # 2 levels (root→internal→leaves)

result = minimax(values, depth, 0, True)

print("Leaf Nodes:", values)
print("Mini-Max Value:", result)
