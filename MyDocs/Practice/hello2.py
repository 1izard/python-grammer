print('hello2')

def print_hello2():
    print('Called print_hello2()')

class Hello2(object):
    def __new__(cls, arg):
        print('Called __new__({})'.format(cls))
        # print('*args =', *args)
        print(super().__new__(cls).__dict__)
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value

hello2 = Hello2(2)
print('hello2.value in hello2.py =', hello2.value)