# Tuple
# tuple is immutable. In other words, tuple is Constant list.

# Tuple vs List
# 1.Used memory by Tuple is smaller than by List
# 2.Elements of Tuple are free from rewrite
# 3.Tuple can be used as Key of Dictionary
# 4.Named Tuple can be used as an simple alternative of the Object
# 5.Argument of Function is given as Tuple

empty_tuple = ()

one_artists = "Renoir",     # ("Renoir",)
artists_tuple = "Renoir", "Vermeer", "Monet"    # ("Renoir", "Vermeer", "Monet")
artists_tuple = ("Renoir", "Vermeer", "Monet")

artists_list = ["Renoir", "Vermeer", "Monet"]
tuple(artists_list)

# unpack
a, b, c = one_artists   # a = "Renoir", b = "Vermeer", c = "Monet"


# Named Tuple
# namedtuple(name, field[separated by " "])
# - immutable
# - spatially and temporally effective than object
# - can access like namedtuple.field, not tuple[index]
# - can be used as key of dictionary

from collections import namedtuple
Philosopher = namedtuple("Philosopher", "name country")
philosopher1 = Philosopher("Spinoza", "Netherlands")     # Philosopher("Spinoza", "Netherlands")
philosopher1.name        # Spinoza
philosopher1.country     # Netherlands

properties = {"name": "Spinoza", "country": "Netherlands"}
philosopher1 = Philosopher(**properties)

