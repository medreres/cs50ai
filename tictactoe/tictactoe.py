"""
Tic Tac Toe Player
"""

import copy
import math
import random

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


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i, j))
    if len(actions):
        return actions
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        raise Exception("Action is not valid")

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
                    ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)),
                    ((0, 2), (1, 2), (2, 2)),
                    ((0, 0), (1, 1), (2, 2)),
                    ((0, 2), (1, 1), (2, 0))]

    for combination in combinations:
        i, j = combination[0]
        i1, j1 = combination[1]
        i2, j2 = combination[2]
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
    wnr = winner(board)
    if wnr == 'X':
        return 1
    elif wnr == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    actionOutcome = []
    acts = actions(board)
    for action in acts:
        actionOutcome.append(maxValue(result(board,action)))

    # actionOutcome.sort()
    optimal = min(actionOutcome)

    return acts[actionOutcome.index(optimal)]





    # # if game is over return None
    # if terminal(board):
    #     return None

    # # take all possible actions and chose the best one
    # acts = actions(board)

    # if acts is not None:

    #     # take action and pass to result func let  make move
    #     outcomes = []
    #     for act in acts:
    #         rslt = result(board, act)

    #         if terminal(rslt):
    #             return utility(rslt)

    #         outcomes.append({'score': minimax(rslt), 'action': act})

    #     # take max value from outcomes

    # # call minimax for all of the acts and find out which is best
    #     ...


def maxValue(board):
    if terminal(board):
        return utility(board)

    v = float(-math.inf)

    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    
    return v

    


def minValue(board):
    if terminal(board):
        return utility(board)
    
    v = float(math.inf)

    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

        # if v less from all the choices available - do not study this branch deeper

    return v
