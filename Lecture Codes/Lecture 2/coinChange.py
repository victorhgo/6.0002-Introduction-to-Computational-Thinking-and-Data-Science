""" Coin Change (Minimum Coins, Greedy version)

    - Given coin denominations ```{1, 5, 10, 25}``` and an amount $N$,

    - Find the minimum number of coins to make $N$.

    - Approach: Greedy works when the coin system is canonical (like U.S. coins)."""

# I won't be using OOP for now

coins = [1, 5, 10, 25]

"""
Good tests to start with:

n = 11 > 2 coins: 1 and 10
n = 15 > 2 coins: 5 and 10
n = 16 > 3 coins: 5, 10 and 1
n = 7 > 3 coins: 5, 1 and 1
...
"""

