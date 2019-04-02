from dimensions import BOARD_COLUMN_COUNT, BOARD_ROW_COUNT
from moves import find_landing_row

def print_board(title, board):
    assert isinstance(board, list)
    print(title)
    column_headers = [str(x) for x in range(len(board[0]))]
    print('   ' + ' '.join(column_headers))
    for row in range(len(board)-1, -1, -1):
        columns = board[row]
        row_string = ' '.join(columns)
        print('{}  {}'.format(row, row_string))

def is_column_full(board, column):
    assert column >= 0, column
    assert column < BOARD_COLUMN_COUNT, column
    return find_landing_row(board, column) is None

def is_board_full(board):
    for column in range(BOARD_COLUMN_COUNT):
        if not is_column_full(board, column):
            return False
    return True

