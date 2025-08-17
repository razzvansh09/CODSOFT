import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    # rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = "O"

# Game start
board = [[" " for _ in range(3)] for _ in range(3)]
print("Tic Tac Toe! You are X, AI is O.")

while True:
    print_board(board)
    # Player move
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    if board[row][col] == " ":
        board[row][col] = "X"
    else:
        print("Invalid move! Try again.")
        continue

    if check_winner(board) == "X":
        print_board(board)
        print("You win!")
        break
    elif is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    # AI move
    ai_move(board)
    if check_winner(board) == "O":
        print_board(board)
        print("AI wins!")
        break
    elif is_full(board):
        print_board(board)
        print("It's a draw!")
        break
