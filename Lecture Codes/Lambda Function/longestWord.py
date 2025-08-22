""" Write a lambda that returns the longest word in a list of strings. 

    max() - returns the largest item in an iterable or the largest of two or more arguments.
    Can work with iterables or objects. In case of iterables:

    Syntax : max(iterable, *iterables[, key, default]) 
    Parameters : 

        iterable : iterable object like list or string.
        *iterables : multiple iterables
        key : function where comparison of iterable is performed based on its return value
        default : value if the iterable is empty

    Returns : The maximum value. 

"""
list1 = ['eggs', 'bat', 'raven', 'trains', 'spy', 'space', 'stars', 'twinkle', 'bumblebee', 'shining', 'bohemia', 'shooting', 'dreams', 'mainframes', 'constitution']

print(f"Biggest string in {list1} is {(lambda lst: max(lst, key=len))(list1)}")