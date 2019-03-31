from pprint import pprint

from dimensions import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT
from players import RED as R, YELLOW as Y, EMPTY as E
from exceptions import InvalidMove
from wins import is_winning_board

STARTING_BOARD = [[EMPTY for column in range(BOARD_COLUMN_COUNT)] for row in range(BOARD_ROW_COUNT)]

#def open_row_for_column(board, column):
#    # column is full:
#    if board[BOARD_ROW_COUNT-1][column] != EMPTY:
#        return None
#    # column is empty:
#    if board[0][column] == EMPTY:
#        return 0
#    # Find the top empty cell for this column:
#    for row in range(BOARD_ROW_COUNT-1, 0, -1):
#        if board[row][column] == EMPTY and board[row-1][column] != EMPTY:
#            return row
#    assert False

