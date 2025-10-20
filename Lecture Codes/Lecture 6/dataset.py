import math
import random

def generateSample(ran):
    """ Assumes ran is an integer
    Builds a list from 1 to ran (range)
    Returns the list """
    sample = []

    try:
        sample = [random.randint(1, 100) for _ in range(1, ran)]

        return sample

    except TypeError:
        return "Range is not an integer"
        
def getSample(fileName):
    """ Loads the sample and builds a list
    Parameter: fileName

    Assumes:
        fileName is a .txt and each line of fileName is a number representing a person's age

    Returns:
        A list with all age as integers, called sample """

    print(f"Loading sample from file {fileName}...\n")

    sample = []

    with open(fileName, 'r') as file:

        # Iterate over each file's line
        for line in file:

            if line.strip() == '':
                continue
        
            sample.append(int(line))
        
    return sample

def getMean(sample):
    """ Assumes sample is a list with statistical data (person's age)
    Returns the Mean of sample (in this case, average age of a sample's group)"""
    try:
        return round(sum(sample)/len(sample),2)
    
    except TypeError:
        return "Sample could not be loaded"

def standardDeviation(sample):
    """ Assumes Sample is a list with statistical data (person's age)
    Returns the Standard Deviation of data (how much the ages are dispersed in this sample)"""
    total = 0

    try:
        mean = getMean(sample)
        total += sum((num - mean) **2 for num in sample)

        return round(math.sqrt(total/len(sample)),3)
    
    except TypeError:
        return "Sample could not be loaded"
    
def testSample():
    """ 
    A small test with a known dataset
    """
    sample = [10, 15, 20, 25, 30]
    
    assert getMean(sample) == 20, f"Expected Mean: 20, got: {getMean(sample)}"
    assert standardDeviation(sample) == 7.071, f"Expected standardDeviation: 7.0711, got: {standardDeviation(sample)}"

    print(f"Test successfully completed!")

def simPopulation():
    """
    Runs a simulation generating populations of different sizes
    and prints the mean and standard deviation for each population's age.
    """
    sample_sizes = [100, 1000, 100000, 1000000]

    print("--- Starting Simulation ---\n")

    for size in sample_sizes:

        sample = generateSample(size)

        print(f"Population size: {size:>8,}")
        print(f"Average Age: {getMean(sample)}")
        print(f"Standard deviation: {standardDeviation(sample)}")
        print("--------------------")
    
    print("--- End of Simulation ---\n")

def realPopulationTest():

    # New York City Test
    newYork = getSample("nycAges.txt")

    print(f"NYC Population: {len(newYork)}")
    print(f"Average age of NYC Population: {getMean(newYork)}")
    print(f"Standard Deviation: {standardDeviation(newYork)}\n")

    # Sweden Test
    sweden = getSample("swedenAges.txt")

    print(f"Sweden Population = {len(sweden)}")
    print(f"Average age of Sweden Population: {getMean(sweden)}")
    print(f"Standard Deviation = {standardDeviation(sweden)}\n")

    # Niger Test
    niger = getSample("nigerAges.txt")

    print(f"Niger Population = {len(niger)}")
    print(f"Average age of Niger Population: {getMean(niger)}")
    print(f"Standard Deviation = {standardDeviation(niger)}\n")

    # Japan
    japan = getSample("japanAges.txt")

    print(f"Japan Population = {len(japan)}")
    print(f"Average age of Japan Population: {getMean(japan)}")
    print(f"Standard Deviation = {standardDeviation(japan)}\n")

if __name__ == "__main__":
    # Sanity Check with randomAges.txt
    # random.seed(random.random())

    # testSample()
    print(f"Begin sanity check with dataset")
    sample = getSample("randomAges.txt")

    print(f"Total population: {len(sample)}. Population average age = {getMean(sample)}")
    print(f"Standard Deviation = {standardDeviation(sample)}\n")
    #print("End of sanity check. Now the simulation:")

    # Simulation 1
    # simPopulation()