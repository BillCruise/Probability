# An Even Split at Coin Tossing
# When 100 coins are tossed, what is the
# probability that exactly 50 are heads?
#
# From: Fifty Challenging Problems in Probability
#       by Frederic Mosteller
#       Problem 18

import random

def even_split():
    samples = 10000
    total = 0

    for i in range(samples):
        heads = 0
        for j in range(100):
            if(random.random() < 0.5):
                heads +=1

        if(heads == 50):
            total += 1

    average = total / samples
    print("Probability of exactly 50 heads:", average)
            


if __name__ == '__main__':
    even_split()
