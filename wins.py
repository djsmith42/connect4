from dimensions import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT
from players import RED, YELLOW
from exceptions import InvalidMove
from moves import make_board_with_move
from board import print_board

REQUIRED_CONSECUTIVE_PIECES = 4

def find_winning_column(board, player):
    for column in range(BOARD_COLUMN_COUNT):
        try:
            new_board, row = make_board_with_move(board, player, column)
            if is_winning_board(new_board, player, row, column):
                return column
        except InvalidMove:
            continue

def is_winning_board(board, player, start_row, start_column):
    return max_contiguous_length(board, player, start_row, start_column) >= REQUIRED_CONSECUTIVE_PIECES

def travel(board, player, start_row, start_column, up=None, down=None, left=None, right=None):
    assert not (up and down)
    assert not (left and right)
    assert player in (RED, YELLOW)

    if board[start_row][start_column] != player:
        return 0

    count = 0
    row, column = move(start_row, start_column, up=up, down=down, left=left, right=right)
    while row >= 0 and row < BOARD_ROW_COUNT and column >= 0 and column <= BOARD_COLUMN_COUNT:
        if board[row][column] == player:
            count += 1
        else:
            break

        row, column = move(row, column, up=up, down=down, left=left, right=right)

    return count

def move(row, column, up, down, left, right):
    assert up or down or left or right
    assert not (up and down)
    assert not (left and right)

    if up:
        row -= 1
    elif down:
        row += 1

    if left:
        column -= 1
    elif right:
        column += 1

    return row, column

def max_contiguous_length(board, player, row, column):
    if board[row][column] == player:
        horizontal = (1
                + travel(board, player, row, column, left=True)
                + travel(board, player, row, column, right=True))

        vertical = (1
                + travel(board, player, row, column, up=True)
                + travel(board, player, row, column, down=True))

        diagonal1 = (1
                + travel(board, player, row, column, up=True, right=True)
                + travel(board, player, row, column, down=True, left=True))

        diagonal2 = (1
                + travel(board, player, row, column, up=True, left=True)
                + travel(board, player, row, column, down=True, right=True))

        return max(horizontal, vertical, diagonal1, diagonal2)

    else:
        return 0
