class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        return type.__new__(meta, name, bases, class_dict)


class Field(object):
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class DatabaseRow(object, metaclass=Meta):
    pass


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()


def main():
    bc = BetterCustomer()
    print('bc.first_name =', bc.first_name)
    print('repr(bc.first_name) =', repr(bc.first_name))
    print('bc.__dict__ =', bc.__dict__)
    print()

    bc.first_name = 'FirstName'
    print('bc.first_name =', bc.first_name)
    print('repr(bc.first_name) =', repr(bc.first_name))
    print('bc.__dict__ =', bc.__dict__)
    print()

if __name__ == '__main__':
    main()