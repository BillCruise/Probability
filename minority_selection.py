# Minority Selection
# What is the probability that no member of a minority party
# will be selected out of N slots?
# Example: A certain minority party is 10% of a population. In a
# random drawing of 10 nominees, what are the odds that no
# member of the minority party is selected?

import random

def selection():
    trials = 10000
    represented = 0

    for i in range(trials):
        rep = False
        for i in range(10):
            d = random.randint(1, 10)
            if d == 10:
                rep = True

        if(rep):
            represented += 1

    average = represented / trials
    print("Minority odds of being represented:", average)
    

if __name__ == '__main__':
    selection()
