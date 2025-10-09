###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Victor Correa   
# Time: 7h25min

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1 - Completed in 35 minutes
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    file = open(filename, 'r')

    #Build cows dictionary
    cows = {}

    for lines in file.readlines():

        cowName = lines.split(',')[0]
        cowWeight = lines.split(',')[1]

        cows[cowName] = (int(cowWeight))

    # Closes the file
    file.close()

    return cows
    

# Problem 2 - Completed in 3 hours
def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips """

    # To ensure the cows are sorted from heavier to lighter
    cowsCopy = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))

    # Where we store the best combination of cows for each trip
    trips = []

    while cowsCopy != {}:
        # Store each cow selected for the trip
        currentTrip = []

        # Ship's remaining capacity
        currentWeight = 0

        # We will create a new dictionary to store every cow that hasn't been selected yet
        remainingCows = {}

        for cow, weight in list(cowsCopy.items()):

            if (currentWeight + weight) <= limit:
                currentTrip.append(cow)
                currentWeight += weight
            # If cow not selected for trip, store it on the dictionary remainingCows
            else:
                remainingCows[cow] = (weight)

        trips.append(currentTrip)

        #cowsCopy will receive all the remaining cows, until empty
        cowsCopy = remainingCows

    return trips

# Problem 3 - Completed in 3h30min
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsCopy = cows

    # the bestPartition is the one that no trip exceeds the ship's weight limit and can do it in the most optimal way (less trips)
    bestPartition = None

    # Let's iterate over each partitions (possible trips) and test for each trip (current trip)
    for partition in get_partitions(list(cowsCopy.items())):
        # Suppose all the trips in the partition are valid
        validPartition = True

        # For each trip in the current partition, test if their weight sum exceeds the ship's limit
        for trip in partition:

            # If any trip's total weight exceeds the ship's limit, the trip is invalid. Thus the whole partition is invalid
            if sum(cowWeight for cowName, cowWeight in trip) > limit:
                validPartition = False
                break

        # If all the trips in the partition are valid, bestPartition == None for the first best choice and compare the size of partition with the current selected bestPartition
        if validPartition and (bestPartition == None or len(partition) < len(bestPartition)):
            bestPartition = partition

    # Return only the trips with cow's name for each trip in the best partition
    return [[cowName for cowName, weight in trip] for trip in bestPartition]
        
# Problem 4 - Completed in 20 min
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # Load all the cows from ps1_cow_data.txt:
    cows = load_cows('ps1_cow_data.txt')
    # Test Brute Force first
    startBrute = time.time()
    bruteAlgorithm = brute_force_cow_transport(cows,12)
    endBrute = time.time()

    print(f"Brute force result: {bruteAlgorithm}")
    print(f"Brute force ran in {endBrute - startBrute} seconds")

    # Test greedy heuristic
    startHeuristic = time.time()
    greedyAlgorithm = greedy_cow_transport(cows,12)
    endHeuristic = time.time()

    print(f"Greedy Heuristic result: {greedyAlgorithm}")
    print(f"Greedy heuristic ran in {endHeuristic - startHeuristic} seconds")

if __name__ == '__main__':

    cows = load_cows('ps1_cow_data.txt')

    # Test with limit = 10 first
    # print(cows)
    #bestCows = greedy_cow_transport(cows, 10)

    #print(f"Trip: {bestCows}")

    # Test partitions: PASS
    # for cow in get_partitions(cows):  
    #     print(cow)

    #brutecow = brute_force_cow_transport(cows,10)
    # smallCows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    # bruteSmall = brute_force_cow_transport(smallCows, 7)
    # print(f"Trip: {bruteSmall}")
    # bestCows = greedy_cow_transport(smallCows, 7)
    # print(f"Trip: {bestCows}")
    # Run the test
    compare_cow_transport_algorithms()

    
