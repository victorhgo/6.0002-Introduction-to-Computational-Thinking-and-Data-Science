import random 

class FairRoulette():
    """ Assumes our roulette is a fair one 
    
    self.pocketOdds -> if we make a bet on a pocket and win,
    we'll get len of pockets - 1 (if we bet 1$ and win, we get 1$ + 35$ back)
    """
    def __init__(self):
        self.pockets = []

        for i in range(1,37):
            """ Pockets from 1 to 37 """
            self.pockets.append(i)

        # Ball initiates at None pocket
        self.ball = None
        
        self.pocketOdds = len(self.pockets) - 1

    def spinRoulette(self):
        """ Spins the roulette and the ball will stop in a random pocket """
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amount):
        """ Bets an amount of money into a pocket

        Parameters: pocket (an integer) and amount (a float) 
        
        If the bet pocket is selected, returns the amount bet times
        the odds of getting this pocket. If we lose, we lose the amount bet

        Return the amount of money (lost or win)  
        """

        if str(pocket) == str(self.ball):
            return amount * self.pocketOdds
    
        else: return -amount

    def __str__(self):
        return "Fair roulette"
    
class EuropeanRoulette(FairRoulette):
    """ A subclass of FairRoulette, where europeans add an extra pocket 0 """
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    
    def __str__(self):
        return 'European Roulette'
    
class AmericanRoulette(EuropeanRoulette):
    """ A subclass of EuropeanRoulette, where there's two extra pocket 0 and 00 """
    def __init__(self):
        EuropeanRoulette.__init__(self)
        self.pockets.append('00')
    
    def __str__(self):
        return 'American Roulette'
    
def playRoulette(game, numSpins, pocket, bet, toPrint = False):
    """ Simulates a game of roulette:
    
    Parameters:

    game - what kind of game we're playing
    numSpins - how many spins we want in this game (integer)
    pocket - what pocket we're betting in (integer)
    bet - amount of bet (integer)
    toPrint - choses whether we print the results or not (boolean)
    
    Returns:
    The expected return bet 
    """
    totalPocket = 0

    for i in range(numSpins):
        game.spinRoulette()
        totalPocket += game.betPocket(pocket, bet)

    if toPrint:
        print(f"{numSpins} spins of {game}")
        print(f"Expected return betting {pocket} = {str(100*totalPocket/numSpins)}%\n")

    return (totalPocket/numSpins)

def play():
    # Playing the game for 100 and 1M spins
    game = EuropeanRoulette()

    for numSpins in (100, 1000000):
        for i in range(3):
            # Betting 1$ in pocket 2. If we win, we get 2$
            playRoulette(game, numSpins, 2, 1, True)

def findPocketReturn(game, numTrials, trialSize, toPrint = False):
    pocketReturns = []

    for trial in range(numTrials):
        trialVals = playRoulette(game, trialSize, 2, 1, toPrint)
        pocketReturns.append(trialVals)

    return pocketReturns

def simulateGames():
    """ Let's simulate each game and their expected returns """

    numTrials = 20
    resultDict = {}
    games = (FairRoulette, EuropeanRoulette, AmericanRoulette)

    for game in games:
        resultDict[game().__str__()] = []
    
    for numSpins in (1000, 10000, 100000, 1000000):
        print(f"Simulate {numTrials} trials of {numSpins} each:")

        for game in games:
            pocketReturns = findPocketReturn(game(), numTrials, numSpins, False)
            expectedReturn = 100*sum(pocketReturns)/len(pocketReturns)

            print(f"Expected return for {game()} = {str(round(expectedReturn, 4))}%")
        
        print("-" * 5)

def getMeanAndStd(sample):
    """ Return the Mean and Standard Deviation of a Sample dataset """
    mean = sum(sample)/float(len(sample))

    tot = 0.0

    for s in sample:
        tot += (s - mean) ** 2

    std = (tot/len(sample)) ** 0.5

    return mean, std

if __name__ == "__main__":
    # Sanity check
    random.seed(0)

    # Simulate 100 and 1M spins
    # play()
    simulateGames()
