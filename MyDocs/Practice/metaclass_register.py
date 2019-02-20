import json

class Serializable(object):
    def __init__(self, *args):
        print('*args =', *args)
        print('args =', args)
        self.args = args

    def serialize(self):
        # tuple is transformed to list
        return json.dumps({'args': self.args})


class Point2D(Serializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        print('cls =', cls)
        params = json.loads(json_data)
        print('params =', params)
        return cls(*params['args'])


class BetterPoint2D(Deserializable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y


def main():
    point = Point2D(5, 3)
    print('Object =', point)
    print('Serialized =', point.serialize())
    print()

    point = BetterPoint2D(5, 3)
    print('Before =', point)
    data = point.serialize()
    print('Serialized =', data)
    after = BetterPoint2D.deserialize(data)
    print('After =', after)

if __name__ == '__main__':
    main()