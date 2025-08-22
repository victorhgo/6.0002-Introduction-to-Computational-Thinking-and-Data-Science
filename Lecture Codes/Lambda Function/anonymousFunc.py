def func(n):
    """ Assumes n is a real,
        Returns n * a """
    return lambda a: a * n

# This will always double the number
doubler = func(2) 

# This will always triple the number
triple = func(3)

print(f"Double: {doubler(3)}")
print(f"Triple: {triple(3)}")