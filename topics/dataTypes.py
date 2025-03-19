# In python datatypes are classified into two types:
"""
Primitive Data types : Data types that store a single value.
1. Numeric types : int(x = 10), float(y = 10.5), complex(z = 3 + 4j)
2. Boolean type : true/ false
3. character/ string type : "hello", "a", etc
"""

"""
Non-Primitive Data types: Data types that stores multiple values or collections of data.
-> Sequence Types :
    1. list -> nums=[1, 2, 3]
    2. tuple -> nums=(1, 2, 3)
    3. range -> r = range(10) {returns 10 numbers from 0}
-> Set Types : 
    1. set -> s={1, 2, 3}
    2. fronzenset -> fs = frozenset([4, 5, 6])
-> Mapping type :
    1. dict -> person = {"name": "Ram", "age": 25}
"""

"""
useful methods: 

type() Operator : It is used to check the type of variable:
ex: print(type(10)) # <class 'int'>
"""

#code

#primitive data types:

# numeric data types
print(type(10))
print(type(10.5))
print(type(2+3j))

#boolean
print(type(True))

#strings
print(type("bhaai"))

#Non-primitve data types

# sequence types
print(type([10,20,30,40,50]))
print(type((10,20,30,40,50)))
print(type(range(10)))

#set type
print(type({10, 20, 30, 40, 50}))
print(type(frozenset([10, 20, 30, 40, 50])))

#mapping type
print(type({"name": "bhaai", "age": 20}))