class MyClass(object):
    pass


class MyClass2():
    pass


def main():
    my_class = MyClass()
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)
    print()

    # Though MyClass and the instance doesn't define field, my_class can use field as instance field.
    my_class.field = 'One'
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)
    print()

    # In Python 3, class inherit object class as default.
    my_class = MyClass2()
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)

    '''
        my_class.__dict__ = {}
        my_class.__class__.__dict__ = {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
        
        my_class.__dict__ = {'field': 'One'}
        my_class.__class__.__dict__ = {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
        
        my_class.__dict__ = {}
        my_class.__class__.__dict__ = {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyClass2' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass2' objects>, '__doc__': None}
    '''


if __name__ == '__main__':
    main()