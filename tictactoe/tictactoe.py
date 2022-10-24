"""
Tic Tac Toe Player
"""

import copy
import math
from queue import Empty

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
    numX, numO = 0, 0
    for col in board:
        for cell in col:
            if cell == 'X':
                numX += 1
            elif cell == 'O':
                numO += 1

    if numX > numO:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Action is not valid')

    boardWithAction = copy.deepcopy(board)
    boardWithAction[action[0]][action[1]] = player(board)
    return boardWithAction


def winner(board):
    """
    Returns the winner of the game, if there is one, else returns None.
    """
    combinations = [((0, 0), (0, 1), (0, 2)),
                    ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)),
                    ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)),
                    ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 1), (2, 2)),
                    ((2, 0), (1, 1), (0, 2))]

    for combination in combinations:
        i, j = combination[0]
        i1, j1 = combination[1]
        i2, j2 = combination[2]
        if board[i][j] == board[i1][j1] == board[i2][j2]:
            if board[i][j] == X or board[i][j] == O:
                return board[i][j]

    # no winner is detected
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    wnr = winner(board)
    if wnr == X:
        return 1
    elif wnr == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    """

    alpha = float(-math.inf)
    beta = float(math.inf)

    if player(board) == X:
        return maxValue(board, alpha, beta)[0]
    else:
        return minValue(board, alpha, beta)[0]


def maxValue(board, alpha, beta):
    v = float(-math.inf)
    act = None

    if terminal(board):
        return (act, utility(board))

    for action in actions(board):
        test = minValue(result(board, action), alpha, beta)[1]

        alpha = max(alpha, test)

        if test > v:
            v = test
            act = action

        if alpha >= beta:
            break

    return act, v


def minValue(board, alpha, beta):
    v = float(math.inf)
    act = None

    if terminal(board):
        return (act, utility(board))

    for action in actions(board):
        test = maxValue(result(board, action), alpha, beta)[1]

        beta = min(beta, test)

        if test < v:
            v = test
            act = action

        if alpha >= beta:
            break

    return act, v
