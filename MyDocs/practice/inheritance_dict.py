class MyDict1(dict):
    def __init__(self):
        super().__init__()
        self['Apple'] = 'iPhone'


my_dict1_a = MyDict1()
print(type(my_dict1_a))
print(my_dict1_a)

my_dict1_a['Huawei'] = 'HUAWEI'
print(my_dict1_a)

my_dict1_b = MyDict1()
print(my_dict1_b)

my_dict1_b['Samsung'] = 'Galaxy'
print(my_dict1_b)
print()

'''
<class '__main__.MyDict1'>
{'Apple': 'iPhone'}
{'Apple': 'iPhone', 'Huawei': 'HUAWEI'}
{'Apple': 'iPhone'}
{'Apple': 'iPhone', 'Samsung': 'Galaxy'}
'''


class MyDict2(MyDict1):
    def __init__(self):
        super().__init__()

my_dict2_a = MyDict2()
print(type(my_dict2_a))
print(my_dict2_a)
print()
'''
<class '__main__.MyDict2'>
{'Apple': 'iPhone'}
'''


class MyDict3(dict):
    def __init__(self, string):
        super().__init__()
        self[string] = 'iPhone'

my_dict3_a = MyDict3('Apple')
print(type(my_dict3_a))
print(my_dict3_a)
print()
'''
<class '__main__.MyDict3'>
{'Apple': 'iPhone'}
'''


class MyDict4(dict):
    def __init__(self, key_lst):
        super().__init__()
        for key in key_lst:
            self[key] = []

my_dict4_a = MyDict4(['Apple', 'Huawei', 'Samsung'])
print(type(my_dict4_a))
print(my_dict4_a)
print()
'''
<class '__main__.MyDict4'>
{'Apple': [], 'Huawei': [], 'Samsung': []}
'''


class MyDict5(dict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        if self.__contains__(key):
            lst = super().__getitem__(key)
            lst.append(value)
            super().__setitem__(key, lst)
        else:
            super().__setitem__(key, [value])


my_dict5_a = MyDict5()
print(type(my_dict5_a))
my_dict5_a['Apple'] = 'iPhoneXS'
my_dict5_a['Apple'] = 'iPhone4S'
my_dict5_a['Huawei'] = 'Huawei P10'
my_dict5_a['Huawei'] = 'Huawei P20 lite'
print(my_dict5_a)
print()
'''
<class '__main__.MyDict5'>
{'Apple': ['iPhoneXS', 'iPhone4S'], 'Huawei': ['Huawei P10', 'Huawei P20 lite']}
'''


class ResultHolder(dict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        if self.__contains__(key):
            lst = super().__getitem__(key)
            lst.append(value)
            super().__setitem__(key, lst)
        else:
            super().__setitem__(key, [value])

    def set_result(self, result_dict):
        for key, value in result_dict.items():
            self.__setitem__(key, value)

result_holder = ResultHolder()
print(type(result_holder))
result_dict1 = {
    'Apple': 'iPhone XS',
    'Huawei': 'HUAWEI P10 Pro'
}
result_dict2 = {
    'Apple': 'iPhone 4S',
    'Huawei': 'HUAWEI P20 lite'
}
result_holder.set_result(result_dict1)
result_holder.set_result(result_dict2)
print(result_holder)
print()
'''
<class '__main__.ResultHolder'>
{'Apple': ['iPhone XS', 'iPhone 4S'], 'Huawei': ['HUAWEI P10 Pro', 'HUAWEI P20 lite']}
'''

