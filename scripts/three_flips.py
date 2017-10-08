# Three flips
# The following game has a $10 entry fee.
# You are to flip a fair coin three times.
# The first time it comes up heads you are paid $5.
# The second time it comes up heads you're paid an additional $7.
# The third time it comes up heads you're paid $9 more,
# for a possible maximum prize of $21.
# Would you pay the $10 entry fee to play?

import random

def three_flips():
    samples = 10000
    winnings = 0
    prizes = (5, 7, 9)

    for i in range(samples):
        heads = 0
        for j in range(3):
            if random.random() < 0.5:
                winnings += prizes[heads]
                heads += 1

    winnings = winnings - (10 * samples) # subtract entry fees
    average = winnings / samples
    print("Total winnings:", winnings)
    print("Average winnings:", average)
            


if __name__ == '__main__':
    three_flips()
