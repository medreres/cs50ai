"""
Tic Tac Toe Player
"""

import copy
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
    numxX, numO = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                numX += 1
            elif cell == 'O':
                numO += 1

    if numX > numO:
        return "O"
    else:
        return "X"
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # TODO action is not valid
    if len(action) == 0:
        raise Exception("Action is not valid")

    # ? action returns (i,j)
    boardWithAction = copy.deepcopy(board)
    boardWithAction[action[0]][action[1]] = player(board)
    return boardWithAction


def winner(board):
    """
    Returns the winner of the game, if there is one, else returns None.
    """
    # ? detect winner
    combinations = [((0, 0), (0, 1), (0, 2)),
                    ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)),
                    ((1, 0), (2, 0), (3, 0)),
                    ((1, 1), (2, 1), (3, 1)),
                    ((1, 2), (2, 2), (3, 2)),
                    ((0, 0), (1, 1), (2, 2)),
                    ((0, 2), (1, 1), (2, 0))]
    
    for combination in combinations:
        i,j = combination[0]
        i1,j1 = combination[1]
        i2,j2 = combination[2]
        if board[i][j] == board[i1][j1] == board[i2][j2]:
            return board[i][j]

    # no winner is detected
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # if at least one cell is None, then board is not filled full yet
    allCellsAreFilled = True
    for row in board:
        for cell in row:
            if cell is None:
                allCellsAreFilled = False

    if allCellsAreFilled or winner(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
