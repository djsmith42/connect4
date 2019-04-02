from ..moves import make_board_with_move
from ..players import RED as R, YELLOW as Y, EMPTY as e
from ..board import print_board
from pprint import pprint

def test_make_board_with_move__two_moves_from_empty():
    board = [
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]

    board, row = make_board_with_move(board, R, 0)

    assert row == 0
    assert board == [
        [R, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]

    board, row = make_board_with_move(board, Y, 0)

    assert row == 1
    assert board == [
        [R, e, e, e, e, e, e],
        [Y, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
