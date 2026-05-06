# List Comprehensions - A short way to create a list from another iterable.

# Basic Form [expr for x in iterable]
list = [1, 2, 3, 4, 5]
squared = [x**2 for x in list]
print(squared)

# With Filter [expr for x in iterable if condition]
even_nums_squared = [x**2 for x in list if x%2==0]
print(even_nums_squared)

# Nested Loops [x for row in matrix for x in row]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened_list = [x**2 for r in matrix for x in r]
print(flattened_list)