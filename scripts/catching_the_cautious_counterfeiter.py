# Catching the Cautious Counterfeiter
# (a) The king's minter boxes his coins 100 to a box. In each box
# he puts 1 false coin. The king suspects the minter and from each
# of 100 boxes draws a random coin and has it tested. What is the
# chance the minter's peculations go undetected?
# (b) What if both 100s are replaced by n?
#
# From: Fifty Challenging Problems in Probability
#       by Frederick Mosteller
#       Problem 27

import random

def catching_the_cautious_counterfeiter():
    samples = 10000
    total = 0
    # change values for coins and boxes to answer (b)
    coins = 100
    boxes = 100

    for i in range(samples):
        caught = False
        for j in range(boxes):
            fake = random.randint(1, coins)
            test = random.randint(1, coins)

            if fake == test:
                caught = True

        if caught:
            total += 1
        

    average = total / samples
    print("Chance of going undetected:", 1.0 - average)



if __name__ == '__main__':
    catching_the_cautious_counterfeiter()
