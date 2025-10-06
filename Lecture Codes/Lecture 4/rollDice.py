import random

def rollDice():
    """ Returns a randomly chosen int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + ' ' + str(rollDice())
    
    return result

# Simulation of dice rolling
def runSimulation(goal, numTrials, txt):
    total = 0

    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDice())

        if result == goal:
            total += 1
    
    print(f"Actual probability of {txt} is {round(1/(6**len(goal)), 8)}")
    estimateProbability = round(total/numTrials, 8)
    print(f"Estimated probability of {txt} is {round(estimateProbability,8)}")

if __name__ == "__main__":
    print(f"Rolling the dice 10 times: {rollN(10)}")

    # Running simulation for 1000 trials
    print("What's the probability of getting (1 1 1 1 1) with 1000 trials?")
    runSimulation('11111', 1000, '11111')
    print("\n-\n")

    # Running simulation for 10 000 trials
    print("What's the probability of getting (1 1 1 1 1) with 10 000 trials?")
    runSimulation('11111', 10000, '11111')
    print("\n-\n")

    # Running simulation for 100 000 trials
    print("What's the probability of getting (1 1 1 1 1) with 100 000 trials?")
    runSimulation('11111', 100000, '11111')
    print("\n-\n")

    # Running simulation for 1M trials
    print("What's the probability of getting (1 1 1 1 1) with 1 000 000 trials?")
    runSimulation('11111', 1000000, '11111')
    print("\n-\n")

    # Running simulation for 10 M trials
    print("What's the probability of getting (1 1 1 1 1) with 10 000 000 trials?")
    runSimulation('11111', 10000000, '11111')
    print("Finishes the simulation... Goodbye :-)")