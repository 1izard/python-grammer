# String
# String of python is immutable
"He said 'Hello!'"
poem = '''There was a Young Lady of Norway,
    Who casually sat in a doorway;'''

# transform
print(str(98.6))

# repetition
start = "Na " * 4 + "\n"
middle = "Hey " * 3 + "\n"
end = "Goodbye."
print(start + start + middle + end)

# extraction
letters = "abcdefg"
letters[-1]     # g
letters[26]     # IndexError

# replace
name = "Henny"
name[0] = "P"   # TypeError
name.replace('H', 'P')
"P" + name[1:]  # Penny

# slice
letters[:]      # abcdefg
letters[2:]     # defg
letters[1:2]    # b
letters[-3:]    # efg
letters[2:-2]   # cde
letters[-4:-2]  # de
letters[::2]    # aceg
letters[::-1]   # gfedcba

# len
len(letters)    # 7
empty = ""
len(empty)      # 0

# split
cvsS = "Spinoza,170,Descartes,168,Kant,180"
listS = cvsS.split(",")

# join
phrase = "Philosopher,Height,".join(listS)

# manipulation
letters.startswith("abc")   # True
letters.endWith("abc")      # False
letters.find("cde")         # 2  first "cde"
letters.find("xyz")         # -1
letters.rfind("cde")        # 2  last "cde"
letters.count("a")          # 1
letters.isalnum()           # True  letters is consist only of number or alphabet, not including symbol

setup = "a duck goes into a bar..."
setup.strip(".")        # a duck goes into a bar    remove "." from both ends
setup.capitalize()      # A duck goes into a bar...
setup.title()           # A Duck Goes Into A Bar...
setup.upper()
setup.lower()
setup.swapcase()

setup.center(30)
setup.ljust(30)
setup.rjust(30)


# stack + queue = deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True



# String Format
# Old Style
    # %s String
    # %d Base 10
    # %x Base 16
    # %o Base 8
    # %f float Base 10
    # %e float exponential form
    # %g float Base 10 or float exponential form
    # %% %

    number = 98
    float = 6.07
    string = "string beer"
    print("%d %f %s" % (number, float, string))   # 98 6.070000 string beer
    print("-10%d %-10f %-10s" % (number, float, string))
    print("%10.4d %10.4f %10.4s" % (number, float, string))   # 0098 6.0700 stri
    print("%*.*d %*.*f %*.*s" % (10, 4, number, 10, 4, float, 10, 4, string))  # 0098 6.0700 stri

# New Style
    print("{} {} {}".format(number, float, string))
    print("{2} {0} {1}".format(float, string, number))    # 98 6.07 string beer
    print("{number} {float} {string}".format(number=42, string="string beer", float=6.07))  # 98 6.07 string beer
    d = {"number": 98, "float": 6.07, "string": "string beer"}
    print("{0[number]} {0[float]} {0[string]} {1}".format(d, "other"))    # 98 6.07 string beer other

    print("{2:d} {0:f} {1:s}".format(float, string, number))    # 98 6.0700 string beer
    print("{number:d} {float:f} {string:s}".format(float, string, number))
    print("{2:10d} {0:10f} {1:10s}".format(float, string, number))
    print("{2:<10d} {0:<10f} {1:<10s}".format(float, string, number))     # sort at left end
    print("{2:^10d} {0:^10f} {1:^10s}".format(float, string, number))     # sort at center
    print("{2:>10d} {0:>10.4f} {1:>10.4s}".format(float, string, number))
    print("{2:>10.4d} {0:>10.4f} {1:>10.4s}".format(float, string, number))
    # ValueError: Precision not allowed in integer format specifier

    print("{float:0>8.4}".format(float))    # 006.0700




# Regular Expression
# match()
import re
source = "Python Python Python"
m = re.match("Py", source)
if m:
    print(m.group())
else:
    print("False")
# Py

m = re.match("py", source)
if m:
    print(m.group())
else:
    print("False")
# False

m = re.match(".*thon", source)
if m:
    print(m.group())
else:
    print("False")
# Python Python Python

m = re.match(".*thon ", source)
if m:
    print(m.group())
else:
    print("False")
# Python Python

m = re.match(" .*thon", source)
if m:
    print(m.group())
else:
    print("False")
# False


# search()
m = re.search(" Python")
if m:
    print(m.group())
else:
    print("False")
# " Python"


# findall()
m = re.findall("Py", source)    # ["Py", "Py", "Py"]


# split()
m = re.split(" ", source)   # ["Python", "Python", "Python"]


# sub()
# return string not list
# cf. string.replace()
m = re.sub("Python", "Ruby", source)    # Ruby Ruby Ruby


# Meta-Character
# expr1 | expr2
# .
# ^                 front of source string
# $                 end of source string
# prev ?            having prev of 0 or 1
# prev *            having prev of 0 or more
# prev *?
# prev +            having prev of 1 or more
# prev +?
# prev {m}          prev of number of m
# prev {m, n}       prev of number of range between m and n
# prev {m, n}?
# [abc]             a|b|c
# [^abc]            not(a|b|c)
# prev (?=next)     match prev followed next
# prev (?!next)     match prev not followed next
# (?<=prev) next    match next following prev
# (?<!prev) next    match next not following prev