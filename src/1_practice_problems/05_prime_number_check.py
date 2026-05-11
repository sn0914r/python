# Check whether a given number is prime or not.

def is_prime(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False

    return True

print(is_prime(10))
print(is_prime(5))
print(is_prime(100))