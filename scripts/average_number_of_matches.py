# Average Number of Matches
# From a shuffled deck, cards are laid out on a table one at a time,
# face up from left to right, and then another deck is laid out so
# that each of its cards is beneath a card of the first deck.
# What is the average number of matches of the card above and
# the card below in repetitions of this experiment?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 45

import random

def number_of_matches():
    samples = 10000
    total = 0

    for i in range(samples):
        deck1 = [x for x in range(52)]
        random.shuffle(deck1)
        deck2 = [x for x in range(52)]
        random.shuffle(deck2)

        matches = 0
        zipped = zip(deck1, deck2)

        for pairs in zipped:
            if pairs[0] == pairs[1]:
                matches += 1

        total += matches

    average = total / samples
    print("Average number of matches:", average)
                

if __name__ == '__main__':
    number_of_matches()
