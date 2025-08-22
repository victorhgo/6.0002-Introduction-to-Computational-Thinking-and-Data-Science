""" Use a lambda with map() to capitalize the first letter of each word in a list. 

    map() - used for applying a function to every item in an iterable

    Syntax: map(function, iterables) 
    where iterables will be the list

    
    I might use capitalize() function to do that.

    capitalize() - converts the first character of a string to uppercase and the remaining characters to lowercase.
"""

#list1 = "Hello, this is the first list just for test purpose only."
list1 = ['cunningly', 'creatures,', 'accomplish', 'substance,', 'thee', 'individual', 'necessary.', 'acknowledge', 'transmutest', 'generation,', 'governance.', 'influences,', 'instruction.', 'substantial,', 'individualized']

upperList = list(map(lambda x: x.capitalize(), list1))

print(upperList)