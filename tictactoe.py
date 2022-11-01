"""
Tic Tac Toe Player
"""

from audioop import ulaw2lin
from copy import deepcopy
from itertools import count
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                x_count += 1
            if board[i][j] == "O":
                o_count += 1
    if x_count <= o_count:
        return X
    else:
        return O 
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    pos_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                pos_actions.add((i, j))
    return pos_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # exception for invalid action
    if board[action[0]][action[1]] != EMPTY:
        raise NameError
    copy_board = deepcopy(board)
    copy_board[action[0]][action[1]] = player(copy_board)
    return copy_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal
    for i in range(len(board)):
        if set(board[i]) == {"X"}:
            return X
        if set(board[i]) == {"O"}:
            return O
    # vertical
    for i in range(len(board)):
        if set([board[0][i], board[1][i], board[2][i]]) == {"X"}:
            return X
        if set([board[0][i], board[1][i], board[2][i]]) == {"O"}:
            return O
    
    # diagonal
    if set([board[0][0], board[1][1], board[2][2]]) == {"X"} or set([board[0][2], board[1][1], board[2][0]]) == {"X"}:
            return X
    if set([board[0][0], board[1][1], board[2][2]]) == {"O"} or set([board[0][2], board[1][1], board[2][0]]) == {"O"}:
            return O
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False
    
    return True
    
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # determin if player is max or min
    if player(board) == "X":
        v, best = max_value(board)
        return best
    else:
        v, best = min_value(board)
        return best
    

def max_value(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return utility(board), None
    v = float('-inf')
    best = None
    for action in actions(board):
        v_new, ac = min_value(result(board, action))
        if v_new > v:
            best = action
            v = v_new
    return v, best


def min_value(board):
    """
    Returns the optimal action for the current player on the board.
    """


    if terminal(board):
        return utility(board), None
    v = float('inf')
    best = None

    for action in actions(board):
        v_new, ac = max_value(result(board, action))
        if v_new < v:
            best = action
            v = v_new
    return v, best