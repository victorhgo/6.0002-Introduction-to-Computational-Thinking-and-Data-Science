""" Use a lambda with filter() to remove all words shorter than 4 characters from a list. 

    filter() - used to pull out elements from an iterable but only if they pass a test. 
    Needs a function (also called predicate) that takes each item and returns True or False . 
    
    If the test passes (if function returns True ) filter() keeps it.

    Syntax: filter(function, iterable) 
"""

list1 = ['eggs', 'bat', 'raven', 'trains', 'spy', 'space', 'stars', 'twinkle', 'shining', 'bohemia', 'shooting', 'dreams']

biggerWords = list(filter(lambda x: len(x) >= 4, list1))

print(biggerWords)