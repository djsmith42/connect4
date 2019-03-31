def print_board(title, board):
    print(title)
    for row in range(len(board)-1, -1, -1):
        columns = board[row]
        row_string = ' '.join(columns)
        print('{}: {}'.format(row, row_string))
