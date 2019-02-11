# Function

def do_nothing():
    pass    # return None


def agree():
    return True

if agree():
    print("True")
else:
    print("False")


def menu(wine, entree, dessert):
    return {"wine": wine, "entree": entree, "dessert": dessert}

menu("chardonnay", "chicken", "cake")
menu("chicken", "chardonnay", "cake")   # not expected {"wine": "chicken" "entree": "chardonnay", "dessert": "cake"}
menu(entree="chicken", wine="chardonnay", dessert="cake")
menu("chardonnay", dessert="cake", entree="chicken")
menu("chicken", wine="chardonnay", dessert="cake")  # TypeError: multiple values for "wine"


# default value
# [important1] : default value is evaluated when the function is defined. Don't use mutable value as default value.
def menu(wine, entree, dessert="cake"):
    return {"wine": wine, "entree": entree, "dessert": dessert}

menu("chardonnay", "chicken")
menu("chardonnay", "chicken", "pudding")
# {"wine": "chardonnay", "entree": "chicken", "dessert": "pudding"} because of [important1]

def a_func(arg, result=[]):
    result.append(arg)
a_func("a")      # result=["a"]
a_func("b")      # result=["a", "b"] because of [important1]

def a_func(arg):
    result = []
    result.append(arg)
a_func("a")      # result=["a"]
a_func("b")      # result=["b"]

def a_func(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
a_func("a")     # result=["a"]
a_func("b")     # result=["b"]

# cf.
def a_func(arg=2):
    print(arg)
a_func()    # 2
a_func(3)   # 3
a_func()    # 2
# I think that Function has two type of field or parameter, hided from our view.
# one case of call with argument and another case of call without argument.
# in case of call without argument Function use default value it having in itself field.
# if the field of call without argument (i.e. default value) is mutable, the value is stored and changed at every call.


# *args
# collect arguments into a tuple.
def print_more(required1, required2, *args):
    print("Need this one:", required1)
    print("Need this one too:", required2)
    print("All the rest:", args)        # not "*args"
print_more("cap", "gloves", "scarf", "monocle", "mustache wax")
# Need this one: cap
# Need this one too: gloves
# All the rest: (scaf, monocle, mustache wax)


# **kwags
# collect arguments into a dictionary.
def print_kwargs(**kwargs):
    print("Keyword arguments:", kwargs)
print_kwargs(wine="merlot", entree="mutton", dessert="macaroon")
# Keyword arguments: {"dessert": "macaroon", "wine": "merlot", "entree": "mutton"}


# docstring
def print_if_true(thing, check):
    '''
    :param thing: value to print
    :param check: if print arg or not
    :return: thing
    '''
    if check:
        print(thing)
print_if_true(3, True)      # 3
help(print_if_true)
#Help on function print_if_true in module test:

#print_if_true(thing, check)
#    :param thing: value to print
#    :param check: if print arg or not
#    :return: thing
print(print_if_true.__doc__)
#    :param thing: value to print
#    :param check: if print arg or not
#    :return: thing


# As an object
def run_with_positional_args(func, *args):
    return func(*args)      # not "args" because of [reference1]
def sum_args(*args):
    return sum(args)        # not "*args" because of [reference2]
run_with_positional_args(sum_args, 1, 2, 3, 4)      # 10

# [reference1]
def run(func, *args):
    print("*args:", *args)   # *args: 1 2 3 4
    print("args:", args)     # args: (1, 2, 3, 4)
    return func(args)
def sum_args(*args):
    print("*args:", *args)  # *args: (1, 2, 3, 4)
    print("args:", args)    # args: ((1, 2, 3, 4),)
    return sum(args)        # TypeError
run(sum_args, 1, 2, 3, 4)

# [reference2]
def run(func, *args):
    return func(*args)
def sum_args(*args):
    return sum(*args)       # TypeError: sum expected at most 2 arguments, got 4
run(sum_args, 1, 2, 3, 4)


# Inner Function
def knights(saying):
    def inner(quote):
        return "Hello, '%s'!" % quote
    return inner(saying)
knights("World")


# Closure
# Closure is Function created dynamically in outer Function.
# inner2 is Closure below example.
def knights2(saying):
    def inner2():       # Function "inner2" can use outer Function arguments "saying".
        return "Hello, '%s'!" % saying
    return inner2       # return Function "inner2" itself
a = knights2("Nick")
b = knights2("Michel")
a()     # Hello, Nick!  because a is inner2 to return "Hello, Nick!"
b()     # Hello, Michel!    because b is inner2 to return "Hello, Michel"


# Lambda Function
order = ["first", "second", "third"]
def cap_order(words, func):
    for word in words:
        print(func(word))
cap_order(order, lambda word: word.capitalize())    # First Second Third


# Generator [Function]
sum(range(1, 5))    # 10
# my_range is Generator [Function], not generator object.
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number        # yield expression creates and returns generator [object]
        number += step
ranger = my_range(1, 5)     # range <generator object my_range>
for i in ranger:
    print(i)        # 1, 2, 3, 4


# Decorator
# Decorator is used to decorate the Function without change its sourcecode.
def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function

# Measure1
def add_ints(a, b):
    return a + b
add_ints(3, 5)
cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

# Measure2
@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8

# Multiple Decorator is available.
# decorators are applied in order from the nearest Decorator from Function.
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function
@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64
# 64
@square_it
@document_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 64


# Scope and Namespace
# Access to global variable from Function
word = "global"
def change_and_print_global():
    global word
    word = "local"
    print(word)
print(word)                 # "global"
change_and_print_global()   # "local"
print(word)                 # "local"


# _ && __
# func.__name__     # return name of func
# func.__doc__      # return doc (e.g. '''arg: xxx return: yyy''' in func) of func


# Exception
short_list = [1, 2, 3]
while True:
    value = input("Position [q to quit]? ")
    if value == "q":
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print("Bad index: ", position)
    except Exception as other:
        print("Something else broke: ", other)

# Create Exception class
