# Tic Tac Toe with Minimax AI

board = [
    ['X', 'O', 'X'],
    ['-', 'O', '-'],
    ['-', '-', '-']
]

def print_board(b):
    for row in b:
        print(row)

def is_terminal(b):
    lines = [
        b[0], b[1], b[2],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]]
    ]
    for L in lines:
        if L[0] == L[1] == L[2] != '-':
            return True
    return all(cell != '-' for row in b for cell in row)

def evaluate(b):
    lines = [
        b[0], b[1], b[2],
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]]
    ]
    for L in lines:
        if L[0] == L[1] == L[2] == 'X':
            return 1
        if L[0] == L[1] == L[2] == 'O':
            return -1
    return 0

def get_moves(b):
    moves = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == '-':
                moves.append((i, j))
    return moves

def make_move(b, r, c, sym):
    new = [row[:] for row in b]
    new[r][c] = sym
    return new

def minimax(b, depth, max_turn):
    if depth == 0 or is_terminal(b):
        return evaluate(b)

    if max_turn:
        best = -999
        for (r, c) in get_moves(b):
            val = minimax(make_move(b, r, c, 'X'), depth - 1, False)
            best = max(best, val)
        return best

    else:
        best = 999
        for (r, c) in get_moves(b):
            val = minimax(make_move(b, r, c, 'O'), depth - 1, True)
            best = min(best, val)
        return best


print("Before AI move:")
print_board(board)

best_val = -999
best_move = None

for (r, c) in get_moves(board):
    val = minimax(make_move(board, r, c, 'X'), 9, False)
    if val > best_val:
        best_val = val
        best_move = (r, c)

r, c = best_move
board[r][c] = 'X'

print("\nAfter AI move:")
print_board(board)
