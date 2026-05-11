# Reverse a given string.

# 1. using slicing
def reverse_string_1(string):
    return string[::-1]

print(reverse_string_1("siva"))


# 2. using built-in method
def reverse_string_2(string):
    return "".join(reversed(string))

print(reverse_string_2("siva"))


# 3. using loop
def reverse_string_3(string):
    reversed_str = ""

    for ch in string:
        reversed_str = ch + reversed_str
    
    return reversed_str

print(reverse_string_3("siva"))