# Curing the Compulsive Gambler
# Mr. Brown always bets a dollar on the number 13 at roulette against
# the advice of Kind Friend. To help cure Mr. Brown of playing roulette,
# Kind Friend always bets Brown $20 at even money that Brown will be
# behind at the end of 36 plays. How is the cure working?
# (Most American roulette wheels have 38 equally likely numbers.
# If the player's number comes up, he is paid 35 times his stake and
# gets his original stake back; otherwise he loses his stake.)
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 7

import random

def curing_the_compulsive_gambler():
    samples = 10000
    total = 0

    for i in range(samples):
        bank = 0
        for j in range(36):
            spin = random.randint(1, 38)
            if spin == 13:
                bank += 35
            else:
                bank -= 1

        if bank >= 0:
            bank += 20
        else:
            bank -= 20

        total += bank

    average = total / samples
    print("Average winnings after 36 spins:", average)
        

if __name__ == '__main__':
    curing_the_compulsive_gambler()
