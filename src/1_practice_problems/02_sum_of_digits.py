# Given a number, find the sum of all its digits

# 1. directly with the numbers
def sum_of_digits_1(num):
    total = 0
    n = num

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total

print(sum_of_digits_1(1234))

# 2. using strings
def sum_of_digits_2(num):
    str_num = str(num)
    total = 0

    for ch_num in str_num:
        total += int(ch_num)
    
    return total

print(sum_of_digits_2(1234))