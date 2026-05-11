# Check whether a given number reads the same forwards and backwards.

# 1. Using numbers only
def is_palindrome_1(num):
    reversed_num = 0
    n = num

    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n = n // 10

    return reversed_num == num

print(is_palindrome_1(1234))
print(is_palindrome_1(1221))

# 2. Using strings
def is_palindrome_2(num):
    return str(num) == str(num)[::-1]

print(is_palindrome_2(1234))
print(is_palindrome_2(1221))