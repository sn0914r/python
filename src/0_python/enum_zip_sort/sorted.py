"""
Python sorted() — Clean Notes

1. Basic
- sorted(iterable) → returns a NEW sorted list
- does NOT modify original data

2. sort() vs sorted()
- list.sort() → modifies the original list (in-place)
- sorted() → returns a new list

3. Reverse sorting
- sorted(iterable, reverse=True)

4. key parameter (MOST IMPORTANT)
- key is a function applied to each element
- sorting is done based on the returned value
- original elements are returned (NOT the key values)

Example:
    sorted(words, key=len)

5. What can key return?
- The key function must return values that Python can compare (<, >)

Safe return types:
- numbers (int, float)
- strings
- tuples (for multi-level sorting)
- booleans (False < True)

6. Important behavior
- key values are used ONLY for comparison
- they are NOT part of the final output

7. Best practice
- use key for custom sorting
- use tuple for multi-condition sorting

Example:
    key=lambda x: (x["price"], x["name"])

8. Common mistakes
- mixing incomparable types → ERROR
- assuming key values are returned → WRONG
- confusing sort() vs sorted() → WRONG

One-line memory:
sorted = order elements using key(element)
"""

fruits = ["orange", "apple", "kiwi", "banana"]
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))