# Carnival barker asks you to pick a # from 1 to 6.
# Then he rolls 3 dice. If your number comes up all 3 times,
# you win $30, if twice $20, if once $10, if 0 times, you lose $10.
# What is expected value of your winnings.

# From John Allen Paulos
# https://twitter.com/JohnAllenPaulos/status/1050387226499133445

import random

def carnival_barker():
    samples = 1000000
    winnings = 0.00

    for i in range(samples):
        my_number = random.randint(1, 6)

        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        die_3 = random.randint(1, 6)

        if die_1 == my_number:
            winnings += 10.00
        if die_2 == my_number:
            winnings += 10.00
        if die_3 == my_number:
            winnings += 10.00
        if not my_number in (die_1, die_2, die_3):
            winnings -= 10.00

    avg_winnings = winnings / samples
    print("Total winnings:", winnings)
    print("Expected winnings per game:", avg_winnings)


if __name__ == '__main__':
    carnival_barker()
