import random
import pylab

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

class OddField(Field):
    def __init__(self, numHoles = 1000,
                 xRange = 100, yRange = 100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-xRange, xRange)
            y = random.randint(-yRange, yRange)
            newX = random.randint(-xRange, xRange)
            newY = random.randint(-yRange, yRange)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc

    def moveDrunk(self, drunk):
        Field.moveDrunk(self, drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
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

# Plotting the simulation now
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of',
              numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle,
                   label = dClass.__name__)
    pylab.title('Mean Distance from Origin ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = OddField()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        meanX = sum(abs(xVals))/len(xVals)
        meanY = sum(abs(yVals))/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle,
                      label = dClass.__name__ +\
                      ' mean abs dist = <'
                      + str(meanX) + ', ' + str(meanY) + '>')
    pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower center')

if __name__ == "__main__":
    # Sanity Check
    random.seed(0)

    plotLocs((UsualDrunk, MasochistDrunk), 10000, 1000)

    pylab.show()