import pickle
import copyreg


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    print('Called pickle_game_state')
    kwargs = game_state.__dict__
    # upickle_game_state() equals to GameState constructor.
    # Here the arguments is given by (kwargs,),
    # so use unpickle_game_state() to pass kwargs after transformed **kwargs
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


# copyreg.pickle(class, deserialize_method)
copyreg.pickle(GameState, pickle_game_state)
state = GameState()
state.points += 100
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print('state_after.__dict__ =', state_after.__dict__)
# Called pickle_game_state
# state_after.__dict__ = {'level': 0, 'lives': 4, 'points': 100}



class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

# Not work as expected
def pickle_game_state(game_state):
    print('Called pickle_game_state')
    kwargs = game_state.__dict__
    return GameState, (kwargs,)

# copyreg.pickle(class, deserialize_method)
copyreg.pickle(GameState, pickle_game_state)
state = GameState()
state.points += 100
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print('state_after.__dict__ =', state_after.__dict__)
# Called pickle_game_state
# state_after.__dict__ = {'level': {'level': 0, 'lives': 4, 'points': 100}, 'lives': 4, 'points': 0}
