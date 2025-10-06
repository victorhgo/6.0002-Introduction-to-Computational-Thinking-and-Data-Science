""" Coin Change (Minimum Coins, Greedy version)

    - Given coin denominations ```{1, 5, 10, 25}``` and an amount $N$,

    - Find the minimum number of coins to make $N$.

    - Approach: Greedy works when the coin system is canonical (like U.S. coins)."""

"""
Good tests to start with:

n = 11 > 2 coins: 1 and 10
n = 15 > 2 coins: 5 and 10
n = 16 > 3 coins: 5, 10 and 1
n = 7 > 3 coins: 5, 1 and 1
...
"""

def chooseCoin(coins, targetChange):
    """ Parameters:
    coins - a list of coin values
    targetChange - integer, the amount we want to return
    
    Returns:

    numCoins - integer, minimum amount of coins 
    """
    copyCoins = list(sorted(coins, reverse=True))

    selectedAmount = 0
    numCoins = 0

    for coin in copyCoins:
        
        if coin + selectedAmount <= targetChange:
            selectedAmount += coin
            numCoins += 1
            print(f"Selected coin: {coin} selectedAmount: {selectedAmount} and number of coins {numCoins}")
        



if __name__ == '__main__':
    coins = [1, 5, 10, 25]
    change = 11

    print(f"Test1: coins {coins} and change {change} = {chooseCoin(coins,change)}")
    