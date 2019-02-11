# if, elif, else

x = 7
if 0 <= x <= 10:
    print("x is between 0 and 10")
elif 10 < x:
    print("x is greater than 10")
else:
    print("x is smaller than 0")

if x in {1, 3, 5, 7}:
    print("Found x")
else:
    print("Not found x.")

# False
# null, 0, 0.0, "", [], (), {}, set()


# while
while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    else:
        print(number, "squared is", number*number)

# else  as break checker
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    if numbers[position] % 2 == 0:
        print("Found even number", numbers[position])
        break
    position += 1
else:   # if break is not called = elements do not match While condition.
    print("No even number found")

cheeses = []
for cheese in cheeses:
    print("This shop has some lovely", cheese)
    break
else:   # if break is not called = elements do not match For condition.
    print("This is not much of a cheese shop, is it?")


# zip()
# zip() stop when it completed processing the smallest sequence.
days = ["Monday", "Tuesday", "Wednesday"]
fruits = ["banana", "orange", "peach"]
drinks = ["coffee", "tea", "beer"]
desserts = ["tiramisu", "ice cream", "pie", "pudding"]
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
# "pudding" in desserts is not processed.

english = ("Monday", "Tuesday", "Wednesday")
french = ("Lundi", "Mardi", "Mercredi")
ef_list = list(zip(english, french))    # [("Monday", "Lundi"), ("Tuesday", "Mardi"), ("Wednesday", "Mercredi")]
ef_dict = dict(zip(english, french))    # {"Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi"}


# range(start, end, step)
# range() is one of Generator
for x in range(0, 3):
    print(x)    # 0, 1, 2

for x in range(2, -1, -1):
    print(x)    # 2, 1, 0


# Comprehension
# List Comprehension
number_list = [number for number in range(1, 6)]    # [1, 2, 3, 4, 5]
number_list = [number-1 for number in range(1, 6)]  # [0, 1, 2, 3, 4]
number_list = [number for number in range(1, 6) if number % 2 == 1]     # [1, 3, 5]

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]    # [(1, 1), (1, 2), (2, 1), (2. 2), (3, 1), (3, 2)]

# Dictionary Comprehension

# Set Comprehension
a_set = {number for number in range(1, 6) if number % 3 == 1}   # {1, 4}

# Generator Comprehension
# Generator can be executed just once
# because Generator generates values and immediately gives Iterator them, not using memory.
number_thing = (number for number in range(1, 6))   # <class 'generator'> (1, 2, 3, 4, 5)
number_list = list(number_thing)    # [1, 2, 3, 4, 5]
try_again = list(number_thing)  # []


# enumerate(iterator[, start])
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list, 1):
    print('{}: {}'.format(i, flavor))   # 1: vanilla  2: chocolate  ...