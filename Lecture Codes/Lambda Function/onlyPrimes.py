""" Use filter() with a lambda to keep only prime numbers from a list.
    Syntax: filter(function, list)

    Fastest way to check if n is prime:
    Test that no number from 2 to sqrt(n) divides n

    -> Implementation: for all: all() : The all() function returns True if all items in an iterable are true, otherwise it returns False.
                                        If the iterable object is empty, the all() function also returns True.

    > all(n % i != 0 for i in range(2, int(n**0.5) + 1)) where:

    Check if n divided for all numbers in range(2, sqrt(n) + 1) is different than zero
    Note: We transform the square root of n to int + 1 to make it easier to use

    So the final algorithm will look like:

    if n > 1 and n is false true for every numbers in the range, n is prime

 """

# Test some instances
"""n = 2
print(all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 4
print(all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 5
print(all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 7
print(all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
n = 10
print(all(n % i != 0 for i in range(2, int(n**0.5) + 1)))"""

set1 = list(range(1,20))

primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), set1))

print(f"Primes: {primes}")

