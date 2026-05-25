# Iterator

1. An iterator is an object that lets us go through items one by one. It keeps track of the current position and gives the next value when needed using `next()`.

```py
nums = [10, 20, 30]

it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

- `iter()` → creates an iterator
- `next()` → gets the next value
- When all values are finished, Python raises `StopIteration`

---

# Generators

1. A generator is an easy way to create iterators using the `yield` keyword. It produces values one at a time instead of storing everything in memory.

```py
def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
```

---

# Key Difference

- Iterators are objects used to iterate over data.
- Generators are a simple way to create iterators using `yield`.

Generators are memory efficient because they generate values lazily, only when needed.

```py
def huge_numbers():
    for i in range(1_000_000):
        yield i
```

This does not store all one million numbers in memory at once.