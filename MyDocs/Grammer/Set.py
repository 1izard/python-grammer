# Set

empty_set = set()
even_number = {1, 3, 5, 7}
set(List)
set(Tuple)
set(Dict)   # { kye1, key2, ... }

# in
drinks = {
    "martini": {"vodka", "vermouth"},
    "black russian": {"vodka", "kahlua"},
    "White russian": {"cream", "kahlua", "vodka"},
    "manhattan": {"rye", "vermouth", "bitters"},
    "screwdriver": {"orange juice", "vodka"}
}
for name, contents in drinks.items():
    if contents & {"vermouth", "orange juice"}:     # = contents.intersection({"vermouth", "orange juice"})
        print(name)     # martini, manhattan, screwdriver

drinks["black ruissian"] | drinks["white russian"]
drinks["black ruissian"].union(drinks["White russian"])     # {"cream", "kahlua", "vodka"}

drinks["black ruissian"] - drinks["white ruissan"]
drinks["black ruissian"].difference(drinks["white russian"])    # {"cream"}

# exclusive OR
drinks["black russian"] ^ drinks["white russian"]
drinks["black russian"].symmetric_difference(drinks["white russian"])   # {"cream"}

# subset
drinks["black russian"] <= drinks["white russian"]
drinks["black russian"].issubset(drinks["white russian"])   # True

# proper subset
drinks["black russian"] < drinks["white russian"]   # True
