# Chuck-a-Luck
# Chuck-a-Luck is a gambling game often played at carnivals and gambling houses.
# A player may bet on any one of the numbers 1, 2, 3, 4, 5, 6. Three dice
# are rolled. If the player's number appears on one, two, or three of the dice,
# he receives respectively one, two, or three times his original stake, plus
# his own money back; otherwise he loses his stake. What is the player's
# expected loss per unit stake? (Actually, the player may distribute stakes on
# several numbers, but each such stake can be regarded as a separate bet.)
#
# From: Fifty Challenging Problems in Probability
#       by Frederic Mosteller
#       Problem 6

import random

def chuck_a_luck():
    samples = 10000
    bank = 10000

    for i in range(samples):
        dice = [random.randint(1, 6) for x in range(3)]
        #assume the player always bets on 1
        wins = dice.count(1)

        if wins > 0:
            bank += wins
        else:
            bank -= 1

    loss = (10000 - bank) / 10000
    print("Expected loss:", loss)


if __name__ == '__main__':
    chuck_a_luck()
