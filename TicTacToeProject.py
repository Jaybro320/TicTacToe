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
    if board[column][row] == " ":
        board[column][row] = player
    else:
        print("Invalid move, space taken. Try again")
draw_board(board)
update_board(board, 1, 1, "X")
draw_board(board)
#Input and game loop for placing X or O and switching players
while True:
    draw_board(board)
    column = int(input("Enter column (0-2): "))
    row = int(input("Enter row (0-2): ")) 
    update_board(board, column, row, player)
    player = "O" if player == "X" else "X"
    continue