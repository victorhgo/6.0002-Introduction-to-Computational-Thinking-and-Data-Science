""" Use map() with a lambda to convert a list of temperatures from Celsius to Fahrenheit.

Syntax: map(function, iterables) 
    where iterables will be the list
 """

celsius = [36.7, 38.8, 27.4, 33.3, 28.9, 32.3, 29]

fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

print(f"Celsius to Fahrenheit: {celsius} -> {fahrenheit}")