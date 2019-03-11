class MyClass(object):
    class_field = 'One'

    def __init__(self, instance_field):
        self.instance_field = instance_field


def main():
    my_class = MyClass('Hello')
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)
    print()

    # MyClass.class_field is Not set 'Two'
    # because code below sets 'Two' into field of my_class instance.
    # Python newly adds the field into instance __dict__
    # when the filed doesn't exist in __dict__.
    my_class.class_field = 'Two'
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)
    print()

    # To set class field
    my_class.__class__.class_field = 'Two'
    print('my_class.__dict__ =', my_class.__dict__)
    print('my_class.__class__.__dict__ =', my_class.__class__.__dict__)
    print()

    print('my_class.instance_field =', my_class.instance_field)
    print('getattr() =', getattr(my_class, 'instance_field', 'Default'))
    print()

    setattr(my_class, 'instance_field', 'Goodnight')
    print('my_class.instance_field =', my_class.instance_field)
    print('getattr() =', getattr(my_class, 'instance_field', 'Default'))


if __name__ == '__main__':
    main()