"""
Input: words = ["apple", "banana", "cherry"]
Output:
1 apple
2 banana
3 cherry
"""

words = ["apple", "banana", "cherry"]
def add_index(li):
    for index, item in enumerate(li, 1):
        print(f"{index} {item}")

add_index(words)


"""
Input: words = ["a", "b", "c"]
Output: {0: "a", 1: "b", 2: "c"}
"""
words = ["a", "b", "c"]
def transform(li):
    return {index: value for index, value in enumerate(li)}

print(transform(words))


"""
Input: nums = [10, 20, 30]
Output: [(0, 10), (1, 20), (2, 30)]
"""
nums = [10, 20, 30]
print(list(enumerate(nums)))

"""
names = ["a", "b", "c"]
marks = [90, 80, 70]

output: {"a": 90, "b": 80, "c": 70}
"""
names = ["a", "b", "c"]
marks = [90, 80, 70]
print(dict(zip(names, marks)))


"""
a = [1, 2, 3]
b = [4, 5, 6]

output: [5, 7, 9]
NOTE: element-wise sum
"""
a = [1, 2, 3]
b = [4, 5, 6]
print([a + b for a, b in zip(a, b)])


"""
type: zip
names = ["a", "b", "c"]
marks = [90, 80]
NOTE: Write code to handle safely
"""
names = ["a", "b", "c"]
marks = [90, 80]
def zip_itrs(names, marks):
    if len(names) != len(marks):
        return "List size mismatch"
    return list(zip(names, marks))

print(zip_itrs(names, marks))


"""
sort descending:
nums = [5, 2, 9, 1]
"""
nums = [5, 2, 9, 1]
print(sorted(nums, reverse=True))


"""
sort by length:
words = ["apple", "kiwi", "banana"]
"""
words = ["apple", "kiwi", "banana"]
print(sorted(words, key=len))


"""
sort by marks (ascending)
students = [
    ("a", 90),
    ("b", 70),
    ("c", 80)
]
"""
students = [
    ("a", 90),
    ("b", 70),
    ("c", 80)
]
sort_key_fn = lambda e: e[1]
print(sorted(students, key=sort_key_fn))


"""
use zip + sorted
sort by marks descending

names = ["a", "b", "c"]
marks = [90, 70, 80]

output:
a 90
c 80
b 70
"""
names = ["a", "b", "c"]
marks = [90, 70, 80]
def print_output(li1, li2):
    for x, y in sorted(zip(li1, li2), key=sort_key_fn, reverse=True):
        print(f"{x} {y}")

print_output(names, marks)


"""
sort by marks descending
use zip + sorted

names = ["a", "b", "c"]
marks = [90, 70, 80]
ages = [20, 18, 22]

output:
a 90 20
c 80 22
b 70 18
"""
names = ["a", "b", "c"]
marks = [90, 70, 80]
ages = [20, 18, 22]

def transform_3(li1, li2, li3):
    for x, y, z in sorted(zip(li1, li2, li3), reverse=True, key=lambda x: x[1]):
        print(f"{x} {y} {z}")

transform_3(names, marks, ages)