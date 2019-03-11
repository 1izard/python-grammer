class Meta(type):
    # __new__ of MetaClass is called when the program is compiled,
    # before the instance associated with MetaClass is created.
    # So We can examine if class is based on the rule defined on MetaClass before execute the program.
    # Be careful __new__() of MetaClass is different from __new__() of object.
    def __new__(meta, name, bases, class_dict):
        print('Called __new__({})'.format(meta))
        print(meta)
        print(name)
        print(bases)
        print(class_dict)
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


class MyClass2(object, metaclass=Meta):
    def __init__(self):
        print('Called __init__({})'.format(self))
        super().__init__()


class MyClass3(object):
    # __new__() of object is called when create the instance.
    # __new__() should return the instance because __init__() use the instance to customize.
    def __new__(cls):
        print('Called __new__({})'.format(cls))
        return super().__new__(cls)

    def __init__(self):
        print('Called __init__({})'.format(self))
        super().__init__()


# Do not examine base class by metaclass
# because it is not to examine base class attribution.
# Base class define the class attribution,
# Meta class define the rule,
# and we expect to examine if the class attribution of class created from base class follows
# the rule defined by meta class.
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ sides')
        return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


class Triangle(Polygon):
    sides = 3



def main():
    print('hello')
    my_class = MyClass()
    my_class = MyClass()
    print()

    my_class = MyClass2()
    my_class = MyClass2()
    print()

    my_class = MyClass3()

    '''
    Called __new__(<class '__main__.Meta'>)
    <class '__main__.Meta'>
    MyClass
    (<class 'object'>,)
    {'__module__': '__main__', '__qualname__': 'MyClass', 'stuff': 123, 'foo': <function MyClass.foo at 0x10de60b70>}
    Called __new__(<class '__main__.Meta'>)
    <class '__main__.Meta'>
    MyClass2
    (<class 'object'>,)
    {'__module__': '__main__', '__qualname__': 'MyClass2', '__init__': <function MyClass2.__init__ at 0x10de60bf8>, '__classcell__': <cell at 0x10dd8ef48: empty>}
    hello
    
    Called __init__(<__main__.MyClass2 object at 0x10de6bb00>)
    Called __init__(<__main__.MyClass2 object at 0x10de6bb38>)
    
    Called __new__(<class '__main__.MyClass3'>)
    Called __init__(<__main__.MyClass3 object at 0x10de6bb00>)
    '''



if __name__ == '__main__':
    main()