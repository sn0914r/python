"""
Sets:
    - Unordered
    - No duplicates
    - Fast lookup
"""

s = {1, 2, 4, 5}

# add()
s.add(100)

# remove() - if target value didn't exist, ERROR will be thrown
s.remove(5)

# discard() - if target value didn't exist, NO ERROR will be thrown
s.discard(50)

# pop() - removes random element
s.pop()

# clear()
s.clear()

# COMBINING SETS
a = {1, 2}
b = {2, 4}

# union() or |
print(a.union(b))
print(a | b)

# update - union + mutates the original set
print(a.update(b))

# intersection or &
print(a.intersection(b))
print(a & b)

# - difference (elements in a not in b)
print(a - b)