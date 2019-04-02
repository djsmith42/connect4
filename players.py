RED = 'r'
YELLOW = 'y'
EMPTY = '-'

def pretty_player_name(player):
    if player == RED:
        return 'red'
    elif player == YELLOW:
        return 'yellow'
    else:
        assert False
