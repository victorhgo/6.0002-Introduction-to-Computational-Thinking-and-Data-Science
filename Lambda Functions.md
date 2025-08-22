# $\lambda$ Lambda Functions 

I decided to write this small but useful note to further develop the idea of lambda functions which can be really handy.

## What is a Lambda Function? $\lambda$

When writing programs, sometimes we may encounter a situation where we need to write a small function that will run only once during the entire program's execution. For instance: we need to sum two real numbers x and y, we could do that by writing a small function that receives x and y and returns their sum like:

```py
def addition(x, y):
    """ Assumes x and y are two real numbers
        Returns their sum """
    return x + y
```

Then we would just need to call the function by it's name and input the two values for x and y like:

    addition(15, 20)

This is appropriate when we define a function that will be used more than once, but as stated, what if we want to use the function only once?

We can use Python's native ```lambda function``` also known as ```anonymous function```, which is defined as a **small anonymous function**. Why anonymous? Because it has no name to be called. A lambda function can have multiple inputs, but only one expression, that's why it's suited for writing small functions instead of the standard ```def```. It's syntax:

    lambda args : expression

Going back to the previous example, we could rewrite it simply as:

```py
addition = lambda x,y : x + y

print(addition(15,20))
```

So essentially, lambda functions are just small disposable functions. Python guidelines discourages programmers to assigning lambda functions directly to variables because it's hard to debug errors in the code if all functions have a generic and anonymous name.

## Why do we use Lambda Functions?

Lambda Functions are better used when we need to pass one function as an argument to another. For instance, we want to sort a list of strings where the strings are a mess: they're with different cases, spaces. Instead of writing a ```def``` function to treat this list and pass as a key argument on ```sorted()``` function, we can simply write a lambda function like:

```py
list1 =	['fox', 'Gnu', ' bee', 'CAT', 'EEL', 'ant', '  dog']

print(sorted(list1, key=lambda lst: lst.strip().casefold()))
```

In the above example, the lambda function is transient: it's born when we call the ```sorted()``` and it dies when sorted returns its result. For tiny functions that we use only once in the code, lambda functions help with memory usage.

We can also use lambda functions as anonymous functions inside other functions, for instance. A function receives an integer and returns the result multiplied by an unknown number:

```py
def func(n):
    """ Assumes n is a real,
        Returns n * a """
    return lambda a: a * n

# This will always double the number
doubler = func(2) 

# This will always triple the number
triple = func(3)

# Then we can call the functions with the values we want to double, triple...

print(f"Double: {doubler(3)}")
print(f"Triple: {triple(3)}")
```

## Exercises $\lambda$

*Solutions at /Lecture Codes/Lambda Function/*

**Beginner**

- [X] - Write a lambda function to add 10 to a given number.

- [X] - Write a lambda function to check if a number is even.

- [X] - Write a lambda function that returns the square of a number.

- [X] - Write a lambda function to extract the last character of a string.

- [X] - Write a lambda function to check if a string is a palindrome.

**Intermediate Level**

- [X] - Use ```map()``` with a lambda to convert a list of temperatures from Celsius to Fahrenheit.

- [X] - Use ```filter()``` with a lambda to keep only prime numbers from a list.

- [X] - Use ```reduce()``` with a lambda to find the product of all numbers in a list.

- [X] - Write a lambda that sorts a list of tuples by the second element.

- [X] - Write a lambda that sorts words in a sentence by length.

**Advanced Level**

- [X] - Use a lambda with ```map()``` to capitalize the first letter of each word in a list.

- [X] - Use a lambda with ```filter()``` to remove all words shorter than 4 characters from a list.

- [ ] - Write a lambda to check if a given year is a leap year.

- [ ] - Use a lambda inside ```sorted()``` to sort a dictionary by its values.

- [ ] - Write a lambda that takes a number and returns "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, otherwise the number itself.

**Challenges**

- [ ] - Write a lambda to flatten a nested list ```[[1,2],[3,4],[5,6]] → [1,2,3,4,5,6]```.

- [X] - Write a lambda that returns the longest word in a list of strings.

- [ ] - Write a lambda to count how many words in a list start with a vowel.

- [X] - Use ```reduce()``` with a lambda to compute the greatest common divisor (GCD) of a list of numbers.

- [ ] - Create a lambda-based function composition: given two lambdas f and g, return a new lambda ```h(x) = f(g(x))```.