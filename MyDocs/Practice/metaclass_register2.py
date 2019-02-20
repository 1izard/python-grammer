import json


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


def deserialize(data):
    params = json.loads(data)
    name = params['class']
    target_class = registry[name]
    return target_class(*params['args'])


class BetterSerializable(object):
    def __init__(self, *args):
        self.args = args

    # Be careful of json.dumps, not json.dump.
    def serialize(self):
        return json.dumps({
            'class': self.__class__.__name__,
            'args': self.args
        })


class EvenBetterPoint2D(BetterSerializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

register_class(EvenBetterPoint2D)


def main():
    point = EvenBetterPoint2D(5, 3)
    print('Before =', point)
    data = point.serialize()
    print('Serialized =', data)
    after = deserialize(data)
    print('After =', after)

if __name__ == '__main__':
    main()