###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Victor Correa   
# Time: 3h35min

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

# Problem 3
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
    # To ensure the cows are sorted from heavier to lighter
    cowsCopy = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    print(limit)

    for trip in get_partitions(cowsCopy):
        print(trip)

        
# Problem 4
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
    # TODO: Your code here
    pass

if __name__ == '__main__':

    cows = load_cows('ps1_cow_data.txt')

    # Test with limit = 10 first
    # print(cows)
    #bestCows = greedy_cow_transport(cows, 10)

    #print(f"Trip: {bestCows}")

    # Test partitions:
    # for cow in get_partitions(cows):  
    #     print(cow)

    brutecow = brute_force_cow_transport(cows,10)
    print(f"Trip: {brutecow}")