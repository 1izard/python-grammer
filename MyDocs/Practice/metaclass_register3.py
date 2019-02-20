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


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class RegisteredSerializable(BetterSerializable, metaclass=Meta):
    pass


class Vector3D(RegisteredSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x, self.y, self.z = x, y, z


def main():
    point = Vector3D(10, -7, 3)
    print('Before point =', point)
    print('Before point.__dict__ =', point.__dict__)
    data = point.serialize()
    print('Serialized =', data)
    after = deserialize(data)
    print('After after =', after)
    print('After after.__dict__ =', after.__dict__)

if __name__ == '__main__':
    main()