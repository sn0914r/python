# Reverse the digits of a given integer.

# 1. using numbers only
def reverse_number_1(num):
    reversed_num = 0
    n = num

    while n > 0:
        digit = n % 10
        reversed_num = (10 * reversed_num) + digit
        n = n // 10
    
    return reversed_num

print(reverse_number_1(1234))


# 2. using strings
def reverse_number_2(num):
    return int(str(num)[::-1])

print(reverse_number_2(1234))
