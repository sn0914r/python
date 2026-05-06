nums = [1, 2, 3, 4, 5, 6]
words = ["apple", "banana", "cherry"]
matrix_1 = [
    [1, 2], 
    [3, 4], 
    [5, 6]
    ]
matrix_2 = [
    [1, 2, 3], 
    [4, 5, 6]
    ]

"""
Create a new list with each number doubled
OUTPUT: [2, 4, 6, 8, 10, 12]
"""
doubled_nums = [x * 2 for x in nums]
print(doubled_nums)

"""
Get only even numbers
OUTPUT: [2, 4, 6]
"""
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums)

"""
square only odd numbers
OUTPUT: [1, 9, 25]
"""
squared_odd_nums = [x**2 for x in nums if x % 2 != 0]
print(squared_odd_nums)

"""
create a list of lengths of each word
OUTPUT: [5, 6, 6]
"""
lengths_of_words = [len(x) for x in words]
print(lengths_of_words)

""" 
Create a new matrix where each value is +10 for matrix_1
OUTPUT: 
[
    [11, 12],
    [13, 14],
    [15, 16]
]
"""
matrix_plus_10 = [[x + 10 for x in r] for r in matrix_1]
print(matrix_plus_10)

"""
Flatten matrix_2 it into a single list
OUTPUT: [1, 2, 3, 4, 5, 6]
"""
flat_list = [x for r in matrix_2 for x in r]
print(flat_list)

"""
replace the nums with even/odd strings for nums list
OUTPUT: ["odd", "even", "odd", "even", "odd", "even"]
"""
even_or_odd = ["even" if x % 2 == 0 else "odd" for x in nums]
print(even_or_odd)

"""
replace the nums with even/odd strings for matrix_2
OUTPUT:
[
    ["odd", "even", "odd"],
    ["even", "odd", "even"]
]
"""
even_or_odd_matrix = [["even" if x % 2 == 0 else "odd" for x in r] for r in matrix_2]
print(even_or_odd_matrix)

""" 
Transform the matrix_2:
    - multiply by 2
    - flatten result
    - only ONE list comprehension
OUTPUT: [2, 4, 6, 8, 10, 12]
"""
multiply_by_2_plus_flat_list = [x*2 for r in matrix_2 for x in r]
print(multiply_by_2_plus_flat_list)