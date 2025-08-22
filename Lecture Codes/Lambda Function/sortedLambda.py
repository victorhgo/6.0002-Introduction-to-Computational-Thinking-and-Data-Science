list1 =	['fox', 'Gnu', ' bee', 'CAT', 'EEL', 'ant', '  dog']

""" 
We can sort it by default using sorted() which will return:

['  dog', ' bee', 'CAT', 'EEL', 'Gnu', 'ant', 'fox']
"""

print(sorted(list1))

""" We could also define a key function to treat each string and return it better sorted """

def keyFunction(lst):
    """ Receives a list 
        Treats: case insensitive sorting, ignores leading and trailing spaces
        Returns a better list to be used with sorted
    """
    return lst.strip().casefold()

""" We can now call keyFunction as a key argument on sorted()
    ['ant', ' bee', 'CAT', '  dog', 'EEL', 'fox', 'Gnu'] """

print(sorted(list1, key=keyFunction))

""" But we could get rid of this function and use a lambda function on sorted() which will return the same result:
    ['ant', ' bee', 'CAT', '  dog', 'EEL', 'fox', 'Gnu'] """

print(sorted(list1, key=lambda lst: lst.strip().casefold()))