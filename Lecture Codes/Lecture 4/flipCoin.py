import random

def flipCoin():
    """ Returns a randomly chosen side between 0 and 1, where:
    0 for Heads and 1 for Tails.
    """
    return random.choice([0, 1])

def flip(n):
    result = ''
    for i in range(n):
        result = result + ' ' + str(flipCoin())
    
    return result

if __name__ == "__main__":
    print(f"Flipping the coin 10 times: {flip(10)}")