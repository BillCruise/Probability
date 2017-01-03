# Craps
# The game of craps, played with two dice, is one of America's fastest
# and most popular gambling games. Calculating the odds associated with
# it is an instructive exercise.
# The rules are these. Only totals for the two dice count. The player
# throws the dice and wins at once if the total for the first throw is
# 7 or 11, loses at once if it is 2, 3, or 12. Any other throw is called
# his "point." If the first throw is a point, the player throws the dice
# repeatedly, until he either wins by throwing his point again or loses
# by throwing 7. What is the player's chance to win?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 9

import random

def craps():
    samples = 10000
    wins = 0
    losses = 0

    for i in range(samples):
        total = roll()

        if total == 7 or total == 11:
            wins += 1
        elif total == 2 or total == 3 or total == 12:
            losses += 1
        else:
            point = total
            loop = True
            while loop:
                total = roll()
                if total == 7:
                    losses += 1
                    loop = False
                elif total == point:
                    wins += 1
                    loop = False
                # else: keep rolling

    average = wins / samples
    print("Player's chance to win at craps:", average)

def roll():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return (d1 + d2)


if __name__ == '__main__':
    craps()
