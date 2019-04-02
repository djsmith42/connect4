from ..moves import make_board_with_move, find_landing_row, other_player
from ..players import RED as R, YELLOW as Y, EMPTY as e
from ..board import print_board, is_column_full
from ..errors import InvalidMove

import pytest

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

def test_make_board_with_move__InvalidMove():
    board = [
        [e, e, e, R, e, e, e],
        [e, e, e, R, e, e, e],
        [e, e, e, R, e, e, e],
        [e, e, e, R, e, e, e],
        [e, e, e, R, e, e, e],
        [e, e, e, R, e, e, e],
    ]

    with pytest.raises(InvalidMove):
        make_board_with_move(board, R, 3)

def test_find_landing_row():
    board = [
        [e, R, R, R, R, R, R],
        [e, e, R, R, R, R, R],
        [e, e, e, R, R, R, R],
        [e, e, e, e, R, R, R],
        [e, e, e, e, e, R, R],
        [e, e, e, e, e, e, R],
    ]

    assert find_landing_row(board, 0) == 0
    assert find_landing_row(board, 1) == 1
    assert find_landing_row(board, 2) == 2
    assert find_landing_row(board, 3) == 3
    assert find_landing_row(board, 4) == 4
    assert find_landing_row(board, 5) == 5
    assert find_landing_row(board, 6) is None

def test_other_player():
    assert other_player(R) == Y
    assert other_player(Y) == R
    with pytest.raises(AssertionError):
        other_player('foo')
