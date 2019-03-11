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



class MyClazz(object):
    def __str__(self):
        return 'This is __str__()'


obj = MyClazz()
print(obj)
# This is __str__()


# print() expresses __str__() prior to __repr__()
class MyClazz2(object):
    # __repr__() returns 'official' string.
    # Useful for debug.
    def __repr__(self):
        return 'This is __repr__()'

    # __str__() returns 'informal' string.
    # Useful for UI.
    def __str__(self):
        return 'This is __str__()'


obj = MyClazz2()
print(obj)
# This is __str__()

