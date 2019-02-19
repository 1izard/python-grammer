# List
# List is mutable
empty_list = []
philosophers = ["Spinoza", "Descartes", "Kant"]

# transform
a_tuple = ("ready", "fire", "aim")
a_list = list(a_tuple)

# extract
philosophers[-1]     # Kant
philosophers[5]      # IndexError

philosophers[2] = "Heidegger"

# slice
philosophers[0:2]    # ["Spinoza", "Descartes"]
philosophers[::-1]   # ["Kant", "Descartes", "Spinoza]

# append()
philosophers.append("Heidegger")

# extend()
others = ["Socrates", "Plato"]
philosophers.extend(others)      # ["Spinoza", "Descartes", "Kant", "Socrates", "Plato"]
philosophers.append(others)      # ["Spinoza", "Descartes", "Kant", ["Socrates", "Plato"]]

# insert()
philosophers.insert(2, "Socrates")   # ["Spinoza", "Descartes", "Socrates", "Kant"]

# del
# "del" is a statement of python, not a method.
# the function mean the reverse of "=".
# "del" separates the "del"ed name from python object
# and if the object is last reference, it release the memory resource.
del philosophers[-1]     # ["Spinoza", "Descartes", "Socrates"]

# remove()
philosophers.remove("Socrates")      # ["Spinoza", "Descartes"]

# pop()
philosophers = ["Spinoza", "Descartes", "Kant", "Socrates", "Plato"]
philosopher1 = philosophers.pop()   # philosopher1 = "Plato", philosophers = ["Spinoza", "Descartes", "Kant",
# "Socrates"]
philosopher2 = philosophers.pop(2)  # philosopher2 = "Kant", philosophers = ["Spinoza", "Descartes", "Socrates"]

# index()
philosophers = ["Spinoza", "Descartes", "Kant", "Socrates", "Plato"]
philosophers.index("Spinoza")       # 0
philosophers.index("Heidegger")     # ValueError

# in
"Spinoza" in philosophers       # True

# count()
philosophers.count("Kant")     # 1

# join() & split()
philosophers_str = ", ".join(philosophers)     # philosophers_s = "Spinoza", "Descartes", "Kant", "Socrates", "Plato"
philosopher_list = philosophers_str.split(",") # philospher_list = ["Spinoza", "Descartes", "Kant", "Socrates", "Plato"]

# sort() & sorted
philosophers = ["Spinoza", "Descartes", "Kant"]
sorted_philosophers = sorted(philosophers)
# sorted_philosophers = ["Descartes", "Kant", "Spinoza"]
# philosophers = ["Spinoza", "Descartes", "Kant"]
philosophers.sort()     # philosophers = ["Descartes", "Kant", "Spinoza"]
philosophers.sort(reverse=True)     # philosophers = ["Spinoza", "Kant", "Descartes"]

# len()
len(philosophers)       # 3

# copy()
# b, c, d are independent on list a
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

