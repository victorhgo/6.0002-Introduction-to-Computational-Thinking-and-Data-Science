# Lecture 6 - Monte Carlo Simulation

Monte Carlo Simulation and Roulette

#### Contents

- [What is Monte Carlo Simulation](#what-is-monte-carlo-simulation)
- [Law of Large Numbers (or Bernoulli's Law)](#law-of-large-numbers-or-bernoullis-law)

## What is Monte Carlo Simulation?

Monte Carlo simulation is a method of estimating the value of *an unknown quantity* using the principles of **inferential statistics**.

Read more from Section 15.1 to 15.4 and Chapter 16 to develop further.

On inferential statistics we have:

- **Population** which is the set of examples (universe set of possible examples)

In case of *Solitaire* game, the **population** is the universe of all possible solitaire games that we can possible play. We can also think of Chess, where the **population** is also going to be the universe of every possible movements (a very large set, we can say).

- **Sample** is a *proper subset* of a population

We could take a subset of every possible games in Solitaire and work with it as a **sample**.

A **random sample** tends to exhibit the same properties as the population from which it is drawn, which we can observe working with population ages, which we did with **random walks**.

An example with flip coins: Estimate the fraction of heads that we would get if a coin is flipped an infinite number of times. We can achieve this by the following simulation:

```py
def flipCoin():
    """ Assumes a normal coin with Head or Tail
    Flips the coin and return whether it got Heads (H) or Tails (T) """
    coin = ['H','T']

    return random.choice(coin)
```

## Law of Large Numbers (or Bernoulli's Law)

This law states that

    In repeated independent tests with the same actual probability p 
    of a particular outcome in each test, the change that the fraction
    of times that outcome occurs differs from p converges to zero 
    as the number of trials goes to infinity.

The Gambler's Fallacy x Regression to the Mean : they're different!!!

## Regression to the Mean

Following an extreme random event, the next random event is likely to be less extreme, for instance in the roulette game: if we spin a *fair roulette* 10 times and get 100% reds, that's an extreme event (`probability = 1 / 1024`)

## Quantifying Variation in Data

Fundamental Question of Computational Statistics - How many samples do we need to look at before we can have real, justifiable confidence in our answer?

$$ \textrm{Variance}(X) = \frac{\sum_{x \in X} (x - \mu )^2}{|X|} $$

Where X is the sample dataset, a list of data examples. Variance is the average (or Mean) of value, that's $\mu = \textrm{Mean}$. and $|X|$ is the size of this list.

For each value $x$ in this dataset $X$, we compare the difference of this value to the mean $\mu$ and square this difference, we sum them up then we divide by the size of the set. Why this division is important? Because we don't want to say something has a high variance just because it has many members.

If all values of a set has the same value, what's the variance? It's equal to $0$

Then we can calculate the **standard deviation $\sigma$** of a sample dataset as:

$$ \sigma (X) = \sqrt{\frac{1}{|X|} \cdot \sum_{x \in X} (x - \mu)^2} $$

It's simply the square root of the variance. Standard deviation by itself does not mean anything because we always have to think about it in the context of the mean. Which means that if we have a standard deviation of 100 and the mean is also 100, then it's a pretty big number, if the mean is 1 billion and the standard deviation is 100, then it's a pretty small number.

The **standard deviation** tells us how much the data are **dispersed** in a dataset. A **low standard deviation** means the data points are clustered closely around the average (or mean), which means that we can trust the **mean** as a good predictor for data points. A **high standard deviation** means the data is more spread out, which means the **mean** it's not a good predictor for the datapoint. It simply quantifies the *amount of variation* in a dataset.

We can calculate the **Mean** and **Standard Deviation** with the following functions:

```py
def getMean(sample):
    """ Assumes sample is a list with statistical data 
    Returns the Mean of sample"""
    try:
        return round(sum(sample)/len(sample),2)
    
    except TypeError:
        return "Sample could not be loaded"

def standardDeviation(sample):
    """ Assumes Sample is a list with statistical data
    Returns the Standard Deviation of data """
    total = 0.0

    try:
        mean = getMean(sample)
        total += sum((num - mean) ** 2 for num in sample)

        return round(math.sqrt(total/len(sample)),3)
    
    except TypeError:
        return "Sample could not be loaded"
```

## Confidence Levels and Intervals

Instead of estimating an unknown parameter by a single value (for instance, the mean of a set of trials on the roulette), a **confidence interval** provides a range that's likely to contain the unknown value and a confidence that the unknown value lays within that range. For instance, the return of betting a pocket 10k times in European Roulette is $-3.3$%. The margin of error is $\pm 3.5$% with a $95$% level of confidence.

37.58
