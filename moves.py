from dimensions import BOARD_ROW_COUNT
from players import EMPTY
from copy import deepcopy
from exceptions import InvalidMove

def make_board_with_move(board, player, column):
    row = find_landing_row(board, column)
    if row is not None:
        new_board = deepcopy(board)
        new_board[row][column] = player
        return new_board, row
    else:
        raise InvalidMove

def find_landing_row(board, column):
    for row in range(BOARD_ROW_COUNT):
        if board[row][column] == EMPTY:
            return row
    return None
