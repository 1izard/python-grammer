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
    def __init__(self, ky_lst):
        super().__init__()
        for ky in ky_lst:
            self[ky] = []

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

    def __setitem__(self, ky, val):
        if self.__contains__(ky):
            lst = super().__getitem__(ky)
            lst.append(val)
            super().__setitem__(ky, lst)
        else:
            super().__setitem__(ky, [val])


my_dict5_a = MyDict5()
print(type(my_dict5_a))
my_dict5_a['Apple'] = 'iPhoneXS'
my_dict5_a['Apple'] = 'iPhone4S'
my_dict5_a['Huawei'] = 'Huawei P10'
my_dict5_a['Huawei'] = 'Huawei P20 lite'
print(my_dict5_a)
'''
<class '__main__.MyDict5'>
{'Apple': ['iPhoneXS', 'iPhone4S'], 'Huawei': ['Huawei P10', 'Huawei P20 lite']}
'''