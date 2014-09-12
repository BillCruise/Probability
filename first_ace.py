# The First Ace
# Shuffle an ordinary deck of 52 playing cards containing four aces.
# Then turn up cards from the top until the first ace appears.
# On the average, how many cards are required until the first ace appears?
#
# From: Fifty Challenging Problems in Probability
#       by Frederic Mosteller
#       Problem 40

import random

def first_ace():
    samples = 10000
    total = 0

    for i in range(samples):
        deck = [x for x in range(52)]
        random.shuffle(deck)

        count = 1
        for card in deck:
            if card < 4:
                break
            else:
                count += 1
        total += count

    average = total / samples
    print("Average number of cards until the first ace:", average)


if __name__ == '__main__':
    first_ace()
