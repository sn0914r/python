# remove the duplicates
# output: {1, 2, 3, 4, 5}
nums = [1, 2, 2, 3, 4, 4, 5]
no_dups = set(nums)
print(no_dups)

# get common elements
a = {1, 2, 3}
b = {2, 3, 4}
# output: {2, 3}
print(a & b)

# elements only in a
# output: {1}
print(a - b)

# elements only in b
# output: {4}
print(b - a)

# all unique elements  (combine both)
# output: {1, 2, 3, 4}
print(a | b)

# Remove common elements
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# output: {1, 2, 5, 6}
no_common_elems = (a | b) - (a & b)
print(no_common_elems)

# check the subset
a = {1, 2}
b = {1, 2, 3, 4}
# output: True
print(True if a & b == a else False)

# Unique characters in string
s = "programming"
# output: {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}
unique_chars = set(list(s))
print(unique_chars)

# case-insensitive unique words
words = ["Apple", "banana", "APPLE", "Banana"]
# output: {"apple", "banana"}
print(set([word.lower() for word in words]))
