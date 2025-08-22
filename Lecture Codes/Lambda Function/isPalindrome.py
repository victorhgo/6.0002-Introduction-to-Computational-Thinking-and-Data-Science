# Write a lambda function to check if a string is a palindrome.

morocco = "Socorram me subi no onibus em Marrocos"
napoleon = "Able was I ere I saw Elba"

""" Used Methods to achieve this in the minimal way possible:

casefold() - The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, 
meaning that it will convert more characters into lower case, and will find more matches when comparing 
two strings and both are converted using the casefold() method.

---

replace(" ", "") - Replaces all spaces with no spaces

---

We can reverse a string with string[::-1] """

isPalindrome = lambda str: str.casefold().replace(" ","") == str[::-1].casefold().replace(" ","")

print(f"{morocco} is a palindrome: {isPalindrome(morocco)}")
print(f"{napoleon} is a palindrome: {isPalindrome(napoleon)}")

# Tests to figure it out the spaces, lowercase
print(f"{morocco.casefold().replace(" ","")}")
print(f"{morocco[::-1].casefold().replace(" ","")}")


