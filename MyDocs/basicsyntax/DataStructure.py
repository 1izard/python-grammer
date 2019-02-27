# Deque (Double-ended Queue)
from collections import deque

fifo = deque()
fifo.append(1)
x = fifo.popleft()
print(x)
# 1



# Default Dictionary
from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1



# Heap Queue
'''
Useful for store queue with priority.
Be careful that list.sort() doesn't work.
'''
from heapq import heappush, heappop
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
print(heappop(a), heappop(a), heappop(a), heappop(a))
# 3 4 5 7

from heapq import heappush, nsmallest
a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3
'''
nsmallest(n, iterable): return the n-th smallest element
'''



# Bisection
from bisect import bisect_left
x = list(range(10**6))
i = bisect_left(x, 991234) # O(log(n))
# which means that bisect_left(list with 10**6, 991234)
# equals to work (list with 14 elements).index(991234).
# Use instead of i = x.index(991234) : O(n)



# itertools
'''
- Usage as link: chain, cycle, tee
- Usage for sifting elements: islice, takewhile, dropwhile, fileterfalse
- Usage for combining elements: product, permutations, combination
'''
