# Class

class Person():
    pass

class Person():
    def __init__(self):
        pass

class Person():
    def __init__(self, name):
        self.name = name

# [important1] class attribution vs instance attribution
class Person():
    name = "Spinoza"
print(Person.name)

class Person():
    def __init__(self, name):
        self.name = name
person = Person("Spinoza")
print(person.name)
print(Person.name)      # AttributeError

# [important2] class has only one __init__() method.


# inheritance
class Person():
    def introduce(self):
        print("I am a human.")
class Michel(Person):
    pass

# override
class Michel(Person):
    def introduce(self):
        print("I am Michel, Nice to meet you.")

class Person():
    def __init__(self, name):
        self.name = name
class Doctor(Person):
    def __init__(self, name):
        self.name = "Doctor" + name


# adding methods
class Doctor(Person):
    def __init__(self, name):
        self.name = "Doctor" + name
    def examine(self, part):
        print("Your " + part + " is bad.")

a_doctor = Doctor("Mario")
a_doctor.examine("liver")


class Student(Person):
    def __init__(self, name, school):
        super().__init__(self, name)
        self.school = school


# property()
# used as getter and setter
class Person():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name)
a_person = Person("Jack")
a_person.name   # inside the getter  "Jack"
a_person.get_name   # inside the getter "Jack"
a_person.name = "Michel"
a_person.name   # inside the getter  "Michel"
a_person.set_name("John")
a_person.name   # inside the getter  "John"

# Decorator
# the same as property().
class Person():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        self.hidden_name = input_name

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
c.radius            # 5
c.diameter          # 10
c.radius = 7
c.diameter          # 14
c.diameter = 17     # AttributeError



# @classmethod
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @staticmethod
    def ready():
        print("This is a static method.")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
A.ready()   # This is a static method.
a1 = A()
a2 = A()
a3 = A()
A.kids()    # A has 3 little objects.
a3.kids()   # A has 3 little objects.


# Polymorphism
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + "."
class QuestionQuote(Quote):
    def says(self):
        return self.words + "?"
class ExclamationQuote(Quote):
    def says(self):
        return self.words + "!"
class BabblingBrook():      # Not inherit Quote, but having methods of the same name.
    def who(self):
        return "Brook"
    def says(self):
        return "Babble"
def who_says(obj):
    print(obj.who(), "says", obj.says())

hunter = Quote("Elmer Fudd", "I'm hunting wabbits")
hunted1 = QuestionQuote("Bugs Bunny", "What's up, doc")
hunted2 = ExclamationQuote("Daffy Duck", "It's rabbit season")
brook = BabblingBrook()
who_says(hunter)    # Elmer Fudd says I'm hunting wabbits.
who_says(hunted1)   # Bugs Bunny says What's up, doc?
who_says(hunted2)   # Daffy Duck says It's rabbit season!
who_says(brook)     # Brook says Babble      this measure is called as "Duck typing"


# Special Method
class Word():
    def __init__(self, word1):
        self.word1 = word1
    def __eq__(self, word2):
        return self.word1.lower() == self.word2.lower()
    def __str__(self):
        return self.word1
    def __repr__(self):
        return "Word('" + self.word1 + "')"
first = Word("ha")
second = Word("Ha")
first == second     # True  because of __eq__
first    # __repr__
print(first)    # __str__

# __eq__
# __ne__    !=
# __lt__    <
# __gt__    >
# __le__    <=
# __ge__    >=

# __add__
# __sub__
# __mul__
# __floordiv__
# __truediv__
# __mod__
# __pow__

# __str__       str(self)
# __repr__      repr(self)
# __len__       len(self)


# Composition
class Bill():
    def __init__(self, description):
        self.description = description
class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, "tail")
tail = Tail("long")
bill = Bill("wide orange")
duck = Duck(bill, tail)


# Module vs Class
# - Class is useful when you need some instance having the same method and the different attribution.
# - Class can use inheritance, but Module cannot.
# - Module is better if you need just one something.
# - Class maybe better when you give some Function the variables having some values as argument.
# - Simple is the best. If dictionary, list, or tuple can be used, you should use them.


# __call__
# Callable class, having __call__ method, can be treated like function.
class MissingCounter():
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

import collections.defaultdict
org_dict = {'green': 12, 'blue': 3}
increments = [
    ('red', 5)
    ('blue', 17)
    ('orange, 9')
]
counter = MissingCounter()
after_dict = collections.defaultdict(counter, org_dict)
for key, amount in increments:
    after_dict[key] += amount
assert counter.added == 2       # red, orange