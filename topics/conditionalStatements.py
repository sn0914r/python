"""
The conditional statements are used to execute code based on conditions

The conditional Statemnets in python are:
1. if statement
2. if-else statement
3. if-elif-else statement
4. Nested statements
"""

#if statement : elecutes only if the condition is true otherwise the block will be skipped, it only contains one block
if True:
    print("true condition will be executed") # this will execute as the condition is true

if False:
    print("false condition will be skipped", end="\n") # this will not be execute as the condition is false

# if-else statement : if the condition istrue then if block will be executed if the condtion is false then else block will be executed

if True:
    print("if blck executes and else block will be skipped")
else:
    print("else block, i dont execute")

if False:
    print("if condition is true, i don't execute")
else:
    print("if condition is false so elese block executes", end="\n")

# if-elif-else: 
"""
1. This type of conditonal statements are used when we have more than two conditions.
2. python checks this conditional statements one by one, if anyone one of them is true then its corresponding block of code will be executed and others will be skipped.
3. If all conditions fail then else block will be executed

Syntax:
if condition:
    #if block
elif condition:
    #elif block
else:
    # else block

"""

if False:
    print("this if block is skipped")
elif True:
    print("This elif block executes")
else:
    print("This else block is skipped")