""" Write a lambda that sorts a list of tuples by the second element.

    For this example we can use sorted():

    The sorted() function returns a sorted list of the specified iterable object.
    You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.   

    Syntax: sorted(iterable, key=key, reverse=reverse) where,
    iterable: the sequence to be sorted
    key: Optional, but it can be the function to decide the order to be sorted
    reverse: Also Optional, but it is Boolean. False will sort ascending, True will sort descending. Default is False

    Let's use as a key the second element for each tuple (element[1]):

"""

list1 = [
    ("apple", 5),
    ("banana", 2),
    ("cherry", 7),
    ("date", 3),
    ("elderberry", 1),
    ("fig", 6),
    ("grape", 4)
]

listSorted = list(sorted(list1, key=lambda x: x[1]))

print(f"Unsorted List: {list1}")
print(f"Sorted list: {listSorted}")