from ..board import is_column_full, is_board_full
from ..players import RED as R, YELLOW as Y, EMPTY as e

def test_is_column_full():
    board = [
        [R, R, e, e, e, e, e],
        [Y, R, e, e, e, e, e],
        [R, R, e, e, e, e, e],
        [Y, R, e, e, e, e, e],
        [R, R, e, e, e, e, e],
        [Y, e, e, e, e, e, e],
    ]

    assert is_column_full(board, 0) is True
    assert is_column_full(board, 1) is False
    assert is_column_full(board, 2) is False
    assert is_column_full(board, 3) is False
    assert is_column_full(board, 4) is False
    assert is_column_full(board, 5) is False
    assert is_column_full(board, 6) is False

def test_is_board_full_negative():
    board = [
        [R, R, e, e, e, e, e],
        [Y, R, e, e, e, e, e],
        [R, R, e, e, e, e, e],
        [Y, R, e, e, e, e, e],
        [R, R, e, e, e, e, e],
        [Y, e, e, e, e, e, e],
    ]

    assert is_board_full(board) is False

def test_is_board_full_positive():
    board = [
        [R, Y, R, Y, R, Y, R],
        [Y, R, Y, R, Y, R, Y],
        [R, Y, R, Y, R, Y, R],
        [Y, R, Y, R, Y, R, Y],
        [R, Y, R, Y, R, Y, R],
        [Y, R, Y, R, Y, R, Y],
    ]

    assert is_board_full(board) is True
