class LazyDB(object):
    def __init__(self):
        self.exists1 = 5
        self.exists2 = 10

    def __getattr__(self, name):
        value = 'Value for {}'.format(name)
        setattr(self, name, value)
        return value


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__({})'.format(name))
        return super().__getattr__(name)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__({})'.format(name))
        try:
            return super().__getattribute__(name)
        except AttributeError:
            print('AttributionError')
            value = 'Value for {}'.format(name)
            setattr(self, name, value)
            return value


class DictionaryDB(dict):
    def __getattribute__(self, name):
        return super().__getitem__(name)


def main():
    data = LazyDB()
    print('Before:', data.__dict__)
    print('foo;', data.foo)
    print('After:', data.__dict__)
    print()

    data = LoggingLazyDB()
    print('Before:', data.__dict__)
    print('foo;', data.foo)
    print('After:', data.__dict__)
    print()

    data3 = ValidatingDB()
    print('foo exists:', hasattr(data3, 'foo'))
    print('foo exists:', hasattr(data3, 'foo'))
    print()

    ddb1 = DictionaryDB()
    ddb1['foo'] = 'foooo'
    print('ddb1.foo:', ddb1.foo)

if __name__ == '__main__':
    main()