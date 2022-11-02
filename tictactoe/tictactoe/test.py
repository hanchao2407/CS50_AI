import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None

board =  [["X", EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

print(ttt.player(board))