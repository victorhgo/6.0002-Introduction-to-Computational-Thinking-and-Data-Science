# Lecture 4 - Stochastic Thinking

Introduction to Stochastic processes and basic probability theory.

#### Content

- [What is Stochastic Thinking](#what-is-stochastic-thinking)
- [Simulation Models](#simulation-models)
- [Stochastic Processes](#stochastic-processes)
- [Probability](#probability)
    [Properties of Probability](#properties-of-probability)
- [Simulating the Rolling Dice](#simulating-the-rolling-dice)
- [Actual Probability versus Sample Probability](#difference-between-actual-probability-and-sample-probability)
- [Birthday Problem](#birthday-problem)

## What is Stochastic Thinking

So far we have focused on problems that can be solved by a **deterministic program**, which given the same initial state and inputs, it will always produce the exact same outputs following the same sequence of operations. This predictability that makes deterministic programs easy to test and debug, also their reliability, because any behaviour and bugs for instance, can be reproduced by just providing the same conditions again. Unfortunately these computations aren't sufficient to tackle some problems as we will see.

Because we live in a world full of uncertainty, many aspects of it can be only modeled as **Stochastic Process**. A process is said to be stochastic if *its next state depends upon the previous states in some random element*, thus the outcome of a stochastic process is usually uncertain. Therefore we can rarely make definitive statements about what they will do, hence we make *probabilistic statements* about what they might do. 

Most of the programs that deals with uncertain situations will be **Simulation Models**

## Simulation Models

**Simulation Models** imitates the activity of a real system. They are widely used to *predict a future state of a physical system* (e.g., the position of planet Earth in reference to the Sun in the next 30 days, phases of the Moon, Stock Market, the temperature of the planet in 100 years). 

Bear in mind that **simulation models** only approximates the reality:

> "All models are wrong, but some are useful"

For instance, the following code will simulate a car running with constant velocity within a time frame (in seconds), where the code is the **experimental device** that provides information about the possible behaviour of the system being modeled:

```py
def car_simulation():
    """
    Using the formula distance = velocity * time to simulate how much distance
    a car will move given the velocity and the time running.
    """
    # Get user input
    try:
        velocity = float(input("Enter the velocity of the car (in m/s): "))
        timeTravel = float(input("Enter the time traveled (in seconds): "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    # Distance formula: d = v * t
    distance = velocity * timeTravel

    print("\nStarting simulation...\n")
    distance = 0.0
    step_time = 1  # seconds

    for t in range(1, int(timeTravel) + 1):
        distance = velocity * t
        print(f"Time: {t:2d}s | Distance covered: {distance:.2f} m")
        time.sleep(0.3)  # slow down the simulation

    print(f"Total (approximated) distance covered: {distance:.2f} meters\n")
```

But since the velocity is constant and the given time is also a constant given number, the result of this simulation will be always the same, no matter how many times we run it with the same values. In the real world we would have to deal with uncertainties like: traffic lights, speed limitations and other obstacles in the road such other cars, poor quality roads and other elements that will make the journey not constant.

## Stochastic Processes 

Let's consider a program to play a dice in a game, it means that it would have a function that simulates the roll of the dice (a six sided one). Consider the specification bellow:

```py
def rollDice():
    """ Returns an int between 1 and 6""""
```

Since this implementation allows the function to return the same number each time it is called, a better implementation would be:

```py
def rollDice():
    """ Returns a randomly chosen int between 1 and 6""""
```

This implementation would require a **stochastic implementation**.

In Python, we can use the module `random` from the standard library to help us writing stochastic programs. Let's write a simple simulation model that simulates the rolling of a dice:

```py
import random

def rollDice():
    """ Returns a randomly chosen int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def rollN(n):
    result = ''

    for i in range(n):
        result = result + ' ' + str(rollDice())
    
    return result
```

The function `random.choice` takes a nonempty sequence as its argument and returns a randomly chosen member in that sequence. Remember that almost all functions in `random` are built using the `random.random` function, which generates a random floating point number between `0.0` and `1.0`.

If we run this program with `rollN(10)`, the sequence `1 1 1 1 1 1 1 1 1 1` and `5 1 4 3 2 5 1 2 5 6` are **equally likely** because the value of each roll does not depend on the values of earlier rolls. In a stochastic process, two events are **independent** if the outcome of one event has no influence on the outcome of the other. Running the simulation above for 10 rolls:

```sh
$ py rollDice.py
    Rolling the dice 10 times:  1 6 5 2 4 1 5 6 6 2

    Rolling the dice 10 times:  2 4 5 2 2 2 2 2 5 4

    Rolling the dice 10 times:  2 5 4 3 2 4 5 3 5 5

    Rolling the dice 10 times:  3 4 5 5 6 6 3 4 5 1

    Rolling the dice 10 times:  2 5 5 2 6 6 4 4 1 3

    Rolling the dice 10 times:  4 1 6 3 3 1 6 1 5 2
```

Another simple implementation is to think about flipping a coin with the values 0 (Heads) and 1 (Tails). We can think the output of `rollN()`as a binary number. When flipping a coin, there are $2^n$ possible sequences that it might return. Each of these sequences are equally likely, thus each has a probability of occurring of $(1/2)^n$.

Implementation of flipping a coin:

```py
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
```

Going back to the `rollDice` problem, first we ask: how many different sequences are there of length 10? Since our dice has 6 sides and we are rolling it 10 times, it can have $6^{10}$ sequences of length 10. Hence the **probability** of rolling ten consecutive 1's is $(1/6)^{10}$, less than one out of sixty million. It's pretty low, but it's not as lower as the probability of any other sequence.

## Probability

The probability of a result having some property (for instance, what is the probability of getting 10 consecutive 1s `(1 1 1 1 1 1 1 1 1)` when rolling a dice?) can be described as the *fraction* of all possible results that has that property. Thus to calculate the probability of rolling `(1 1 1 1 1 1 1 1 1)`:

$$
(1/6)^{10} \approx 1.65 \times 10^{-8}
$$

But what if we want to calculate the probability of getting **any sequence** other than `(1 1 1 1 1 1 1 1 1)` (for instance: `(2 4 7 5 8 9 9 6 1)`)? Then we can simply calculate $1 - (1/6)^{10}$ because the probability of something happening and the probability of the same thing not happening must add up to 1.

1. To calculate the probability of not rolling a 1 in a single roll:
- There are 5 options in the dice that are not 1 `(2, 3, 4, 5, 6)`

Thus the probability of not rolling a 1 in one roll is:

$$
P(\textrm{not rolling 1}) = \frac{5}{6}
$$

2. To calculate the probability of not rolling a 1 in 10 rolls:

- Since the rolls are all independent:

$$
P(\textrm{not rolling 1 in 10 rolls}) = (\frac{5}{6})^{10}
$$

3. To calculate the probability of rolling **at least one 1**:

- The probability of rolling **at least** one 1 in 10 rolls is the complement of the previous roll, because the probability of something happening and the probability of the same thing not happening must add up to 1:

$$
P(\textrm{at least 1 in 10 rolls}) = 1 - (\frac{5}{6})^{10}
$$

Hence the probability of rolling 1 at least once is:

$$
P(\textrm{1 at least once in 10 rolls}) = 1 - (\frac{5}{6})^{10} \approx 0.8385
$$

Probability is all about counting (discrete probability), first we count the number of possible events, then we count the number of events that have the property of interest (for instance when dice roll equals to 1) and we divide one by another. That's why probabilities are always in the range **0 to 1** where 0 means it's impossible for that event to happen and 1 if guaranteed.

Some facts about Probability:

- If the probability of an event occurring is $p$, the probability of it not occurring must be $1 - p$. 

This is a very useful trick because often will be the case when we want to compute the probability of something happening. It's easier to compute the probability of it not happening, and subtract it from 1.

- When events are *independent* of each other, the probability of all events occurring is equal to a **product** of the probabilities of each of the events occurring.

If the probability of A is $0.5$ and the probability is $0.4$, then the probability of A and B is $0.5 * 0.4 = 0.2$. It's much smaller than either of the first two probabilities. (**Multiplicative Law**).

But this only holds if the events are **independent**.

- Two events are said to be **independent** if the outcome of one event has no influence on the outcome of the other.

When we roll a dice for the second time, we assume the outcome will be independent from the first roll.

But it can raise a problem, because people often compute probabilities assuming independence where there is not. Example given in class (football): `New England Patriots x Denver Broncos`. The `Patriots` has a winning percentage of `7 out of 8 (7/8)` (they've won 7 of their 8 games so far) and the `Broncos` has a winning percentage of `6 out of 8 (6/8)`. What's the probability of both winning next Sunday?

$$ P(\textrm{Patriots winning}) \times P(\textrm{Broncos winning}) \equiv \frac{7}{8} * \frac{6}{8} \approx 0.656 \textrm{ or } \frac{42}{64}$$

Simplifying the fraction:

$$P(\text{Both winning next Sunday}) = \frac{21}{32}$$

Hence the probability of **at least one of them losing** is $1 - \frac{21}{32} = \frac{11}{32}$

Here is an example on how the 1 minus rule is useful: we can compute the probability of both winning by simply multiplying and we subtract that from 1 to see the probability of one of them winning.

**But what if the `Patriots` play the `Broncos`?** Now the outcome are not independent, the probability of one of them losing is influenced by the probability of the other winning.

### Properties of Probability

- Non-negativity: The property of any event $P(E)$ is always non-negative, thus $P(\textrm{E}) \geq 0$

- Range: As we stated before probabilities are always in the range **0 to 1** where 0 indicates an impossible event and 1 indicates a certain or sure event.

- Normalization: The sum of probabilities for all possible outcomes in a sample space is 1.

**Rules for Probability**

Let A and B be events such that:

- **Addition Rule**: For any two events A and B, the probability of either A or B occurring (the union of A and B) is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

- **Mutually Exclusive Events**: If A and B are mutually exclusive (these events cannot happen at the same time) then their intersection $P(A \cap B) = 0$ and the *addition rule* $P(A \cup B) = P(A) + P(B)$

- **Complementary Rule**: The probability of an event not happening (called the complement of A, or $A^C$) is $P(A^C) = 1 - P(A)$.

## Simulating the Rolling Dice

In the following simulation, we will take a look on an example of simulating the rolling of a die, where we give a `goal` to it (For instance, wheter we get a `(1 1 1 1)`) within the number of trials. Then we are going to check if each trial has the property we want (the goal), incrementing the total counting. Then we sum up the results and divide by the number of trials.

```py
def runSimulation(goal, numTrials, txt):
    total = 0

    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDice())

        if result == goal:
            total += 1
    
    print(f"Actual probability of {txt} is {round(1/(6**len(goal)), 8)}")
    estimateProbability = round(total/numTrials, 8)
    print(f"Estimated probability of {txt} is {round(estimateProbability,8)}")

# Running simulation for 1000 trials
print("What's the probability of getting (1 1 1 1 1) with 1000 trials?")
runSimulation('11111', 1000, '11111')
print("\n-\n")
```

Running the above code we get the following result:

```sh
$ py rollDice.py

    What's the probability of getting (1 1 1 1 1) with 1000 trials?
    Actual probability of 11111 is 0.0001286
    Estimated probability of 11111 is 0.0
```

How did we know the estimated probability would be zero? Because `random.choice` is not actually random, and nothing we do in a computer is actually random. But computers generate numbers that are *pseudorandom*. Numbers are generated by an algorithm that given one number, generates the next number in a sequence. This number is called **seed**. Usually the computer gets this seed by reading the computer's clock.

We can make a program predictable, which makes it easier to debug (make sure to debug with more than one value). We just call `random.seed()` and gives it a value. For the same seed, we always get the same sequence of random values.

**But why the simulation gave us the wrong answer?** The actual probability is 0.0001286 but it estimated a probability of 0.0. Since we run with 1000 trials, it means that within this 1000 run times it didn't get a sequence `(1 1 1 1 1)`, hence the numerator of the division at the bottom was 0.

## Difference between actual probability and sample probability

Analysing the last simulation's results, we have to be careful to understand the difference between what's in this case an actual probability versus what is a sample probability.

If we are doing a simulation of an event which is pretty rare, we want to try it on a very large number of trials. For instance:

```py
# Running simulation for 10 000 trials
print("What's the probability of getting (1 1 1 1 1) with 10 000 trials?")
runSimulation('11111', 10000, '11111')
print("\n-\n")

# Running simulation for 100 000 trials
print("What's the probability of getting (1 1 1 1 1) with 100 000 trials?")
runSimulation('11111', 100000, '11111')
print("\n-\n")

# Running simulation for 1M trials
print("What's the probability of getting (1 1 1 1 1) with 1 000 000 trials?")
runSimulation('11111', 1000000, '11111')
```

Running the above simulation we get:

```sh
$ py rollDice.py

What's the probability of getting (1 1 1 1 1) with 10 000 trials?
Actual probability of 11111 is 0.0001286
Estimated probability of 11111 is 0.0002

-

What's the probability of getting (1 1 1 1 1) with 100 000 trials?
Actual probability of 11111 is 0.0001286
Estimated probability of 11111 is 0.00018

-

What's the probability of getting (1 1 1 1 1) with 1 000 000 trials?
Actual probability of 11111 is 0.0001286
Estimated probability of 11111 is 0.000112

What's the probability of getting (1 1 1 1 1) with 10 000 000 trials?
Actual probability of 11111 is 0.0001286
Estimated probability of 11111 is 0.0001284
```

We can see that as we increase the number of trials, we also increase the estimated probability for this event to happen, making it closer to the actual probability.

Therefore if we are writing a simulation to compute the probability of an event and this event is moderately rare, then we better run a lot of trials before we can believe our estimated probability.

Hence:

- Takes a lot of trials to get a good estimate of the frequency of a rare event.

- We should always know if we're getting an estimated probability and not confuse with the actual probability.

## Birthday Problem

This is a famous problem which states: what's the probability of at least two people in a group having the same birthday?

Suppose we have 367 people in the group, what's the probability of at least two of them sharing a birthday? It's one! By the pigeonhole principle which states that:

> If you have more items (or pigeons) than available categories (called pigeonholes), at least one category must contain more than one item. (or at least one pigeonhole will have more than one pigeon).

If we make a simplified assumption that each birthdate is equally likely, then there's actually a nice solution for it:

$$
1 - \frac{366!}{366^N \times (366 - N)!}
$$

Where $N$ is the number of people sharing a birthday.

Not this is also a question where it's easier to compute the opposite of what we're trying to do and subtract it from 1. So the fraction represents the probability of two people not sharing a birthday.

Let's do a simulation for this problem:

```py
def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthdays = [0] * 366

    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    
    return max(birthdays) >= numSame
```

This function takes two arguments: the number of people in the group and the number that we asking `do they have the same birthday?`. Since we're assuming that every birthday is equally likely, then possible dates range from 1 to 366. We keep a track of the number of people born in each date by starting with `None`. Then for `person p` in the range of number of people, we make a random choice of the possible dates and increment the element of the list by 1. Then at the end we can check the maximum number of birthdays and check if it's greater than or equal to the number of same.

Finishing up the simulation:

```py
def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0

    for trial in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1

    return numHits/numTrials

for numPeople in [10, 20, 40, 100]:
    print(f"For {numPeople} people, the estimate probability of a shared birthday is {birthdayProb(numPeople, 2, 10000)}")
    
    numerator = math.factorial(366)
    denom = (366**numPeople)*math.factorial(366 - numPeople)
    print(f"Actual probability of N = 100 = {1 - numerator/denom}\n")
```

Running with the test we get the following output:

```sh
$ py sameBirthday.py

    For 10 people, the estimate probability of a shared birthday is 0.1194
    Actual probability of N = 100 = 0.1166454118039999

    For 20 people, the estimate probability of a shared birthday is 0.4164
    Actual probability of N = 100 = 0.4105696370550831

    For 40 people, the estimate probability of a shared birthday is 0.8915
    Actual probability of N = 100 = 0.89054476188945

    For 100 people, the estimate probability of a shared birthday is 1.0
    Actual probability of N = 100 = 0.9999996784357714
```