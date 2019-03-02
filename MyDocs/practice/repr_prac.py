class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = OpaqueClass(1, 2)
print(obj)
# <__main__.OpaqueClass object at 0x10bbb76d8>



class BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'BetterClass({}, {})'.format(self.x, self.y)


obj = BetterClass(1, 2)
print(obj)
print(obj.__dict__)
# BetterClass(1, 2)
# {'x': 1, 'y': 2}

