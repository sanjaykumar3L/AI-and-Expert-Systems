# N-Queen Problem (Backtracking)

N = 4  # You can change N to any size

board = [["-" for _ in range(N)] for _ in range(N)]

def print_board(b):
    for row in b:
        print(row)

def is_safe(b, row, col):
    for i in range(col):
        if b[row][i] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if b[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if b[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True

def solve(col):
    if col == N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            if solve(col + 1):
                return True
            board[row][col] = "-"

    return False


print("Before placing queens:")
print_board(board)

solve(0)

print("\nAfter placing queens:")
print_board(board)
