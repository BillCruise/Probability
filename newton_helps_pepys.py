# Isaac Newton Helps Samuel Pepys
# Pepys wrote Newton to ask which of three events is more likely:
# that a person get (a) at least 1 six when 6 dice are rolled,
# (b) at least 2 sixes when 12 dice are rolled, or (c) at least 3
# sixes when 18 dice are rolled. What is the answer?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 19

import random

def newton_helps_pepys():
    samples = 10000
    totals = [ 0, 0, 0 ]

    for i in range(samples):
        # roll 6 dice
        sixes = 0
        for j in range(6):
            if(random.randint(1, 6) == 6):
                sixes += 1
        if(sixes >= 1):
            totals[0] += 1

        # roll 12 dice
        sixes = 0
        for j in range(12):
            if(random.randint(1, 6) == 6):
                sixes += 1
        if(sixes >= 2):
            totals[1] += 1

        # roll 18 dice
        sixes = 0
        for j in range(18):
            if(random.randint(1, 6) == 6):
                sixes += 1
        if(sixes >= 3):
            totals[2] += 1

    averages = [x / samples for x in totals]


    print("Probability of at least 1 six when 6 dice are rolled:", averages[0])
    print("Probability of at least 2 sixes when 12 dice are rolled:", averages[1])
    print("Probability of at least 3 sixes when 18 dice are rolled:", averages[2])

    
if __name__ == '__main__':
    newton_helps_pepys()
