from dimensions import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT
from players import EMPTY, RED, YELLOW
from copy import deepcopy
from errors import InvalidMove

def make_board_with_move(board, player, column):
    assert column >= 0, column
    assert column < BOARD_COLUMN_COUNT, column
    row = find_landing_row(board, column)
    if row is not None:
        new_board = deepcopy(board)
        new_board[row][column] = player
        return new_board, row
    else:
        raise InvalidMove

def find_landing_row(board, column):
    assert column >= 0, column
    assert column < BOARD_COLUMN_COUNT, column
    for row in range(BOARD_ROW_COUNT):
        if board[row][column] == EMPTY:
            return row
    return None

def other_player(player):
    if player == RED:
        return YELLOW
    elif player == YELLOW:
        return RED
    else:
        assert False
