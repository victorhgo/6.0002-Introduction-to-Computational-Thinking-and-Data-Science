# Problem Set 1.A - Space Cows Transportation

    Solution by Victor Correa
    Time spend on this activity: 7hours 25 minutes
    Completed on 11th September 2025

How to transport cows across the space when your spaceship has a weight limit and you want to **minimize** the number of trips across the universe.

## Problem A.1: Loading Cow Data:

First of all, we need to load the data to be used within our program, with the function ```load_cows``` we can do it by reading the file that has the cow's name and weight such data we need it to be loaded in a dictionary where the *key* is the cow's name and the *value* is its weight. A good approach is iterating through each file's line with ```readlines()``` method and attributing the data to the *key,value* pair on the dictionary as:

```py
def load_cows(filename):
    """
    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    file = open(filename, 'r')

    # Builds cows dictionary
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
    # First we create a copy of cows dictionary and sort it to bring the heaviest
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

> Trip: ['Betsy'], ['Henrietta'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']

Clearly it's not the most optimized solution, as this could be done is less trips than that. **Florence** for instance, is traveling alone while she weights only two tons.

Another problem is that dictionaries in Python uses way more memory than lists, it's okay to copy and pop a dictionary inside a loop for small inputs when we are testing only 10 items, but as the number of cows increases, it will add overhead (memory and time consuming on running the program) to the program.

Now that the implementation helped to figure it out how to solve this problem using the heuristic approach, now it's time to improve the algorithm. By analysing it closely, we can observe that the following improvements can make our code better and perhaps gain some extra performance:

- [X] - Instead of tracking a ```maxWeight```, we can think of it as *ship's remaining capacity for current trip*. It will make our logic more clear for the reader to follow.

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

In this approach, we need to use ```get_partitions``` which will transform every entry on the dictionary into a group (partition) of every possible trips. We can iterate through this list checking the total weight for each trip to see if it's within the ship's weight limit. If it is, we can consider it a good candidate. Then we can select the best option.

Our best trip partition is the most efficient one. In other words it is the trip combination that can transport every cow across the universe with the **minimum trips possible**.

Before we can start the implementation, let's take a look on a way of using summation in Python for a list with tuples *key,values*, this way we can check each trip combination and compare if the ship is not overweight. But first let's take a look on how Python turns a dictionary into a list:

- Suppose we have a dictionary of *key,value* such that each key is the name of the students and the value is their grades:

```students = {"Jesse": 6, "Walter": 10, "Gustavo": 6, "Hank": 7}```

We can transform this dictionary to a list of tuples such that the tuple will contain the (*key,value*) format:

```py
# Dictionary of students
students = {"Jesse": 6, "Walter": 10, "Gustavo": 6, "Hank": 7}

# Transform it to a list of tuples:
studentList = list(students.items())
```

Now the dictionary of students will be turn to a list of tuples in the following way:

```studentList = [('Jesse', 6), ('Walter', 10), ('Gustavo', 6), ('Hank', 7)]```

We can now access each name or grade independently by iterating over them. Note that we can use ```_``` indicating that we won't need the first variable ```name```, all that matters to us are their grades (the opposite is also valid):

```py
# Getting only the grades
for _, grade in studentList:
    print(grade)

# Getting only the names
for name, _ in studentList:
    print(name)
```

In the same way to access each item in the tuple, we can use the function ```sum()``` from Python which returns the sum of all items in an iterable. It has the following syntax:

    sum(iterable, start) 

So we can use the same idea as iterable to return the summation of every grade:

```py
# Store the sum of every grades in grade
grades = sum(grade for name, grade in studentList)
```

Back to the initial problem, since we are obtaining lists of every possible trip, we can sum up the weights for each trip and check which violates the ship's limit independently.

We start by creating a copy of cow dictionary which we will call ```cowsCopy```, which won't be sorted. Since we are getting a list of every possible sets, sorting is irrelevant for this approach. We can set a variable ```bestPartition``` which will contain the trips that don't exceed the ship's weight limit. We must initialize it as *None* because the first partition is valid, no cow surpasses the weight limit. Also len(partition) will be the same size of bestPartition, which will fail the later evaluation for best trips.

We are going to iterate on each partition (every trip possible) with:

```py
for partition in get_partitions(list(cowsCopy.items())):
```

For the example ```{“Jesse”: 6, “Maybel”: 3, “Callie”: 2, “Maggie”: 5}``` the code above will iterate over the following partitions (trip combination):

```sh
[[('Callie', 2), ('Jesse', 6), ('Maybel', 3), ('Maggie', 5)]]
[[('Callie', 2), ('Maggie', 5), ('Maybel', 3)], [('Jesse', 6)]]
[[('Callie', 2), ('Jesse', 6), ('Maggie', 5)], [('Maybel', 3)]]
[[('Callie', 2), ('Maggie', 5)], [('Jesse', 6), ('Maybel', 3)]]
[[('Callie', 2), ('Maggie', 5)], [('Maybel', 3)], [('Jesse', 6)]]
[[('Jesse', 6), ('Maybel', 3), ('Maggie', 5)], [('Callie', 2)]]
[[('Maggie', 5), ('Maybel', 3)], [('Callie', 2), ('Jesse', 6)]]
[[('Maggie', 5), ('Maybel', 3)], [('Jesse', 6)], [('Callie', 2)]]
[[('Jesse', 6), ('Maggie', 5)], [('Callie', 2), ('Maybel', 3)]]
[[('Jesse', 6), ('Maggie', 5)], [('Maybel', 3)], [('Callie', 2)]]
[[('Maggie', 5)], [('Callie', 2), ('Jesse', 6), ('Maybel', 3)]]
[[('Maggie', 5)], [('Jesse', 6), ('Maybel', 3)], [('Callie', 2)]]
[[('Maggie', 5)], [('Callie', 2), ('Maybel', 3)], [('Jesse', 6)]]
[[('Maggie', 5)], [('Maybel', 3)], [('Callie', 2), ('Jesse', 6)]]
[[('Maggie', 5)], [('Maybel', 3)], [('Jesse', 6)], [('Callie', 2)]]
```

We now can check which of these partitions (trip combinations) are going to violate the weight limit and exclude them, for that, we initialize the variable ```validPartition``` as *True* and we can validate in the following way:

1. For each trip in partition, if the sum of weights is greater than the shipt's limit, this trip is invalid, thus we set the ```validPartition = False``` and break the check.

2. If all the trips in the partition are valid, we first store it in ```bestPartition```and for each valid consequent partitions, we check if the amount of trips performed for this partition is smaller than the current selected ```bestPartition```. If yes, it means that this partition has a better solution than the last one, which means that we can transport more cow in less trips.

3. After every possible combination of trips are checked (every partition), we will have the best one stored in ```bestPartition```, and we can return a list containing the name of each cow per trip.

In our example, the best combination is: ```[['Maggie', 'Callie'], ['Maybel', 'Jesse']]```

We can also use iteration in the return statement to return only the partition containing the name of the cows in the following way

```return [[cowName for cowName, weight in trip] for trip in bestPartition]```

So instead of returning ```[[('Maggie', 5), ('Callie', 2)], [('Maybel', 3), ('Jesse', 6)]]``` it will return ```[['Maggie', 'Callie'], ['Maybel', 'Jesse']]```

The implementation for this version is:

```py
def brute_force_cow_transport(cows,limit):
    """
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
```

By running this **brute force** version, we ensure that we are selecting the best combination of trips possible, thus the optimal result relies on selecting which partition has the least amount of trips possible that does not exceeds the ship's weight limit, ensuring that every cow is being transported across the universe in the most optimized way.

## Problem A.4: Comparing the Cow Transport Algorithms

Implement ```compare_cow_transport_algorithms```, load the cow data in ```ps1_cow_data.txt```, and then run your greedy and brute force cow transport algorithms on the data to find the minimum number of trips found by each algorithm and how long each method takes. Use the default weight limits of 10 for both algorithms.

We can measure the time a block of code takes to execute using the time.time() function (from time library):

    start = time.time() 
    ## code to be timed 
    end = time.time() 
    print end – start

So we can implement a test for each algorithm as:

```py
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
    bruteAlgorithm = brute_force_cow_transport(cows,10)
    endBrute = time.time()

    print(f"Brute force result: {bruteAlgorithm}")
    print(f"Brute force ran in {endBrute - startBrute} seconds")

    # Test greedy heuristic
    startHeuristic = time.time()
    greedyAlgorithm = greedy_cow_transport(cows,10)
    endHeuristic = time.time()

    print(f"Greedy Heuristic result: {greedyAlgorithm}")
    print(f"Greedy heuristic ran in {endHeuristic - startHeuristic} seconds")
```

Running the test we get the following output:

```py
Brute force result: [['Henrietta'], ['Maggie', 'Moo Moo', 'Florence'], ['Betsy'], ['Milkshake', 'Millie', 'Lola'], ['Oreo'], ['Herman']]
Brute force ran in 0.22369980812072754 seconds
Greedy Heuristic result: [['Betsy'], ['Henrietta'], ['Herman', 'Maggie'], ['Oreo', 'Moo Moo'], ['Millie', 'Milkshake', 'Lola'], ['Florence']]
Greedy heuristic ran in 1.6927719116210938e-05 seconds
```

## Problem A.5: Writeup

Answer the following questions:

1. What were your results from compare_cow_transport_algorithms? Which algorithm runs faster? Why?

The greedy heuristic runs faster because it requires less computation to find a result, which is not the optimal one but it's faster. In the other hand, brute force will analyse every possible combination possible to select the most optimal one, it sacrifices computation to return the most optimised output.

2. Does the greedy algorithm return the optimal solution? Why/why not? Does the brute force algorithm return the optimal solution? Why/why not? 

Both algorithm could transport every cow in only 6 trips, which means that both version are returning the most optimal solution for this particular cow's set. But if we increase the amount of cows, the brute force one will return the best result for analysing every possible combination and selecting the best.