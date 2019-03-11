import pickle

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4
        self.points = 0

state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print('state_after.__dict__ =', state_after.__dict__)
# state_after.__dict__ = {'level': 0, 'lives': 4, 'points': 0}

with open('game_state.bin', 'rb') as f:
    state_after = pickle.load(f)
print('state_after.__dict__ =', state_after.__dict__)
# state_after.__dict__ = {'level': 1, 'lives': 3}

assert isinstance(state_after, GameState)
# pass