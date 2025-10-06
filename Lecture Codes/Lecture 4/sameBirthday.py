import random
import math as math

def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthdays = [0] * 366

    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0

    for trial in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1

    return numHits/numTrials

for numPeople in [10, 20, 40, 100]:
    print(f"For {numPeople} people, the estimate probability of a shared birthday is {birthdayProb(numPeople, 2, 10000)}")
    
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366 - numPeople)
    print(f"Actual probability of N = {numPeople} = {1 - numerator/denom}\n")