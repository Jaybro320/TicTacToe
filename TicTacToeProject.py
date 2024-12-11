board = [[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]
]
player = "X"
def draw_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
def update_board(board, column, row, player):
    if board[row][column] == " ":
        board[row][column] = player
    else:
        print("Invalid move, space taken. Try again")
        return False
    return True
def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    for column in range(3):
        if board[0] [column] == board[1] [column] == board[2] [column] and board[0] [column] != " ":
            return True
    if board[0] [0] == board[1] [1] == board[2] [2] and board[0] [0] != " ":
        return True
    if board[0] [2] == board[1] [1] == board[2] [0] and board[0] [2] != " ":
        return True
    return False
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
#Input and game loop for placing X or O and switching players
while True:
    draw_board(board)
    print(f"{player}'s turn")
    try:
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): ")) 
        if row < 0 or row > 2 or column < 0 or column > 2:
            print("Invalid input, please enter numbers between 0 and 2.")
            continue
        if not update_board(board, column, row, player):
            continue
        if check_win(board):
            draw_board(board)
            print(f"Player {player} wins!")
            break
        if is_draw(board):
            draw_board(board)
            print("It's a draw!")
        player = "O" if player == "X" else "X"
    except ValueError:
        print("Invalid input, please enter numeric values.")