"""
LOOPS
1. Loops are used to run a block of code multiple times.
2. It runs until a specific condition returns false.
3. If the condition is always true then it forms "INFINITE LOOP"

TYPES OF LOOPS:
1. for loop : generally used when we know the numberof iterations and in python it's used to iterate over sequences like list, tuple, range, sets, dictionaries, and strings.
2. while loop : used when we don't know the numberof iterations
"""

#for loop
"""
syntax: 
for i in sequence:
    #code
"""
#example
for i in [10,20,30]:
    print(i, end=" ")
print("",end="\n") #output : 10 20 30
#while loop
"""
syntax:
while condition:
    #code
"""
#example
i = 1
while i<=3:
    print(i, end=" ")
    i=i+1
#output : 1 2 3


# break and continue
"""
the break statement is used to conditionally terminate the ongoing loop.

the continue statement is used to conditionally skip the current iteration and moves to the next iteration
"""

for i in (10, 20, 30, 40, 50):
	if i == 30:
		continue #skips at 30
	if i == 50:
		break # terminates at 50
	print(i, end=" ")

#output : 10 20 40