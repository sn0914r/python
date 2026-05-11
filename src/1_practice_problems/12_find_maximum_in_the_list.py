# Find the largest number in a list without using the built-in `max()` function

def maximum (li):
    max_num = li[0]

    for i in li:
        if i > max_num:
            max_num = i
    
    return max_num

print(maximum([2, 5, 78, 9]))

def maximum_2(li):
    return max(li)

print(maximum_2([2, 5, 78, 9]))