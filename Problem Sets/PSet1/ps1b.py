###########################
# 6.0002 Problem Set 1b: Space Change
# Name: Victor Correa
# Time: 4h30min

#================================
# Part B: Golden Eggs
#================================

# Helper function for recursive calls
def minIgnore(a, b):
    """ Assumes a, b are integers or None

    Returns int: the smaller valid integer 
    between a and b. Or None if both of them are None"""

    # Check if a is invalid
    if a is None:
        return b

    # Check if b is invalid
    if b is None:
        return a
    
    # If both are integers, returns the smallest one
    return min(a, b)

# Problem 1 - Completed
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # If already calculated for target weight, return it
    if target_weight in memo:
        return memo[target_weight]
    # Base case
    if target_weight == 0:
        numEggs = 0
    
    # Recursive call
    else:
        numEggs = None

        for egg in egg_weights:

            remainingWeight = target_weight - egg

            if remainingWeight < 0:
                # Prints what are the negative problems for test purpose only
                # print(f"negative subproblem: {remainingWeight}")
                continue
            
            # minIgnore is a helper function to ignore negative subproblems, because some subproblems does not have a solution
            numEggs = minIgnore(numEggs, dp_make_weight(egg_weights, remainingWeight) + 1)
    
    #Store the numEggs calculate for target_weight in memo
    memo[target_weight] = numEggs
    return numEggs

# Testing the algorithm for a weight of 99
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    #egg_weights = (1, 3, 4)
    #n = 17
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print(f"Therefore if we have eggs of weight {egg_weights} and the ship's maximum capacity is {n}, " \
          f"then we can bring up to {dp_make_weight(egg_weights, n)} eggs for each trip")
