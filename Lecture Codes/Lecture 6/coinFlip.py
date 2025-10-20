""" Let's simulate flipping a coin n times and see the behavior for
amount of heads x tails """

import random

def flipCoin():
    """ Assumes a normal coin with Head or Tail
    Flips the coin and return whether it got Heads (H) or Tails (T) """
    coin = ['H','T']

    return random.choice(coin)

def multipleFlips(amnt):
    """ Flips the coin amnt times
    Assumes amnt is an integer
    Returns a list with faces """
    selection = []

    for _ in range(amnt):
        selection.append(flipCoin())

    return selection

def countFaces(amnt):
    """ Count how many Heads x Tails we got in a set of plays
    Return some statistical data """
    flips = multipleFlips(amnt)

    heads = 0
    tails = 0

    # Not the best way to count faces, but it will do
    for face in flips:

        if face == 'H':
            heads += 1
        if face == 'T':
            tails += 1
    
    return heads, tails
    
def simulateFlips():
    flips = [100, 1000, 10000, 100000, 1000000]

    for flip in flips:
        print(f"Flipping the coin {flip} times...")
        head, tail = countFaces(flip)
        
        print(f"Result: {round(head/flip * 100,2)}% Heads and {round(tail/flip * 100,2)}% Tails\n")
    
if __name__ == '__main__':
    # print(f"For 40 times, we got heads,tails = {countFaces(40)}")
    simulateFlips()