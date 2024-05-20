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
    # if board X > board O return O else return X
    count_X = 0
    count_O = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1

    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # prolazimo kroz svaki red i vratimo koordinatu praznog polja, koja ce predstavljati akciju

    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    validActions = actions(board=board)

    if action not in validActions:
        raise Exception("This action is not valid")

    nextMove = player(board=board)

    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = nextMove

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
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
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0



def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v
        
    
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    best_action = None

    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            action_value = minValue(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
    else:
        best_value = math.inf
        for action in actions(board):
            action_value = maxValue(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action

    return best_action

        
        
        
