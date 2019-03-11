

class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        print('Called __get__({}, {}, {})'.format(self, instance, instance_type))
        if instance is None: return self
        # getattr()
        #   - Not use __get__(), so this __get__() doesn't loop.
        #   - If you access to instance attribution using instance.attribution,
        #     instance and attribution is specified beforehand;
        #     instance and attribution is constant.
        #     Using getattr() enable to specify instance and attribution as variable.
        #   - In this case, it's useless that Field object has field because of using getattr()
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        print('Called __set__({}, {}, {})'.format(self, instance, value))
        setattr(instance, self.internal_name, value)


class Customer(object):
    first_name = Field('first_name')
    last_name = Field('last_name')


def main():
    customer = Customer()
    print('customer.__dict__ =', customer.__dict__)
    print()

    customer.first_name = 'Euclid'
    print('customer.__dict__ =', customer.__dict__)
    print('customer.first_name =', customer.first_name)


if __name__ == '__main__':
    main()
