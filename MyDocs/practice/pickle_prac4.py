'''
copyreg usage for management of pickled instance's class version
'''
import pickle
import copyreg


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)

def unpickle_game_state(kwargs):
    return GameState(**kwargs)


copyreg.pickle(GameState, pickle_game_state)
state = GameState()
serialized = pickle.dumps(state)


class GameState(object):
    def __init__(self, level=0, points=0, magic=5):
        self.level = level
        self.points = points
        self.magic = magic


# state_after = pickle.loads(serialized)

# Traceback (most recent call last):
#   File "pickle_prac4.py", line 33, in <module>
#     state_after = pickle.loads(serialized)
#   File "pickle_prac4.py", line 18, in unpickle_game_state
#     return GameState(**kwargs)
# TypeError: __init__() got an unexpected keyword argument 'lives'


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    kwargs['version'] = 2
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    version = kwargs.pop('version', 1)
    if version == 1:
        kwargs.pop('lives')
    return GameState(**kwargs)


copyreg.pickle(GameState, pickle_game_state)
state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print('state_after.__dict__ =', state_after.__dict__)
# state_after.__dict__ = {'level': 0, 'points': 0, 'magic': 5}
