"""
Tuples:
    - Faster than lists
    - immutable
    - ordered
    - used in returns
"""

# tuple packing
t = 1, 2, 3
# Python automatically packs into tuple
print(t)

# unpacking
a, b, c = (1, 2, 3)
print(a)  # 1
print(b)  # 2
print(c)  # 3
# NOTE: Must match length otherwise it throws an error

# Star unpacking
a, *b = (1, 2, 3, 4) # a takes the first elem, rest of the elements are stored as list in b
print(a)
print(b)

# Returning multiple values
def get_user():
    return "Siva", "csm"

print(get_user())
name, age = get_user()
print(name)
print(age)

# Loop with unpacking
pairs = [(1, 2), (3, 4)]

for a, b in pairs:
    print(a, b)