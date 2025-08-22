""" Use reduce() with a lambda to compute the greatest common divisor (GCD) of a list of numbers. 

    reduce() - From functools. The reduce() function in Python applies a given function cumulatively to all items in an iterable, 
    reducing it to a single final value.

    Syntax : reduce(function, iterable[,init])
    Notes: function must take two values and returns one
           iterable is the sequence to be reduced
           init is optional, starting value that is placed before first element.

    Notes:

    - Euclidean Algorithm recall:
    a and b are both integers. If b == 0, then gcd(a,b) = a (base case)
    gcd(a,b) == gcd(b, a % b) (recursive call?)

    A non recursive way of implementing the Euclidean algorithm:

    def gcd(a, b):
        '''' Assumes a and b are integers
            Return the greatest common divisor of a and b ''''

        while b != 0:
            a, b = b, a % b
        return a

    We can use this as a helper function because we can't use loops with lambdas. Remember: Lambda is an expression, not a statement!
    Calling this helper function inside the lambda will help with loops

"""
from functools import reduce

# Helper gcd function (non recursive) because we can't use loops with lambdas.
def gcd(x, y):
    """ Assumes x and y are positive integers
        Returns the greatest common divisor of x and y """
    while y != 0:
        x, y = y, x % y
    
    return x

list1 = [18, 24, 36, 42]
#list1 = [18, 30, 42]

#greatestCommonDivisor = reduce(lambda x,y: x if y == 0 else gcd(y, x % y),list1)

# Test with helper function
#print(f"The greatest common divisor of {list1} is {greatestCommonDivisor}")

""" Note: I've also tested the following lambda with a recursive call, it works great without the need of helper function:

result = lambda x,y: x if y == 0 else result(y, x % y), which is way more elegant and smaller """

result = lambda x,y: x if y == 0 else result(y, x % y)

forList = reduce(lambda x,y: result(x, y), list1)

# Test recursive lambda
#print(f"The greatest common divisor of 18 and 24 is {result(18,24)}")

# Test recursive lambda with list
print(f"The greatest common divisor of {list1} is {forList}")