# Question

# Why does this function with default value work without argument "result",
# and store previous "result" at the second call?
def a_func(arg, result=[]):
    result.append(arg)
a_func("a")     # ["a"]
a_func("b")     # ["a","b"]
