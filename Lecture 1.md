# Introduction and Optimization Problems

In this lecture, we will see how can we use computational models to understand the world in which we live, in particular he discusses the knapsack problem and greedy algorithms.

In this part, programming assignments will be a bit easier, focused on to problem to be solved than programming itself. But the content is more abstract. We'll also discuss a bit about Software Engineering.

This part of the course is an introduction to data science.

## Using Computational Models

In this part we are expected to use computation to help understand the real world, designing experiments that allow us to understand something that happened or predict the future. This can answer our question: "What is a model?".

Science is moving out of labs going into computers.

We have three main categories of models:

    1. Optimization Models
    2. Statistical Models
    3. Simulation Models

Let's dive in into Optimization Models, specially greedy algorithms.

## What is an Optimization Model?

Optimization Models are simple, we start with an objective function that's either to be maximized or minimized. For instance if we are going from Berlin to München, we want to find a rout by car, train or plane that **minimizes** the journey's time. So the objective function in this case would be the minutes spend in transit getting from *A* to *B*.

We might often layer on top of this objective function a **set of constraints** (limitations, restrictions) that we have to obey (can be also empty). For instance, maybe the fastest way to get from Berlin to München is by plane but it would cost more than what I can spend, so this option would be off the table. Or we should get to München before 17h but the bus gets there at 18h.

## The knapsack (backpack) problem

Imagine we have a backpack that we want to store some items on it, but we have a limited strength, meaning there is a maximum weight that we can carry. Usually we would like to store more items than we can carry. So how do we choose which items we take and which we leave behind?

This problem has two variants:

    1. 0/1 knapsack problem:

        This mean that we either take the object or we don't. It's much more complicated because once we take a decision it will affect every subsequent one.

    2. Continuous or fractional knapsack problem:

        This mean that we can take pieces of the object. (This is easy to solve).

We can solve the **0/1 Problem** with an **Greedy Algorithm**.

### 0/1 knapsack problem example and formalized

Imagine that we have a calorie restriction, and we need to choose the best food combination without exceeding the calorie restriction, where the calorie restriction is the maximum weight our backpack can carry.

Each food item is represented by a pair **<value, weight>**, and the knapsack can accommodate items with a total weight of no more than **w**. We will use a vector **L** of length **n** to represent the set of available items such that each element of this vector is an item. (Assuming we have **n** items to choose from)

We also have a vector **V** of length **n** to indicate whether or not items are taken. For instance: If ```V[i] = 1```, item ```L[i]```is taken, if ```V[i] = 0```, item ```L[i]```is not taken.

Find a **V** that maximizes:

$$\sum_{i=1}^{n - 1} V[i] \cdot L[i].value$$

And it will be subject to the restrictions that:

$$\sum_{i=1}^{n - 1} V[i] \cdot L[i].weight \leq w$$

### Using a Brute Force Algorithm

This algorithm will look like:

1. Enumerate all possible combinations of items. (Generate all subsets of the set of items, called **power set**).

2. Remove all of the combinations whose total units exceeds our allowed weight.

3. From the remaining combinations, choose any one whose value is the largest.

But unfortunately is not very practical, the power set can be huge, and also **V** can have as many different binary numbers as can be represented in *n* bits.

For instance, if there are 100 items to choose from, the power set is of size $10^{30}$ approximately.

**Is there a better algorithm to solve this issue?**

Sadly the answer is **No**, for the knapsack problem and many other Optimization problems are inherently exponential, meaning there is no algorithm that provides an exact solution for this problem with worse case running time is not exponential in number of items.

### Greedy Algorithm - Practical Alternative

```
while knapsack is not full
    put "best" available item in knapsack
```

What means to be "best available item"? It can be the most valuable, least expensive (fewer calories) or the highest value/units ratio (a calorie in a glass of beer can be more valuable than in a box of chocolate for instance).

A practical example: when sitting down for a meal, we know how much we value different foods (pizza is better than apples), but with the calorie restriction, we don't want to consume more than we should. So choosing what to eat is a **knapsack problem**. The menu:

|   Food   | Wine | Beer  | Pizza | Burger | Chips | Coke | Apple | Donuts |
|:--------:|:----:|:-----:|:-----:|:------:|:-----:|:----:|:-----:|:------:|
|   Value  |  89  |   90  |   30  |   50   |   90  |  79  |   90  |   10   |
| Calories |  123 |  154  |  258  |   354  |  365  |  150 |   95  |   195  |

We can now write a program that will find an optimal menu. First of all, we need to abstract our Food object as:

```py
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
```

Where ```density``` is the value divided by the cost (in calories) and getter methods to get the values.

We will also have a build menu function to help us build the meal's menu with the values and calories:

```py
def buildMenu(names, values, calories):
    """ names, values, calories are lists of same length
        names is a list of strings
        values and calories are lists of numbers
        return list of Foods """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu
```

Here's the implementation of Greedy algorithm. It's called flexible greedy because of the ```keyFunction``` parameter, this will map the elements of items to numbers, it will be used to sort the items. We will sort from best to worst and ```keyFunction``` will tell what we mean by **best**.

```py
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
```

### What is the efficiency of this algorithm?

Remember that ```sorted()``` in the worst case scenario has a complexity of O($n \log n$) where $n = $ *len(items)*. And the loop we go thru it *n times*, meaning the complexity is O($n$). So the overall complexity of this Greedy algorithm is O($n \log n$). Which is a very efficient algorithm, we could do that for huge numbers.

### Using Greedy:

Here's a test using this greedy algorithm:

```py
def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print(f"Total value of items taken = {val}")

    for item in taken:
        print('   ', item)
```

Where we take the items, constraints (restriction) and we call the greedy with ```keyFunction``` and prints what we have. And we can finally call a test for it as:

```py
def testGreedys(foods, maxUnits):
    print(f"Use greedy by value to allocate {maxUnits} calories")

    testGreedy(foods, maxUnits, Food.getValue)
    
    print(f"\nUse Greedy by cost to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x)) # <- Observation 1* Check lambda chapter

    print(f"\nUse greedy by density to allocate {maxUnits} calories")
    testGreedy(foods, maxUnits, Food.density)

# Foods Menu as defined previously.
names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)

# Test 1000 calories
testGreedys(750)
```

When running this code, we get:

```sh
> python3 greedy.py

Use greedy by value to allocate 750 calories
Total value of items taken = 284.0
    burger: < 100, 354>
    pizza: < 95, 258>
    wine: < 89, 123>

Use Greedy by cost to allocate 750 calories
Total value of items taken = 318.0
    apple: < 50, 95>
    wine: < 89, 123>
    cola: < 79, 150>
    beer: < 90, 154>
    donut: < 10, 195>

Use greedy by density to allocate 750 calories
Total value of items taken = 318.0
    wine: < 89, 123>
    beer: < 90, 154>
    cola: < 79, 150>
    apple: < 50, 95>
    donut: < 10, 195>
```

Why we get different answers? A greedy algorithm makes a sequence of local optimizations, then chooses the locally optimal answer every point. And that doesn't necessary add up to a globally answer. Example is the hill climbing demonstration.

### The Pros and Cons of Greedy Algorithms

While greedy algorithms are easy to implement and really efficient computationally, they does not always yeld the best solution and it does not even know how good the approximation is. Next chapter we will look finding truly optimal solutions.


