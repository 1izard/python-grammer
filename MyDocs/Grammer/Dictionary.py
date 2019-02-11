# Dictionary

empty_dictionary = {}

musicians = {
    "Debussy": "France",
    "Rachmaninov": "Russia",
    "Chopin": "Poland",
}

musicians_list = [["Debussy", "France"], ["Rachmaninov", "Russia"], ["Chopin", "Poland"]]
dict(musicians_list)

# addition
musicians["Bach"] = "Germany"
# musicians = {
#     "Debussy": "France",
#     "Rachmaninov": "Russia",
#     "Chopin": "Poland",
#     "Bach": "Germany",
# }

# update()
others = {
    "Tchaicovsky": "Russia",
    "Ravel": "France",
}
musicians.update(others)

# del
del musicians["Tchaicovsky"]

# clear()
musicians.clear()

# in
"Debussy" in musicians  # True

# [key] & get()
musicians["Debussy"]    # True
musicians["Beethoven"]  # KeyError

musicians.get("Beethoven", "Not found.")    # "Not found."
musicians.get("Beethoven")      # None

# keys() & values() & items()
musicians = {
    "Debussy": "France",
    "Rachmaninov": "Russia",
    "Chopin": "Poland",
}
list(musicians.keys())
# musicians.keys() -> dict_keys(["Debussy", "Rachmaninov", "Chopin"])
list(musicians.values())
list(musicians.items())     # [("Debussy": "France"), ("Rachmaninov": "Russia"), ("Chopin": "Poland")]


# "=" vs copy()
# Dictionary created by copy() is independent on the original dictionary


# setdefault(Key, Value)
musicians = {"Debussy": "France", "Rachmaninov": "Russia", "Chopin": "Poland"}
beethoven = musicians.setdefault("Beethoven", "Germany")
# if "Beethoven" not found, set "Beethoven": "Germany" into Dictionary "musicians" and return Key "Germany"
print(beethoven)    # "Germany"
print(musicians)    # {"Debussy": "France", "Rachmaninov": "Russia", "Chopin": "Poland", "Beethoven": "Germany"}



# defaultdict(Function[, dictionary])
from collections import defaultdict
def not_found():
    return "Not found"
musicians = {"Debussy": "France", "Rachmaninov": "Russia", "Chopin": "Poland"}
musicians = defaultdict(not_found)
print(musicians["Beethoven"])       # "Not found"

result_dict = defaultdict(not_found, musicians)     # safety about original dictionary

# lamda
musicians = defaultdict(lambda: "Not found")


# counter
from collections import defaultdict
food_counter = defaultdict(int)     # Dictionary "food_counter" is used as counter / int() returns 0
for food in ["spam", "spam", "egg", "spam"]:
    food_counter[food] += 1
for food, count in food_counter.items():
    print(food, count)      # spam 3    egg 1


# OrderedDict
from collections import OrderedDict
order = OrderedDict([       # OrderedDict(item)
    ("First", 1),
    ("Second", 2),
    ("Third", 3)
])

