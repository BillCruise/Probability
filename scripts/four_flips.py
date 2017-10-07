# Four flips
# You are to flip a fair coin four times.
# If heads and tails each appear twice in four flips,
# he will pay you $11. If they don't, you must pay $10.
# Do you take the bet?

import random

def four_flips():
    samples = 10000
    wins = 0

    for i in range(samples):
        heads = 0
        for j in range(4):
            if random.random() < 0.5:
                heads += 1
        if heads == 2:
            wins += 1

    average = wins / samples
    print("Total wins:", wins)
    print("Winning probability:", average)


if __name__ == '__main__':
    four_flips()
