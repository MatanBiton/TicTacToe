"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math
from re import U
from tkinter import HORIZONTAL

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
    count = 0
    for row in board:
        for cell in row:
            if cell is not EMPTY:
                count += 1
    if count == 0:
        return X
    return X if count % 2 == 0 else O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                actions.add((i,j))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board=board):
        raise ValueError("Impossible action entered")
    deep_copy = deepcopy(board)
    deep_copy[action[0]][action[1]] = player(board=board)
    return deep_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    count = 0
    #horizontal victory
    for i, row in enumerate(board):
        count = 0
        for j in range(2):
            if row[j] is row[j+1]:
                count += 1
        if count == 2:
            return row[i]
    
    count = 0
    #vertical victory
    for j in range(3):
        count = 0
        for i in range(2):
            if board[i][j] == board[i + 1][j]:
                count += 1
        if count == 2:
            return board[0][j]
    
    count = 0
    #top left -> buttom right diagonal victory
    for i in range(2):
        if board[i][i] == board[i+1][i+1]:
            count += 1
    if count == 2:
        return board[0][0]
    
    count = 0
    #buttom left -> top right diagonal victory
    for j in range(2):
        if board[2 - j][j] == board[1 - j][j + 1]:
            count += 1
    if count == 2:
        return board[0][2]
    
    return None
            
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board=board) is not None
    count = 0
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            count += 1 if cell is not EMPTY else 0
    return win or count == 9
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board=board) is X else -1 if winner(board=board) is O else 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best = 0
    move = (-1, -1)
    is_max = player(board) == X
    if is_max:
        best = -10
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best:
                best = value
                move = action
        
    else:
        best = 10
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best:
                best = value
                move = action
    return move
    

def min_value(board):
    best = 10
    if terminal(board):
        return utility(board)
    for action in actions(board):
        best = min(best, max_value(result(board, action)))
    return best


def max_value(board):
    best = -10
    if terminal(board):
        return utility(board)
    for action in actions(board):
        best = max(best, min_value(result(board, action)))
    return best





