def addition(x, y):
    """ Assumes x and y are two real numbers
        Returns their sum """
    return x + y

# Instead of this function, we can do it by a lambda function
addition1 = lambda x, y : x + y

print("Sum of 15 and 20 is", addition1(15, 20))