# Knight's Tour using Backtracking

N = 8  # Chessboard size (8x8)

board = [[-1 for _ in range(N)] for _ in range(N)]

# All possible knight moves
moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

def print_board(b):
    for row in b:
        for val in row:
            print(f"{val:2}", end=" ")
        print()

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve_knight(x, y, move_no):
    if move_no == N * N:
        return True

    for k in range(8):
        next_x = x + moves_x[k]
        next_y = y + moves_y[k]

        if is_safe(next_x, next_y):
            board[next_x][next_y] = move_no
            if solve_knight(next_x, next_y, move_no + 1):
                return True
            board[next_x][next_y] = -1  # Backtracking

    return False


# Starting position
start_x, start_y = 0, 0
board[start_x][start_y] = 0

if solve_knight(start_x, start_y, 1):
    print("Knight's Tour Solution:\n")
    print_board(board)
else:
    print("No solution exists")
