# Lonely Card Game
#
# On snowy afternoons, you like to play a solitaire “game” with a standard,
# randomly shuffled deck of 52 cards. You start dealing cards face up, one
# at a time, into a pile. As you deal each card, you also speak aloud,
# in order, the 13 card faces in a standard deck: ace, two, three, etc.
# (When you get to king, you start over at ace.) You keep doing this
# until the rank of the card you deal matches the rank you speak aloud,
# in which case you lose. You win if you reach the end of the deck
# without any matches.
#
# What is the probability that you win?
#
# From: Can You Deal With These Card Game Puzzles?
#       http://fivethirtyeight.com/features/can-you-deal-with-these-card-game-puzzles/

import random

def lonely_card_game():
    samples = 10000
    wins = 0

    deck1 = [(x % 13) for x in range(52)]

    for i in range(samples):
        deck2 = deck1[:]
        random.shuffle(deck2)

        matches = 0
        zipped = zip(deck1, deck2)

        for pairs in zipped:
            if pairs[0] == pairs[1]:
                matches += 1

        if matches == 0:
            wins += 1

    average = wins / samples
    print("Probability of winning:", average)
        



if __name__ == '__main__':
    lonely_card_game()
