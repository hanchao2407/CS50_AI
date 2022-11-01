import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board =  [["X", "O", EMPTY],
            [EMPTY, EMPTY, EMPTY],
            ["X", EMPTY, "Y"]]

board2 =  [["O", "X", "O"],
            ["O", "X", "X"],
            ["O", EMPTY, "X"]]

board3 =  [[EMPTY, EMPTY, EMPTY],
            ["O", "X", "O"],
            [EMPTY, EMPTY, EMPTY]]

board4 =  [["X", "O", "X"],
            [EMPTY, "O", EMPTY],
            ["O", EMPTY, "X"]]

board5 =  [["O", "X", "X"],
            ["O", "X", "X"],
            ["X", "O", "X"]]

board6 = [["X", EMPTY, EMPTY],
            [EMPTY, EMPTY, "O"],
            [EMPTY, EMPTY, EMPTY]]

# print(ttt.player(board2))
print(ttt.minimax(board4))
# print(ttt.result(board, (2,0)))

# print(ttt.winner(board4))
# print([board[0][0], board[1][0], board[2][0]])
# print(ttt.terminal(board3))
# print(ttt.utility(board5))

