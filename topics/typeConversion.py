"""
TYPE CONVERSION : 
1. type conversion is the process of converting a data type into another data type.
    Types in TYPE CONVERSION :
    -> Implicit type conversion: python automatically converts the data (from smaller data like int to larger data like float)
    -> Explicit type conversion or TYPE CASTING : user manually converts the data using the casting operators.
2. Casting Opeartors in Python:
    -> int(value) - converts the data into integers, not applicable for non-numeric strings.
    -> float(value) - converts the data into integers, not applicable for non-numeric strings.
    -> string(value) - converts the data into strings
    -> list(value) - converts sequences into list, not applicable to primitive data types expcept strings (becoz strings are SEQUENCE of chars)
    -> tuple(value) - converts sequences into tuples
    -> set(value) - converts to sets
"""

print(type(int("10"))) # numeric string is convered to int type, output : <class 'int'>
print(type(float(30))) # int is converted to float, output : <class 'float'>
print(type(str(100))) # int is converted to string, output : <class 'str'>
print(type(list( (10, 20 ,30) ))) # tuple is converted to list, output : <class 'list'>
print(type(tuple( [10, 20, 30] ))) # list is converted to tuple, output : <class 'tuple'>
print(type(set( [10,20,30,40] ))) # list is converted to set, output : <class 'set'>