# Yahtzee!
# What is the probability of rolling five of a kind when rolling
# five six-sided dice three times?

import random

def yahtzee():
    samples = 100000
    successes = 0

    for i in range(samples):
        for j in range(3): # roll the dice 3 times
            dice = []
            for k in range(5): # roll 5 dice
                dice.append(random.randint(1, 6))

            if all(die == dice[0] for die in dice):
                successes += 1

    average = successes / samples
    print("Probability of rolling 5 of a kind:", average)



if __name__ == '__main__':
    yahtzee()
