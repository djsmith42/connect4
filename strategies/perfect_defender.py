from wins import find_winning_column
from moves import is_column_full, other_player
from dimensions import BOARD_COLUMN_COUNT, BOARD_ROW_COUNT
from random import shuffle
from players import RED, YELLOW

def next_move(board, player):
    # Find column to win:
    column_to_win = find_winning_column(board, player)
    if column_to_win is not None:
        return column_to_win

    # Find column to defend:
    opponent = other_player(player)
    column_to_defend = find_winning_column(board, opponent)
    if column_to_defend is not None:
        return column_to_defend

    # Choose random column:
    columns = range(BOARD_COLUMN_COUNT)
    shuffle(columns)
    for column in columns:
        if not is_column_full(board, column):
            return column
