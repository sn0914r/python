"""
enumerate: enumerate is used to get both index and value while looping
"""
fruits = ["apple", "banana", "carrot"]

def no_enum(li):
    index = 0
    for item in li:
        print(f"{index} - {item}")
        index += 1

def enum(li):
    for index, item in enumerate(li):
        print(f"{index} - {item}")

print("Without enumerate")
no_enum(fruits)
print("With enumerate")
enum(fruits)

"""
zip: 
1. It combines elements at the same index (pairs items by position)
2. If iterable sizes are not same then it stops at shortest iterable (throws NO ERROR)
"""

itr1 = ["a", "b", "c"]
itr2 = [1, 2]
itr3 = ["A", "B", "C"]
print(list(zip(itr1, itr2, itr3)))
print(list(zip(itr1, itr3)))

"""
sorted([]):
1. [].sort() => mutates, sorted([]) => returns new list
2. reverse sorting: sorted(nums, reverse=True)

sorted([], key=)
the key function must return values that Python can compare (<, >)
safest values that key= fn can return
"""