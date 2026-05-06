# multiply all numbers
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 3, 4))


# print student info in key-value pairs
def student_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}") 

student_info(name="Sivananda", branch="csm")


# return sum of everything
def mix(a, b, *args):
    return a + b + sum(args)

print(mix(1, 2, 3, 4, 5))


# return only keys where value is True
def config(**kwargs):
    return [k for k, v in kwargs.items() if v]

print(config(apiUrl=True, jwt_access=True, jwt_refresh=False))

# print *args and **kwargs cleanly
def wrapper(*args, **kwargs):
    print("args: ",args)
    print("kwargs: ", kwargs)
wrapper(3, 5, 6, 8, name="Sivananda", branch="csm")