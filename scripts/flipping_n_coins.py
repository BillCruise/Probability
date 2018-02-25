# Flipping n coins
# You have 100 coins and you flip them all at the same time.
# Any that come up tails you set aside. The ones that come up
# heads you flip again. How many rounds do you expect to play
# before only one coin remains?
# What if you start with 1000 coins?

import random

def flipping_n_coins():
    samples = 10000
    rounds = 0
    
    for i in range(samples):
        coins = 100
        while coins > 1:
            heads = 0
            for i in range(coins):
                if random.random() <= 0.5:
                    heads += 1
            rounds += 1
            coins = heads

    average = rounds / samples
    print("Average number of rounds:", average)


if __name__ == '__main__':
    flipping_n_coins()
