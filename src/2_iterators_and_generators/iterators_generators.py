# Iterators

nums = [10, 20, 30]

it = iter(nums)

# print(next(it))  # 10
# print(next(it))  # 20
# print(next(it)) # 30


def count():
    print("i print on first yield")
    yield 1
    print("i print on second yield")
    yield 2
    print("i print on third yield")
    yield 3


g = count()
print(next(g))
print(next(g))
print(next(g))


def gene():
    print("Hello")
    yield 100

f = gene()

try:
    print(next(f))
    print(next(f))
except StopIteration:
    print("StopIteration Error")
