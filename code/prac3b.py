# 8-Queens Problem using Backtracking

N = 8
board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve(board, row + 1):
                return True
            board[row][col] = 0

    return False

if solve(board, 0):
    print("Solution:\n")
    for row in board:
        print(row)
else:
    print("No Solution Exists.")
