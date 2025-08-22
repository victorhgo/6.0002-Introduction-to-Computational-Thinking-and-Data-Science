"""  Use reduce() with a lambda to find the product of all numbers in a list.
    reduce() - From functools. The reduce() function in Python applies a given function cumulatively to all items in an iterable, 
    reducing it to a single final value.

    Syntax : reduce(function, iterable[,init])
    Notes: function must take two values and returns one
           iterable is the sequence to be reduced
           init is optional, starting value that is placed before first element.

"""
from functools import reduce

#list1 = list(range(1,10))

list1 = [2, 3, 5, 7, 11]

mult = reduce(lambda x, y: x * y,list1)

print(mult)
