# Python program to interchange first and last elements in a list

"""
1. Using Temporary Value
2. Using tuple variable
3. Using * operand
4. Using Slicing
"""

list = [10,2,532,64]
#temporary value
def tempValue(list):
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    return
tempValue(list)
print(list) # output : [64, 2, 532, 10]

# using tuple variable
def tupleMethod(list):
    # tuple destructuring
    fl = list[0], list[-1]
    list[-1], list[0] = fl
    return
tupleMethod(list)
print(list) # output : [10, 2, 532, 64]

# Using * operand
def catchAllMethod(list):
    # the '*' before a variable is used for collecting and unpacking multiple elements in the iterables

    # Note : when you reassign the variable inside the function, the connection to the original list is broken
    # so it doesn't modify the original list
    a, *b, c = list
    list = [c, *b, a]
    return list
print(catchAllMethod(list)) # output : [64, 2, 532, 10]