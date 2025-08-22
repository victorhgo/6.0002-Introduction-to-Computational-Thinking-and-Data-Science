class Food(object):
    def __init__(self, name, value, w):
        self.name = name
        self.value = value
        self.calories = w
        
    # Getter methods
    def getValue(self):
        return self.value
    
    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue()/self.getCost()
    
    def __str__(self):
        """ Printing method"""
        return self.name + ": < " + str(self.value)\
            + ", " + str(self.calories) + ">"
    
def buildMenu(names, values, calories):
    """ names, values, calories are lists of same length
        names is a list of strings
        values and calories are lists of numbers
        return list of Foods """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu

def greedy(items, maxCost, keyFunction):
    """ Assumes items is a list, maxCost >= 0,
        keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True)

    result = []

    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()

    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print(f"Total value of items taken = {val}")

    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print(f"Use Greedy by value to allocate {maxUnits} calories")

    testGreedy(foods, maxUnits, Food.getValue)
    
    print(f"\nUse Greedy by cost to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

    print(f"\nUse Greedy by density to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)

# Test 1000 calories
testGreedys(foods, 1500)