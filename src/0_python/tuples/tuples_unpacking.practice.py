# unpack into a, b, c
t = (10, 20, 30)
a, b, c = t
print(a, b, c)

# get the first element
nums = (1, 2, 3, 4, 5)
a, *b = nums
print(a)

# Swap
a = 5
b = 10

a, b = b, a
print("a:", a)
print("b:", b)

# get first, middle, last
data = (1, 2, 3, 4)
first, *middle, last = data
print(first)
print(middle)
print(last)

# print sum of each pair
pairs = [(1, 2), (3, 4), (5, 6)]

for a, b in pairs:
    print(a+b)

# get first and last elements and ignore middle values using _
t = (10, 20, 30, 40)
first, *_, last = t
print(first)
print(last) 

# Nested unpacking
data = (1, (2, 3), 4)
"""
output:
a = 1
b = 2
c = 3
d = 4
"""
a, (b, c), d = data
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

# Swap first and last using unpacking
nums = [1, 2, 3, 4, 5]
# [5, 2, 3, 4, 1]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

# Function returning multiple values - sum & max and unpack it
nums = [1, 2, 3, 4, 5]
def sum_max(nums):
    return sum(nums), max(nums)
sum_nums, max_num = sum_max(nums)
print("sum:", sum_nums)
print("max:", max_num)

# Get first, last and only evens from middle
data = (1, 2, 3, 4, 5, 6)
"""
output:
first = 1
last = 6
middle_even = [2, 4]
"""
def transform(nums):
    first, *middle, last = nums
    middle_even = [x for x in middle if x%2==0]
    return first, last, middle_even

first, last, middle_even = transform(data)
print("first:", first)
print("last:", last)
print("middle_even:", middle_even)