# Find the second largest number in a list.

sample_list = [2, 8, 6, 9, 12]

# 1. using loop
def second_largest_num(li):
    max_num = li[0]
    second_max_num = 0

    for i in li:
        if i > max_num:
            second_max_num = max_num
            max_num = i
    
    return second_max_num

print(second_largest_num(sample_list))


# 2. using sort
def second_largest_num_2(li):
    return sorted(li, reverse = True)[1]

print(second_largest_num_2(sample_list))
