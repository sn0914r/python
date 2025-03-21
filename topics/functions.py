# Functions
"""
1. The Functions are used to create reusable blocks of code.
2. In python we can create functions using 'def' key word.
3. The functions are much useful when we want to create reusable and more readable codes.
4. The 'return' keyword is used to return a value or result from a function.
"""
#example 
def add(a,b):
	return a+b #returns the sum
print(add(2,5)) #7


"""
1. The functions can accept the external values inside the paranthesis.
2. The variables that are passed when defining the function are called parameters.
3. The axtual values that are passee when calling the funtions are called arguments.
"""
#example
def multiply(a,b): #a,b are parameters.
	return a*b
c = multiply(5,7) #5, 7 are arguments
print(c)
# the parameters can be said as the placeholders for arguments.

#default parameters
"""
1. Functions can have default values for each parameter, if we dont pass any arguments then python takes that default values as arguments.
2. But the rule is non- default parameter cannot follow the deafult parameter, if it does then we will get an error (non-default argument error).
"""
def sum(a,b=0): #b is default parameter
	return a+b
print(sum(2)) # 2

# taking unknown number of arguments.
"""
1. we use "*args"" and "*kwargs" to take unknown number of arguments.
2. "*args" is used when we want non key-value pair argumnets. it returns all the values in a  tuple.
3. "**kwargs" is uswd when we want to take key-value pair type argumnets. It returns all the key-values in dictionary.
"""
#example
def argsEg(*nums):
	print(nums)
argsEg(10, 20, 30)

def kwargsEg(**pairs):
	print(pairs)
kwargsEg(name="bhAAi", age=40, gender="male")

#lambda functions
"""
1. The lambda functions are the single lined short functions, useful when creating small functions.
2. They are anonymous functions ie. they dont have any name and must must store them in a variable.
3. we use 'lamda' keyword to define a lambda function.
4. SYNTAX:
	lambda arguments:Expressions
	
	these function returns the expressions.
"""
#example
square = lambda a:a*2
print(square(2)) #output: 4