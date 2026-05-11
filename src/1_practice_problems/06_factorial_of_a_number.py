# Calculate the factorial of a given non-negative integer.

def factorial(num):
    if num < 1 :
        print("Invalid number")
        return
    
    fact = 1
    for i in range(1, num+1):
        fact *= i
    
    return fact

print(factorial(5))