""" Exercise 4 - Rod Cutting Problem

    - Given a rod of length $n$ and a table of prices for each piece length,

    - Determine the maximum revenue obtainable by cutting up the rod. """

# Define the class Rod
class Rod(object):
    def __init__(self, length, price):
        self.length = length
        self.price = price

    #Getter Methods
    def getLength(self):
        return self.length
    
    def getPrice(self):
        return self.price
    
    def __str__(self):
        return 'Rod len(' + str(self.length) + '), price = ' + str(self.price)
    
    def __repr__(self):
        return self.__str__()
    
# Build function

def buildRod(length, price):
    """ Assumes length, price are lists
    returns rod : list of each rod's length containing:
    [length, price] """
    rod = []

    for i in range(len(length)):
        rod.append(Rod(length[i], price[i]))

    return rod

# Best option
def bestProfit(n, rod):
    """ Assumes n an integer (n is total size of rod) and rod is a list of Rod objects
    Returns the best revenue for a rod of length n based on each length's price """

    # If we make no cut - Base case
    if n == 0:
        return 0, [] # Empty list, no cut was made

    maxProfit = 0
    bestCuts = [] 

    # Let's try all cut's of length i
    for i in range(1, n + 1):
        remainingProfit, remainingCuts = bestProfit(n - i, rod)

        profit = rod[i - 1].getPrice() + remainingProfit

        cuts = [i] + remainingCuts

        # Prints what it's trying to cut 
        print(f"Trying cut {i} on rod length {n}: profit = {profit}, cuts = {cuts}")

        # To keep a track of the best option profit x cuts
        if profit > maxProfit:
            maxProfit = profit
            bestCuts = cuts

    return maxProfit, bestCuts

# Best option optimized with a dictionary
def bestProfitOptimized(n, rod, memo = {}):
    """ Assumes n an integer (n is total size of rod) and rod is a list of Rod objects
    Returns the best revenue for a rod of length n based on each length's price in form of a tuple (price, cuts)"""

    # If we make no cut - Base case
    if n == 0:
        return 0, [] # Empty list, no cut was made

    # Variables initialization
    maxProfit = 0
    bestCuts = [] 

    # Check if it already calculated for len = n
    if n in memo:
        return memo[n]

    else:
        for i in range(1, n + 1):
            remainingProfit, remainingCuts = bestProfitOptimized(n - i, rod, memo)

            profit = rod[i - 1].getPrice() + remainingProfit

            cuts = [i] + remainingCuts
            #print(f"Trying cut {i} on rod length {n}: profit = {profit}, cuts = {cuts}")

            # To keep a track of the best option profit x cuts
            if profit > maxProfit:
                maxProfit = profit
                bestCuts = cuts


        # Store maxProfit and bestCuts in memo for each key n
        memo[n] = (maxProfit, bestCuts)

    return memo[n]
    
# First test, build a rod and print it
length = [1, 2, 3, 4]
price = [2, 6, 8, 10]

length1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
price1 = [1, 5, 8, 9, 10, 17, 18, 20, 24, 25]

length2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
price2 = [1, 5, 6, 9, 10, 15, 16, 19, 21, 21, 22, 23, 25, 27, 29, 29, 30, 30, 31, 31, 31, 32, 33, 33, 34, 34, 35, 35, 35, 36]

rod1 = buildRod(length, price)

rod2 = buildRod(length1, price1)

rod3 = buildRod(length2, price2)

#profit, cut = bestProfit(4, rod1)
#profit1, cut1 = bestProfitOptimized(4, rod1)

profit3, cut3 = bestProfitOptimized(30, rod3)
#profit3, cut3 = bestProfit(30, rod3)

#print(f"Rod2 (not opt) best profit = {profit} with best cuts: {cut}")
#print(f"Rod2, (opt) best profit = {profit1} with best cuts: {cut1}")
print(f"Rod3(len 30) best profit = {profit3} with best cuts: {cut3}")

