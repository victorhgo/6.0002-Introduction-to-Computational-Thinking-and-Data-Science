import random

class Location(object):
    def __init__(self, x, y):
        """ x and y are floats """
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        """ deltaX and deltaY are floats """
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()

        # Pythagorean theorem
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', '\
                   + str(self.y) + '>'

class Drunk(object):
    def __init__(self, name = None):
        """ Assumes name is a string """
        self.name = name
    
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous Drunk.'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
    
class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.1), (0.0, -0.9),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Drunk already exists')
        else:
            self.drunks[drunk] = loc

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk is not in the field")
        
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk is not in the field")
        
        xDist, yDist = drunk.takeStep()
        # use Location's move method to get new location
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

# Testing the simulation:

# Simulating a single walk
def walk(field, drunk, numSteps):
    """ Assumes: field and drunk in Field
    numSteps an int >= 0.
    Moves drunk numSteps times
    Returns: the distance between the final location and the location
    at the start of the walk."""

    start = field.getLoc(drunk)

    for step in range(numSteps):
        field.moveDrunk(drunk)
    
    return start.distFrom(field.getLoc(drunk))

# Simulating Multiple Walks
def simWalks(numSteps, numTrials, drunkClass):
    """ Assumes numSteps an int >= 0, numTrials and int > 0 and 
    dClass a subclass of Drunk.

    Simulates numTrials walks of numSteps steps each.
    
    Returns a list of the final distances for each trial. """

    Drunk1 = drunkClass()

    origin = Location(0, 0)
    distances = []

    for trial in range(numTrials):
        field = Field()
        field.addDrunk(Drunk1, origin)

        #distances.append(round(walk(field, Drunk1, numTrials), 1))
        distances.append(round(walk(field, Drunk1, numSteps), 1))

    return distances

# A test for the walking simulation
def drunkTest(walkLengths, numTrials, drunkClass):
    """ Assumes walkLengths is a sequence of ints >= 0
    numTrials an integer > 0
    drunkClass a subclass of Drunk
    
    For each number of steps in walkLengths, run simWalks with
    numTrials walks and print results """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, drunkClass)

        print(f"{drunkClass.__name__} random walk of {numSteps} steps")

        print(f" Mean = {round(sum(distances)/len(distances), 4)}")
        print(f" Max = {max(distances)} and Min = {min(distances)}")

# A test simulation for all drunks
def simAll(drunkKinds, walkLengths, numTrials):
    for drunkClass in drunkKinds:
        drunkTest(walkLengths, numTrials, drunkClass)

if __name__ == "__main__":
    """ Testing for a usual drunk with walks from length:
     10 steps, 100 steps, 1000 steps and 10000 steps 
    100 trials """
    #drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)
    #drunkTest((10, 100, 1000, 10000), 100, MasochistDrunk)

    # Sanity check: (0 steps, 1 step, 2 steps)
    #drunkTest((0, 1, 2), 100, UsualDrunk)

    # Sanity check for all drunks with random.seed(0)
    #random.seed(0)

    simAll((UsualDrunk, MasochistDrunk), (1000, 10000), 100)