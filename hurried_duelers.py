# The Hurried Duelers
# Duels in the town of Discretion are rarely fatal. There, each contestant
# comes at a random moment between 5 AM and 6 AM on the appointed day and
# leaves exactly 5 minutes later, honor served, unless his opponent arrives
# within the time interval and then they fight.
# What fraction of duels lead to violence?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 26

import random

def hurried_duelers():
    samples = 10000
    total = 0

    for i in range(samples):
        d1 = random.randint(1, 3600)
        d2 = random.randint(1, 3600)
        if abs(d1 - d2) < 300:
            total += 1

    average = total / samples
    print("Fraction of duels that lead to violence:", average)


if __name__ == '__main__':
    hurried_duelers()
