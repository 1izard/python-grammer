class MyClass(object):
    def __init__(self, b, a):
        self.a = a
        self.b = b

    def print_value(self):
        print('self.a =', self.a)
        print('self.b =', self.b)

myclass = MyClass(1, 2)
myclass.print_value()