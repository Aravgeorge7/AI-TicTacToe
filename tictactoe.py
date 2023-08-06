
import random
import copy


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
    c = 0
    d = 0
    for i in board:
        c += i.count("X")
        d += i.count("O")

    if c > d:
        return "O"
    else:
        return "X"


def actions(board):


    store = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                store.add((i, j))

    return store


def result(board, action):

    board_copy = copy.deepcopy(board)

    if action not in actions(board_copy):
        raise NotImplementedError

    for i in range(3):
        for j in range(3):
            if (i, j) == action:
                board_copy[i][j] = player(board_copy)
    return board_copy


def winner(board):


    for i in range(3):
        count_0 = 0
        count_X = 0
        for j in range(3):
            if board[i][j] == "X":
                count_X += 1
                count_0 = 0
            elif board[i][j] == "O":
                count_0 += 1
                count_X = 0

            if count_0 == 3:
                return "O"
            elif count_X == 3:
                return "X"
    if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[1][1]
    if board[0][0] == board[1][0] and board[2][0] == board[1][0]:
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[1][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[1][2]

    return None


def terminal(board):

    counter = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                counter += 1
    if counter == 9:
        return True
    if winner(board) == "X" or winner(board) == "O":
        return True

    return False


def utility(board):

    if winner(board) == "X":
        return 1
    if winner(board) == "O":
        return -1
    if winner(board) is None:
        return 0


def minimax(board):

    if len(actions(board)) == 9:
        k = random.randint(0, 2)
        j = random.randint(0, 2)
        return (k, j)

    x = 0
    d1 = {}
    d2 = {}

    def MAX_VALUE(board, d={}):
        if terminal(board):
            return utility(board), d

        v = -10
        d5 = {}
        for action in actions(board):
            x = MIN_VALUE((result(board, action)), d5)

            v = max(v, x[0])

            d[action] = v

        return v, d

    def MIN_VALUE(board, d_1={}):
        if terminal(board):
            return utility(board), d_1

        v = 10
        d4 = {}
        for action in actions(board):
            x = MAX_VALUE((result(board, action)), d4)

            v = min(v, x[0])
            d_1[action] = v
        return v, d_1

    if terminal(board):
        return None

    play = player(board)
    value = 0
    if play == "X":
        value = MAX_VALUE(board, d1)
        for i in d1:
            if d1[i] == value[0]:
                return i

    else:
        value = MIN_VALUE(board, d2)
        for i in d2:
            if d2[i] == value[0]:
                return i