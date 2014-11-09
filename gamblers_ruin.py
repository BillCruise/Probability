# Gambler's Ruin
# Player M has $1, and Player N has $2. Each play gives one of the
# players $1 from the other. Player M is enough better than Player N
# that he wins 2/3 of the plays. They play until one is bankrupt.
# What is the chance that Player M wins?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 36

import random

def gamblers_ruin():
    samples = 10000
    m_wins = 0
    odds = 2 / 3

    for i in range(samples):
        m = 1
        n = 2

        while m > 0 and n > 0:
            if random.random() < odds:
                m += 1
                n -= 1
            else:
                m -= 1
                n += 1

        if m > 0:
            m_wins += 1

    average = m_wins / samples
    print("Chance that Player M wins:", average)



if __name__ == '__main__':
    gamblers_ruin()
