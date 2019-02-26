'''
copyreg usage to resolve different class name of pickled instance
'''
import pickle
import copyreg


class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


state = GameState()
serialized = pickle.dumps(state)
print('serialized[:25] =', serialized[:25])
serialized[:25] = b'\x80\x03c__main__\nGameState\nq\x00)'
'''
"Import path" of serialized object class is GameState.
That causes AttributionError when anyone change class name after serialized.
Using copyreg resolves this problem.
'''

class BetterGameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


copyreg.pickle(BetterGameState, pickle_game_state)
state = BetterGameState()
serialized = pickle.dumps(state)
print('serialized[:35] =', serialized[:35])
state_after = pickle.loads(serialized)
print('state_after =', state_after)
print('state_after.__dict__ =', state_after.__dict__)
# serialized[:35] = b'\x80\x03c__main__\nunpickle_game_state\nq\x00}'
# state_after = <__main__.GameState object at 0x101fbfda0>
# state_after.__dict__ = {'level': 0, 'lives': 4, 'points': 0}
'''
When file of GameState class has been deleted and you had used just pickle, 
There is no measure to unpickle GameState instance.
copyreg defines deserialize method 
and sets the method(= unpickle_game_state) as import path.
pickle.loads executes based on import path.
That enables to deserialize deleted class 
after deleted GameState class
if define unpickle_game_state again for current class name.
maybe...
'''
