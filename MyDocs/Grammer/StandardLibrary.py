# module

import sys
for place in sys.path:
    print(place)


# collections
# Counter
from collections import Counter
breakfast = ["spam", "spam", "eggs", "spam"]
breakfast_counter = Counter(breakfast)
breakfast_counter   # Counter({"spam": 3, "eggs": 1})
breakfast_counter.most_common()     # [("spam", 3), ("eggs", 1)]
breakfast_counter.most_common(1)    # [("spam", 3)]

lunch = ["eggs", "eggs", "bacon"]
lunch_counter = Counter(lunch)      # Counter({"eggs": 2, "bacon": 1})
breakfast_counter + lunch_counter   # Counter({"spam": 3, "eggs": 3, "bacon": 1})
breakfast_counter - lunch_counter   # Counter({"spam": 3})
lunch_counter - breakfast_counter   # Counter({"eggs": 1, "bacon": 1})
breakfast_counter & lunch_counter   # Counter({"eggs": 1})
breakfast_counter | lunch_counter   # Counter({"spam": 3, "eggs": 2, "bacon": 1})   Not equal to +


# itertools
# chain
import itertools
for item in itertools.chain([1, 2], ["a", "b"]):
    print(item)     # 1 2 a b
# cycle
for item in itertools.cycle([1, 2]):
    print(item)     # 1, 2, 1, 2, ...
# accumulate
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)     # 1, 3, 6, 10
def multiply(a, b):
    return a * b
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)     # 1, 2, 6, 24


# pprint
from pprint import pprint
musicians = {"Debussy": "France", "Rachmaninov": "Russia", "Chopin": "Poland"}
pprint(musicians)
