"""
Functions
"""

# Default arguments
def greet(name="user"):
    print(f"Hello {name}")
greet()
greet("Siva")

# *args (multiple positional inputs)
# NOTE: args is a TUPLE
def print_total(*args):
    print("Sum:", sum(args))
print_total(2, 4, 5, 7, 8)
print_total(3, 4, 5)

# **kwargs (multiple named inputs)
def print_user_details(**kwargs):
    print(kwargs)
print_user_details(name="Sivananda", branch="CSM")

# NOTE: Order must be: positional → *args → **kwargs
def order(a, b, *args, **kwargs):
    pass