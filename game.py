from pprint import pprint

from dimensions import BOARD_ROW_COUNT, BOARD_COLUMN_COUNT
from players import RED, YELLOW, EMPTY, pretty_player_name
from wins import is_winning_board
from strategies import perfect_defender
from board import print_board
from moves import make_board_with_move, other_player, is_board_full

board = [[EMPTY for column in range(BOARD_COLUMN_COUNT)] for row in range(BOARD_ROW_COUNT)]
player = RED
turn = 0

while True:
    turn += 1
    player = other_player(player)
    column = perfect_defender.next_move(board, player)
    assert column is not None
    board, row = make_board_with_move(board, player, column)
    print('{} chooses column {} to land at row {}'.format(pretty_player_name(player), column, row))
    print_board('After turn {}:'.format(turn), board)

    if is_winning_board(board, player, row, column):
        print('Game over, {} wins after {} turns'.format(pretty_player_name(player), turn))
        break

    if is_board_full(board):
        print('Game over, draw after {} turns'.format(turn))
        break
