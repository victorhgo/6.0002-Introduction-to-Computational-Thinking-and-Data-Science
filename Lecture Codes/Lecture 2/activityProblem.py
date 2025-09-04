"""
Activity Selection Problem: You are given a list of $n$ activities, each with a start time and a finish time. 
Two activities are said to be **compatible** if they do not overlap in time. You can do only one activity at a time.

Select the maximum number of non-overlapping activities. Think of it like scheduling talks at a conference where 
you want to attend as many as possible, but you can't be in two talks at the same time.

    | Activity | Start | Finish |
    |:--------:|:-----:|:------:|
    |    A1    |   1   |   4    |
    |    A2    |   3   |   5    |
    |    A3    |   0   |   6    |
    |    A4    |   5   |   7    |
    |    A5    |   3   |   9    |
    |    A6    |   5   |   9    |
    |    A7    |   6   |   10   |
    |    A8    |   8   |   11   |
    |    A9    |   8   |   12   |
    |    A10   |   2   |   14   |
"""
class Activity(object):
    def __init__(self, act, start, finish):
        self.activity = act
        self.start = start
        self.finish = finish

    # Getters Methods
    def getName(self):
        return self.activity
    
    def getStart(self):
        return self.start
    
    def getFinish(self):
        return self.finish
    
    def __str__(self):

        return 'Activity: ' + self.activity + ': (start: ' + str(self.start)\
                + ', finish: ' + str(self.finish) + ')'
    def __repr__(self):
        """ Represent it as a list"""
        return self.__str__()


def buildActivityDataset(activity, start, finish):
    """ Assumes activity, start and finish are lists
    returns dataset : list of each activity containing:
    [activity, start, finish] """
    dataset = []

    for i in range(len(start)):
        dataset.append(Activity(activity[i], start[i], finish[i]))

    return dataset

def sortFinishTime(unsortedList):
    """ Assumes unsortedList is a non ordered list such that 
    each element is also a list with 3 elements: <activity, start, finish>
        Returns a copy of this list sorted by finish time """

    sortedList = list(sorted(unsortedList, key=lambda x: x.getFinish()))

    return sortedList

""" Note: After sorting by finish times, I need to iterate through the list and select activities one by one, 
making sure the start time of the next activity is not less than the finish time of the last chosen activity.

The greedy algorithm should have the following structure:

- Pick the first activity (with the earliest finish)

- Now: For each subsequent activity: is it compatible with the last picked one? If yes, keep it.”

- This loop structure is the core of the greedy choice.

"""

def greedySelection(dataset):
    """ Assumes dataset is an unsorted list of activities
    Returns the set of selected activities (best schedule) """

    # Sort the dataset putting the earliest finish time first
    sortedDataset = sortFinishTime(dataset)

    bestSchedule = []

    # Here I pick the first activity
    bestSchedule.append(sortedDataset[0])

    # The last chosen item

    lastChosen = sortedDataset[0]

    for i in range(1, len(sortedDataset)):
        if (sortedDataset[i].getStart() >= lastChosen.getFinish()):
            bestSchedule.append(sortedDataset[i])
            # To keep track of each selection
            lastChosen = sortedDataset[i]

    return bestSchedule

activities = ['a1', 'a2', 'a3', 'a4', 'a5',
              'a6', 'a7', 'a8', 'a9', 'a10']
start = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2]
finish = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14]

dataset = buildActivityDataset(activities, start, finish)

bestSchedule = greedySelection(dataset)

# Printing the best schedule

print("The best schedule is:")
for activity in bestSchedule:
    print(f"  {activity}")