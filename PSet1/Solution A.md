# Problem Set 1 - Space Cows Transportation

    Solution by Victor Correa
    Time spend on this activity: 3 hours
    Completed on

How to transport cows across the space when your spaceship has a weight limit and you want to **minimize** the number of trips across the universe.

## Problem A.1: Loading Cow Data:

First of all, we need to load the data to be used with our program, with the function ```load_cows``` we can do it by reading the file that has the cow's name and weight such data we need it to be loaded in a dictionary where the *key* is the cow's name and the *value* is its weight. A good approach is iterating through each file's line with ```readlines()``` method and attributing the data to the *key,value* pair on the dictionary as:

```py
def load_cows(filename):
    """
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
```

## Problem A.2: Greedy Cow Transport

We can transport the cows by always picking the **heaviest** cow that will fit the spaceship first. So we can implement a greedy algorithm for transporting the cows where the result should be a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip:

We need to make sure to not mutate the dictionary of cows that is passed in. We can achieve that by creating a copy of the dictionary to be used within the function. Since the order of the list of trips does not matter, we can focus on getting the heaviest cows first.

**Example provided by the activity instruction**

Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is ```{“Jesse”: 6, “Maybel”: 3, “Callie”: 2, “Maggie”: 5}```. The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is ```[“Jesse”, “Maybel”]```. 
For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as the last cow. Since they will both fit, this makes the second trip ```[“Maggie”, “Callie”]```.  
The final result then is ```[[“Jesse”, “Maybel”], [“Maggie”, “Callie”]]```.

A first approach for this problem could be achieved by the following algorithm: 

```py
def greedy_cow_transport(cows,limit):
    """ Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips """
    # First thing we need, the copy of cows dictionary and sort to bring the heaviest
    # cows for the first trips
    cowsCopy = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    
    # Where we store the best combination of cows for each trip
    trips = []
    selection = []
    maxWeight = 0

    while cowsCopy != {}:

        for cow, weight in list(cowsCopy.items()):

            if (maxWeight + weight) <= limit:
                selection.append(cow)
                cowsCopy.pop(cow)
                maxWeight += weight
        
        maxWeight = 0
        trips.append(selection)
        selection = []

    return trips
```

Python does not support editing the value of a dictionary directly, so we can assign the *keys,values* to lists *cow,weight* using ```for cow, weight in list(cowsCopy.items()):```, this way we can work with *keys,values* independently.

Notes on the algorithm: By sorting the cows by weight and placing the heaviest ones first, ensuring they will be selected first will not guarantee the most optimal solution, where we do the transportation within the minimum number of trips possible. So let's analyse the following trips:

> Trip: [['Betsy'], ['Henrietta'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']]

Clearly it's not the most optimized solution, as this could be done is less trips than that. Florence for instance, is traveling alone while she weights only two tons.

Another problem is that dictionaries in Python uses way more memory than lists, it's okay to copy and pop a dictionary inside a loop for small inputs, we are testing for only 10 items, but as the number of cows increases, it will add overhead (memory and time consuming on running the program).

Now that the implementation helped us figure it out how to solve this problem using the heuristic approach, now it's time to improve it. Analysing it more close, we can conclude the following improvements can be done to make the code better and maybe get some extra performance:

- [X] - Instead of tracking a ```maxWeight```, we can think of it as *ship's remaining capacity for this trip*. It will make our logic more clear for the reader to follow.

Solution: ```remainingCapacity``` is a better name to track ship's remaining capacity for each trip.

- [X] - Instead of popping items directly from the dictionary, we can avoid destructive updates by building a *to remove* list first. 

Solution: We can create a new dictionary and call it ```remainingCows``` and store each cow that didn't go in the current trip. Thus instead of popping each cow directly from ```cowsCopy```, we can reassign ```remainingCows``` to ```cowsCopy``` directly, removing the previous destructive update method.

- [X] - We can avoid nested loops, making the algorithm more concise and transparent, thus making the logic easier to follow.

Solution: By using the filtering above and removing the destructive update, we can now use a single loop for each trip. The selection logic will be inside one loop.

For the second approach for this issue, making all the improvements, the algorithm will look like:

```py
def greedy_cow_transport(cows,limit):
    """ Parameters:
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
```

This heuristic approach is working as expected and the readability improved a lot, with an easy to follow logic. Even though we still having the same issues: this algorithm won't return the optimal solution. For a optimal solution we need a **brute force** approach, which leads to the part 3 of this problem.

## Problem A.3: Brute Force Cow Transport

Another way to transport the cows is to look at every possible combination of trips and pick the best one. This is an example of a **brute force algorithm**. Implement a brute force algorithm to find the minimum number of trips needed to take all the cows across the universe in ```brute_force_cow_transport```. The result should be a list of lists, where each inner list represents a trip and contains the names of cows taken on that trip.

**Notes:**

-  Make sure not to mutate the dictionary of cows!:

- In order to enumerate all possible combinations of trips, you will want to work with set partitions. We have provided you with a helper function called get_partitions that generates all the set partitions for a set of cows.

The helper function ```get_partitions``` generates the set partition such that all the possible 2-partitions of the list ```[1,2,3,4]``` are ```[[1,2],[3,4]], [[1,3],[2,4]], [[2,3],[1,4]], [[1],[2,3,4]], [[2],[1,3,4]], [[3],[1,2,4]], [[4],[1,2,3]]```. Helper functions at ```ps1_partition.py```:

```py
# From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]
```

Testing ```get_partition```:

```py
>>> for partition in get_partitions([1,2,3]):  print(partition)

[[1, 2, 3]]
[[2, 3], [1]]
[[1, 3], [2]]
[[3], [1, 2]]
[[3], [2], [1]]
```

**Example for the brute force algorithm**:

Example: Suppose the spaceship has a cargo weight limit of 10 tons and the set of cows to transport is ```{“Jesse”: 6, “Maybel”: 3, “Callie”: 2, “Maggie”: 5}```.  

The brute force algorithm will first try to fit them on only one trip, ```[“Jesse”, “Maybel”, “Callie”, “Maggie”]```. Since this trip contains 16 tons of cows, it is over the weight limit and does not work. Then the algorithm will try fitting them on all combinations of two trips. 

Suppose it first tries ```[[“Jesse”, “Maggie”], [“Maybel”, “Callie”]]```.  This solution will be rejected because Jesse and Maggie together are over the weight limit and cannot be on the same trip. The algorithm will continue trying two trip partitions until it finds one that works, such as ```[[“Jesse”, “Callie”], [“Maybel”, “Maggie”]]```.

The final result is then ```[[“Jesse”, “Callie”], [“Maybel”, “Maggie”]]```.

### Implementation of a brute force algorithm for the cow transport problem

TODO


## Problem A.4: Comparing the Cow Transport Algorithms

Implement ```compare_cow_transport_algorithms```, load the cow data in ```ps1_cow_data.txt```, and then run your greedy and brute force cow transport algorithms on the data to find the minimum number of trips found by each algorithm and how long each method takes. Use the default weight limits of 10 for both algorithms.

**Note:** Make sure you’ve tested both your greedy and brute force algorithms before you implement this

TODO

## Problem A.5: Writeup

Answer the following questions:

1. What were your results from compare_cow_transport_algorithms? Which algorithm runs faster? Why?

2. Does the greedy algorithm return the optimal solution? Why/why not? 3.  Does the brute force algorithm return the optimal solution? Why/why not? 

TODO