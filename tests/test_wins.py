from ..players import YELLOW as Y, RED as R, EMPTY as e
from ..wins import find_winning_column

def test_win_horizontal_end_of_row():
    board = [
        [Y, Y, Y, e, e, e, e],
        [Y, e, Y, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 3

def test_win_horizontal_middle_of_row():
    board = [
        [e, Y, Y, Y, e, e, e],
        [e, e, Y, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 0

def test_win_vertical_stack_from_base():
    board = [
        [e, Y, e, e, Y, Y, e],
        [e, Y, e, e, Y, e, e],
        [e, e, e, e, Y, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 4

def test_win_vertical_stack_from_base():
    board = [
        [e, Y, e, e, Y, Y, e],
        [e, Y, e, e, Y, e, e],
        [e, e, e, e, Y, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 4

def test_win_diagonal_up_right_and_down_left():
    board = [
        [R, Y, R, R, Y, Y, R],
        [e, Y, R, R, Y, e, e],
        [e, e, Y, e, Y, e, e],
        [e, e, Y, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 3

def test_win_diagonal_down_right_and_up_left():
    board = [
        [R, Y, R, R, Y, Y, R],
        [e, Y, Y, R, R, e, e],
        [e, e, R, e, Y, e, e],
        [e, e, Y, e, Y, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 3

def test_win_diagonal_down_right_and_up_left_end_of_sequence():
    board = [
        [R, Y, R, R, Y, Y, R],
        [e, Y, Y, R, R, e, e],
        [e, e, R, Y, Y, e, e],
        [e, e, Y, e, e, e, e],
        [e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e],
    ]
    assert find_winning_column(board, Y) == 4
